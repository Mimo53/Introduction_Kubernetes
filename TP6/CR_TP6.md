# TP 5 — Mettons à jour nos applications

## Objectifs du TP

- Comprendre et mettre en place une stratégie de RollingUpdate
- Configurer des readiness et liveness probes
- Observer le comportement d'une mise à jour progressive
- Effectuer un rollback

Livrables :
- Manifests Kubernetes mis à jour
- Un compte rendu avec les difficultés rencontrées, et les résultats de chaque exercice.

## Prérequis

- Avoir un compte SSPCloud
- Avoir déployé l'application du TP2 (API Python) avec son Service et son Ingress (TP3)

---

## Exercice 1 : Ajout des probes

### Étape 1 : Ajouter un endpoint de health check

Le fichier `main.py` a été modifié pour ajouter une route `/health` dédiée au health check :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return "world"

@app.get("/health")
def health():
    return {"status": "ok"}
```

L'image a ensuite été taguée en `v1` (version sans health check) puis une nouvelle image `v2` a été buildée et poussée sur Docker Hub :

```bash
# Tagger l'image actuelle en v1
docker tag moonshayne/tp1-exo1:latest moonshayne/tp1-exo1:v1
docker push moonshayne/tp1-exo1:v1

# Builder et pousser la v2 avec l'endpoint /health (multi-arch pour Onyxia)
docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v2 --push .
```

### Étape 2 : Configurer les probes dans le Deployment

Le manifest `app.yaml` a été mis à jour pour utiliser l'image `v2` et ajouter les deux probes :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helloworld-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: helloworld
  template:
    metadata:
      labels:
        app: helloworld
    spec:
      containers:
      - name: helloworld-container
        image: moonshayne/tp1-exo1:v2
        imagePullPolicy: Always
        ports:
        - containerPort: 8081
        readinessProbe:
          httpGet:
            path: /health
            port: 8081
          initialDelaySeconds: 5
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /health
            port: 8081
          initialDelaySeconds: 10
          periodSeconds: 10
```

Vérification que les probes sont bien configurées :

```bash
kubectl apply -f app.yaml
kubectl describe pod helloworld-app-<id> | grep -A5 "Liveness\|Readiness"
```

Résultat :
```
Liveness:   http-get http://:8081/health delay=10s timeout=1s period=10s #success=1 #failure=3
Readiness:  http-get http://:8081/health delay=5s timeout=1s period=5s #success=1 #failure=3
```

Tous les pods passent à `READY 1/1` une fois les probes validées.

### Étape 3 : Comportement des probes

**Que se passe-t-il si la readinessProbe échoue ?**

Le pod est retiré du Service — il ne reçoit plus aucun trafic. Kubernetes attend qu'il redevienne prêt sans le redémarrer. Cela protège les utilisateurs : aucune requête n'est envoyée à un pod qui ne peut pas encore répondre correctement (démarrage en cours, connexion BDD non établie, etc.).

**Que se passe-t-il si la livenessProbe échoue ?**

Kubernetes considère le pod comme mort et le redémarre automatiquement. C'est le mécanisme d'auto-guérison : si l'application est bloquée dans un état défaillant dont elle ne peut pas se sortir seule (deadlock, mémoire saturée), Kubernetes la redémarre pour rétablir le service.

**Pourquoi `initialDelaySeconds` de la livenessProbe est-il plus grand que celui de la readinessProbe ?**

La readinessProbe peut commencer à vérifier tôt — si elle échoue, le pod ne reçoit simplement pas de trafic, sans conséquence grave. La livenessProbe doit attendre que l'application ait eu le temps de démarrer complètement. Si elle démarre trop tôt et que l'app n'a pas encore fini son initialisation, Kubernetes la redémarrerait en boucle inutilement (CrashLoopBackOff). Un `initialDelaySeconds` plus grand sur la liveness garantit que le pod n'est pas tué avant d'avoir eu la chance de démarrer.

---

## Exercice 2 : RollingUpdate

### Objectif

Ajouter un endpoint `/ensai` à l'application et déployer cette mise à jour sans interruption de service via le mécanisme de RollingUpdate.

### Étape 1 : Ajouter l'endpoint `/ensai` et builder en v3

Le fichier `main.py` a été modifié :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return "world"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ensai")
def ensai():
    return {"message": "Bienvenue à l'ENSAI !"}
```

Build et push de la v3 :

```bash
docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v3 --push .
```

### Étape 2 : Manifest avec stratégie RollingUpdate explicite

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helloworld-app
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  selector:
    matchLabels:
      app: helloworld
  template:
    metadata:
      labels:
        app: helloworld
    spec:
      containers:
      - name: helloworld-container
        image: moonshayne/tp1-exo1:v3
        imagePullPolicy: Always
        ports:
        - containerPort: 8081
        readinessProbe:
          httpGet:
            path: /health
            port: 8081
          initialDelaySeconds: 5
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /health
            port: 8081
          initialDelaySeconds: 10
          periodSeconds: 10
```

`maxUnavailable: 1` signifie qu'au maximum 1 pod peut être indisponible pendant la mise à jour. `maxSurge: 1` autorise la création d'1 pod supplémentaire temporaire — on peut donc avoir jusqu'à 4 pods pendant la transition.

### Étape 3 : Déploiement et observation du RollingUpdate

```bash
kubectl apply -f app.yaml

# Observer le rollout en direct
kubectl rollout status deployment helloworld-app
# Waiting for deployment "helloworld-app" rollout to finish: 1 out of 3 new replicas...
# Waiting for deployment "helloworld-app" rollout to finish: 2 out of 3 new replicas...
# deployment "helloworld-app" successfully rolled out

# Consulter l'historique des révisions
kubectl rollout history deployment helloworld-app
# REVISION  CHANGE-CAUSE
# 1         <none>   (v1 initiale)
# 2         <none>   (v2 avec /health)
# 3         <none>   (v3 avec /ensai)
```

### Étape 4 : Rollback

```bash
# Revenir à la version précédente (v2)
kubectl rollout undo deployment helloworld-app

# Vérifier que les pods ont été mis à jour
kubectl get pods

# Rollback vers une version spécifique (v1)
kubectl rollout undo deployment helloworld-app --to-revision=1

# Historique après rollback
kubectl rollout history deployment helloworld-app
# REVISION  CHANGE-CAUSE
# 2         <none>
# 3         <none>
# 4         <none>   (rollback = nouvelle révision)
```

> Un rollback crée une **nouvelle révision** dans l'historique — il ne supprime pas les révisions précédentes. Chaque `kubectl rollout undo` incrémente le numéro de révision.

---

## Difficultés rencontrées

**Aucune difficulté majeure sur ce TP** — les concepts de probes et de RollingUpdate sont bien pris en charge nativement par Kubernetes et ne nécessitent que des ajouts dans le manifest existant.

Le point d'attention principal est le choix du port dans les probes : il doit correspondre exactement au port sur lequel l'application écoute (`containerPort`), ici 8081 pour uvicorn.

---

## Résumé des commandes `kubectl rollout`

| Commande | Description |
|---|---|
| `kubectl rollout status deployment <nom>` | Suivre l'avancement d'un déploiement en cours |
| `kubectl rollout history deployment <nom>` | Lister toutes les révisions |
| `kubectl rollout undo deployment <nom>` | Revenir à la révision précédente |
| `kubectl rollout undo deployment <nom> --to-revision=N` | Revenir à une révision spécifique |
| `kubectl rollout pause deployment <nom>` | Mettre en pause un rollout en cours |
| `kubectl rollout resume deployment <nom>` | Reprendre un rollout mis en pause |