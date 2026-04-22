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




Introduction_Kubernetes git:(main) ✗ # Créer la structure dans TP5
mkdir -p TP5/python-api/src

# Copier les fichiers existants
cp TP1/Exo1/Dockerfile TP5/
cp TP1/Exo1/python-api/requirements.txt TP5/python-api/
cp TP1/Exo1/pytho                                    
➜  Introduction_Kubernetes git:(main) ✗ mkdir -p TP5/python-api/src
➜  Introduction_Kubernetes git:(main) ✗ cp TP1/Exo1/Dockerfile TP5/
➜  Introduction_Kubernetes git:(main) ✗ cp TP1/Exo1/python-api/requirements.txt TP5/python-api/
➜  Introduction_Kubernetes git:(main) ✗ cp TP1/Exo1/python-api/src/main.py TP5/python-api/src/
➜  Introduction_Kubernetes git:(main) ✗ docker tag moonshayne/tp1-exo1:latest moonshayne/tp1-exo1:v1
failed to connect to the docker API at unix:///Users/zaslaoui/.docker/run/docker.sock; check if the path is correct and if the daemon is running: dial unix /Users/zaslaoui/.docker/run/docker.sock: connect: no such file or directory
➜  Introduction_Kubernetes git:(main) ✗ docker images
                                                                                                                                      i Info →   U  In Use
IMAGE                          ID             DISK USAGE   CONTENT SIZE   EXTRA
hugosmn5/backend-3-tier:1.1    e54cf6710233        143MB             0B    U   
hugosmn5/frontend-3-tier:1.1   643c514b150d        133MB             0B    U   
➜  Introduction_Kubernetes git:(main) ✗ cd TP1 
➜  TP1 git:(main) ✗ cd Exo1 
➜  Exo1 git:(main) ✗ docker build -t tp1-exo1
ERROR: docker: 'docker buildx build' requires 1 argument

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Run 'docker buildx build --help' for more information
➜  Exo1 git:(main) ✗  docker build -t tp1-exo1 .
[+] Building 928.9s (10/10) FINISHED                                                                                                 docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                 0.0s
 => => transferring dockerfile: 876B                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                  3.0s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                    0.0s
 => => transferring context: 2B                                                                                                                      0.0s
 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:40365323acc4621904ca8d85aaf1a32da1ae2b93ecf98bbefe956601d1b57f11                          836.8s
 => => resolve docker.io/library/python:3.13-slim@sha256:40365323acc4621904ca8d85aaf1a32da1ae2b93ecf98bbefe956601d1b57f11                            0.0s
 => => sha256:0a694b1ee6d409418f680b3fb2c44bd3177740ba87b55e9b13bbf544962475de 5.52kB / 5.52kB                                                       0.0s
 => => sha256:e4fb5f1cd4d4ee56da574ef5ed88a5c74f100ba98caacf6c5ef26cee66525179 30.14MB / 30.14MB                                                   835.3s
 => => sha256:77147f59c0641698b2116ad59ac51b9f80aa3606c3440e2a02833b3df966383f 1.27MB / 1.27MB                                                      64.2s
 => => sha256:85ca06eb999e8052f7ab3c5287687e23c305af5ad0853bb3077bc150bc6aebd5 11.75MB / 11.75MB                                                   288.3s
 => => sha256:40365323acc4621904ca8d85aaf1a32da1ae2b93ecf98bbefe956601d1b57f11 10.37kB / 10.37kB                                                     0.0s
 => => sha256:8922791069fdfdd6056cf7f418a8655d970862d1972570d4c0e78dfc43afacd6 1.75kB / 1.75kB                                                       0.0s
 => => sha256:d066deb7ef19cbd348c908bb61bcf4a99a51cb31944437929250556989ad1ae4 249B / 249B                                                          65.3s
 => => extracting sha256:e4fb5f1cd4d4ee56da574ef5ed88a5c74f100ba98caacf6c5ef26cee66525179                                                            0.8s
 => => extracting sha256:77147f59c0641698b2116ad59ac51b9f80aa3606c3440e2a02833b3df966383f                                                            0.1s
 => => extracting sha256:85ca06eb999e8052f7ab3c5287687e23c305af5ad0853bb3077bc150bc6aebd5                                                            0.4s
 => => extracting sha256:d066deb7ef19cbd348c908bb61bcf4a99a51cb31944437929250556989ad1ae4                                                            0.0s
 => [internal] load build context                                                                                                                    0.0s
 => => transferring context: 11.74kB                                                                                                                 0.0s
 => [2/4] WORKDIR /app                                                                                                                               0.3s
 => [3/4] COPY . .                                                                                                                                   0.0s
 => [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                             88.7s
 => exporting to image                                                                                                                               0.1s
 => => exporting layers                                                                                                                              0.1s
 => => writing image sha256:6726aa926595600ab8cb149e3b3e849b8a594e0d2d960648630a307032018d86                                                         0.0s
 => => naming to docker.io/library/tp1-exo1                                                                                                          0.0s
➜  Exo1 git:(main) ✗ docker tag tp1-exo1 moonshayne/tp1-exo1
➜  Exo1 git:(main) ✗ docker push moonshayne/tp1-exo1
Using default tag: latest
The push refers to repository [docker.io/moonshayne/tp1-exo1]
2a56cf72d73e: Pushed 
209ebc1aa2e0: Pushed 
5571bbfc6368: Pushed 
230fbf0938fe: Mounted from library/python 
b6ad78d5ecf6: Pushed 
3f3265674e7f: Mounted from library/python 
e6133723babd: Mounted from library/python 
latest: digest: sha256:8d9502de1c1b6c11bcd0faa7594f965d0b389c3b0fda1d21241e5a685abd606a size: 1784
➜  Exo1 git:(main) ✗ cd ..
➜  TP1 git:(main) ✗ cd ..
➜  Introduction_Kubernetes git:(main) ✗ cd TP5 
➜  TP5 git:(main) ✗ docker tag moonshayne/tp1-exo1:latest moonshayne/tp1-exo1:v1
➜  TP5 git:(main) ✗ docker push moonshayne/tp1-exo1:v1
The push refers to repository [docker.io/moonshayne/tp1-exo1]
2a56cf72d73e: Layer already exists 
209ebc1aa2e0: Layer already exists 
5571bbfc6368: Layer already exists 
230fbf0938fe: Layer already exists 
b6ad78d5ecf6: Layer already exists 
3f3265674e7f: Layer already exists 
e6133723babd: Layer already exists 
v1: digest: sha256:8d9502de1c1b6c11bcd0faa7594f965d0b389c3b0fda1d21241e5a685abd606a size: 1784
➜  TP5 git:(main) ✗ docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v2 --push .
[+] Building 1170.9s (13/13) FINISHED                                                                                 docker-container:romantic_blackwell
 => [internal] booting buildkit                                                                                                                    354.6s
 => => pulling image moby/buildkit:buildx-stable-1                                                                                                 353.8s
 => => creating container buildx_buildkit_romantic_blackwell0                                                                                        0.8s
 => [internal] load build definition from Dockerfile                                                                                                 0.0s
 => => transferring dockerfile: 876B                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                  2.8s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                    0.0s
 => => transferring context: 2B                                                                                                                      0.0s
 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:bada92bcc2794014c291cd97ac3604eb907746b9d3f4b4ff5a8a1ffeff40ceff                           70.1s
 => => resolve docker.io/library/python:3.13-slim@sha256:bada92bcc2794014c291cd97ac3604eb907746b9d3f4b4ff5a8a1ffeff40ceff                            0.0s
 => => sha256:a51d847b5d4902dac7726e34078eeb8e64ee8047b67ea02877acabcef191b07f 11.82MB / 11.82MB                                                    37.1s
 => => sha256:3f977313cbf20d1fcbf9d25f28735d97b7bc691319bc43f8c539c8d05c9cf886 1.29MB / 1.29MB                                                       4.7s
 => => sha256:eb7aeb6e31180144e93bad8e32441038f4c4520ec825039827c05fadcc01305f 249B / 249B                                                           0.4s
 => => sha256:3531af2bc2a9c8883754652783cf96207d53189db279c9637b7157d034de7ecd 29.78MB / 29.78MB                                                    69.3s
 => => extracting sha256:3531af2bc2a9c8883754652783cf96207d53189db279c9637b7157d034de7ecd                                                            0.4s
 => => extracting sha256:3f977313cbf20d1fcbf9d25f28735d97b7bc691319bc43f8c539c8d05c9cf886                                                            0.0s
 => => extracting sha256:a51d847b5d4902dac7726e34078eeb8e64ee8047b67ea02877acabcef191b07f                                                            0.2s
 => => extracting sha256:eb7aeb6e31180144e93bad8e32441038f4c4520ec825039827c05fadcc01305f                                                            0.0s
 => [internal] load build context                                                                                                                    0.0s
 => => transferring context: 13.30kB                                                                                                                 0.0s
 => [2/4] WORKDIR /app                                                                                                                               0.2s
 => [3/4] COPY . .                                                                                                                                   0.0s
 => [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                              9.5s
 => ERROR exporting to image                                                                                                                       745.0s
 => => exporting layers                                                                                                                              0.6s
 => => exporting manifest sha256:b64861ccca65429cadc0b98525467a751f934f95707d2636c32c13ba032f5f90                                                    0.0s
 => => exporting config sha256:45fbab30c3ce24985517c97b9851154ed31bdaffb1ce0233c9b8040775f93054                                                      0.0s
 => => exporting attestation manifest sha256:2c79fbb4bb97988184ec26c7c3044d6a2b6e483c876eb800503dcf6aa75a2ef2                                        0.0s
 => => exporting manifest list sha256:99ca2bfd20315df1a271df9a6472f6c5fb696c37117bedcd8df6a3cc08490156                                               0.0s
 => => pushing layers                                                                                                                              744.4s
 => [auth] moonshayne/tp1-exo1:pull,push token for registry-1.docker.io                                                                              0.0s
 => [auth] moonshayne/tp1-exo1:pull,push token for registry-1.docker.io                                                                              0.0s
------
 > exporting to image:
240.4 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/bbb883ec-6258-42f2-855d-5aa1e4cba19f?_state=rVHXsFJbtthMm8_6TCKFfhG3la_BWcll7-YAzk0lS_97Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6ImJiYjg4M2VjLTYyNTgtNDJmMi04NTVkLTVhYTFlNGNiYTE5ZiIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1MToyNC4zNDQ2NDc1ODVaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyMToyNC40MTAzMzE2MjFaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9kNHc3VEJveHNIc1RWanZGS2NvTXV0cGhhSkU9In0%3D&digest=sha256%3Ad2925c6e599c033f6cee96ae6e0322d51620bf50a75fed15a8d7972571f82670": write tcp 172.17.0.2:51270->100.27.240.114:443: write: broken pipe
240.4 retrying in 1s
241.3 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/04b99527-c791-4d79-bc08-cb557c215de5?_state=YMWLgV_PMidvzFOxfzQGiBRr81FWd7ndYCISCSK1SEt7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6IjA0Yjk5NTI3LWM3OTEtNGQ3OS1iYzA4LWNiNTU3YzIxNWRlNSIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1MToyNC4yODEwODM5ODdaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyMToyNC4zNzM5OTU3MzNaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9kNHc3VEJveHNIc1RWanZGS2NvTXV0cGhhSkU9In0%3D&digest=sha256%3A3531af2bc2a9c8883754652783cf96207d53189db279c9637b7157d034de7ecd": write tcp 172.17.0.2:51260->100.27.240.114:443: write: broken pipe
241.3 retrying in 1s
243.4 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/9c4966e7-9974-40a2-9d66-0c5c0c7f7099?_state=g_qmw6uKqiDeVCkXUBzDiSrVaNh1fpWyucGjCAs6wh57Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6IjljNDk2NmU3LTk5NzQtNDBhMi05ZDY2LTBjNWMwYzdmNzA5OSIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1MToyNy41MzkzNDA5MDlaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyMToyNy42NTQxODI1MThaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9kNHc3VEJveHNIc1RWanZGS2NvTXV0cGhhSkU9In0%3D&digest=sha256%3Aa51d847b5d4902dac7726e34078eeb8e64ee8047b67ea02877acabcef191b07f": write tcp 172.17.0.2:51226->100.27.240.114:443: write: broken pipe
243.4 retrying in 1s
394.1 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/24c10c8f-f5cd-4c11-ad2c-aa4aa0d59643?_state=oUvSVGaOId72n9RtTzsbakNJpJ4fTa8tn66N6CKjlwV7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6IjI0YzEwYzhmLWY1Y2QtNGMxMS1hZDJjLWFhNGFhMGQ1OTY0MyIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1NToyNi4zMDE1NzIyODJaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyNToyNi40MTQ3ODMzMjNaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9kNHc3VEJveHNIc1RWanZGS2NvTXV0cGhhSkU9In0%3D&digest=sha256%3Ad2925c6e599c033f6cee96ae6e0322d51620bf50a75fed15a8d7972571f82670": write tcp 172.17.0.2:51500->50.19.60.231:443: write: broken pipe
394.1 retrying in 2s
395.9 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/fd712a07-487c-474e-b832-65a49b9d385b?_state=Odj0IN80IOZuar1sm2oF2gCicbxmNI5i4_GcvIwJ-0l7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6ImZkNzEyYTA3LTQ4N2MtNDc0ZS1iODMyLTY1YTQ5YjlkMzg1YiIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1NToyNi41MzMzMzgzMjNaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyNToyNi42MzEwNTE1NzZaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9kNHc3VEJveHNIc1RWanZGS2NvTXV0cGhhSkU9In0%3D&digest=sha256%3A3531af2bc2a9c8883754652783cf96207d53189db279c9637b7157d034de7ecd": write tcp 172.17.0.2:51512->50.19.60.231:443: write: broken pipe
395.9 retrying in 2s
396.3 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/10e7b50e-7fe4-46d1-9158-bf11b28eca66?_state=T1rXkg7Nm3adEW4P58rRh6HYdKf0cYrC5RCIQ-UHbTl7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6IjEwZTdiNTBlLTdmZTQtNDZkMS05MTU4LWJmMTFiMjhlY2E2NiIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1NTozMS4zODM1MTMyNzRaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyNTozMS40ODk5OTUzNTVaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9kNHc3VEJveHNIc1RWanZGS2NvTXV0cGhhSkU9In0%3D&digest=sha256%3Aa51d847b5d4902dac7726e34078eeb8e64ee8047b67ea02877acabcef191b07f": write tcp 172.17.0.2:51526->50.19.60.231:443: write: broken pipe
396.3 retrying in 2s
441.0 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/7cbb78b2-2690-475c-8ba1-6544c9a68149?_state=X8afd8rPgTJQroilTnmsnz6T4ZmAayWw6J-M_H2rbop7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6IjdjYmI3OGIyLTI2OTAtNDc1Yy04YmExLTY1NDRjOWE2ODE0OSIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1ODowMC4yNzM1MTE4MjdaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyODowMC40MDIwNDQyODdaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9yOER6U05EZDNhTEZNVXoyR3RVZU5FTU1LQTA9In0%3D&digest=sha256%3Ad2925c6e599c033f6cee96ae6e0322d51620bf50a75fed15a8d7972571f82670": write tcp 172.17.0.2:55302->13.217.73.111:443: write: broken pipe
441.0 retrying in 4s
442.8 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/e39f3ae0-d9cb-43dd-8ee3-6bded9dc4e69?_state=uMfsC9TZTFAj_60SxGP7ISKCO69R_z0rLWLproQ8Fa57Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6ImUzOWYzYWUwLWQ5Y2ItNDNkZC04ZWUzLTZiZGVkOWRjNGU2OSIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1ODowMy42OTAxOTUxODJaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyODowMy43ODEwMzUzMjNaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9yOER6U05EZDNhTEZNVXoyR3RVZU5FTU1LQTA9In0%3D&digest=sha256%3A3531af2bc2a9c8883754652783cf96207d53189db279c9637b7157d034de7ecd": write tcp 172.17.0.2:36848->13.217.73.111:443: write: broken pipe
442.8 retrying in 4s
445.2 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/b02501e6-f79c-4430-a3cb-9fe05c54cc37?_state=gwO9co7Cim8ZJZKX4JhRlhVp7UFzLhU5XL3BcCAag9p7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6ImIwMjUwMWU2LWY3OWMtNDQzMC1hM2NiLTlmZTA1YzU0Y2MzNyIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1ODowMy45MzA4MzA0NjRaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyODowMy45OTgwNTMxOVoiLCJVc2VybmFtZSI6Im1vb25zaGF5bmUiLCJVc2VyVVVJRCI6IjdiMTljYWJhLTUxNGMtNGY2Ni1iZjEwLWU3YmQ1MDY2MWY1OCIsIlNlc3Npb25JRCI6ImRja3JfanRpX3I4RHpTTkRkM2FMRk1VejJHdFVlTkVNTUtBMD0ifQ%3D%3D&digest=sha256%3Aa51d847b5d4902dac7726e34078eeb8e64ee8047b67ea02877acabcef191b07f": write tcp 172.17.0.2:36854->13.217.73.111:443: write: broken pipe
445.2 retrying in 4s
744.4 error: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/fec0d06f-0ab7-424b-87e4-65750cf9f672?_state=s-UsAIXpmgaZt2I7ES4Apy7A4pX72f2JxorrorXnh9p7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6ImZlYzBkMDZmLTBhYjctNDI0Yi04N2U0LTY1NzUwY2Y5ZjY3MiIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1ODo0OC44MTM4MjQ0MDJaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyODo0OC45MDUxMTk3MjNaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9yOER6U05EZDNhTEZNVXoyR3RVZU5FTU1LQTA9In0%3D&digest=sha256%3Ad2925c6e599c033f6cee96ae6e0322d51620bf50a75fed15a8d7972571f82670": write tcp 172.17.0.2:60290->100.27.240.114:443: write: broken pipe
------
ERROR: failed to build: failed to solve: failed to push moonshayne/tp1-exo1:v2: failed to copy: failed to do request: Put "https://registry-1.docker.io/v2/moonshayne/tp1-exo1/blobs/uploads/fec0d06f-0ab7-424b-87e4-65750cf9f672?_state=s-UsAIXpmgaZt2I7ES4Apy7A4pX72f2JxorrorXnh9p7Ik5hbWUiOiJtb29uc2hheW5lL3RwMS1leG8xIiwiVVVJRCI6ImZlYzBkMDZmLTBhYjctNDI0Yi04N2U0LTY1NzUwY2Y5ZjY3MiIsIk9mZnNldCI6MCwiU3RhcnRlZEF0IjoiMjAyNi0wNC0yMlQwODo1ODo0OC44MTM4MjQ0MDJaIiwiRXhwaXJlc0F0IjoiMjAyNi0wNC0yMlQwOToyODo0OC45MDUxMTk3MjNaIiwiVXNlcm5hbWUiOiJtb29uc2hheW5lIiwiVXNlclVVSUQiOiI3YjE5Y2FiYS01MTRjLTRmNjYtYmYxMC1lN2JkNTA2NjFmNTgiLCJTZXNzaW9uSUQiOiJkY2tyX2p0aV9yOER6U05EZDNhTEZNVXoyR3RVZU5FTU1LQTA9In0%3D&digest=sha256%3Ad2925c6e599c033f6cee96ae6e0322d51620bf50a75fed15a8d7972571f82670": write tcp 172.17.0.2:60290->100.27.240.114:443: write: broken pipe
➜  TP5 git:(main) ✗ docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v2 --push .
[+] Building 162.6s (11/11) FINISHED                                                                                  docker-container:romantic_blackwell
 => [internal] load build definition from Dockerfile                                                                                                 0.0s
 => => transferring dockerfile: 876B                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                  1.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                    0.0s
 => => transferring context: 2B                                                                                                                      0.0s
 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:bada92bcc2794014c291cd97ac3604eb907746b9d3f4b4ff5a8a1ffeff40ceff                            0.0s
 => => resolve docker.io/library/python:3.13-slim@sha256:bada92bcc2794014c291cd97ac3604eb907746b9d3f4b4ff5a8a1ffeff40ceff                            0.0s
 => [internal] load build context                                                                                                                    0.0s
 => => transferring context: 289B                                                                                                                    0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                        0.0s
 => CACHED [3/4] COPY . .                                                                                                                            0.0s
 => CACHED [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                       0.0s
 => exporting to image                                                                                                                             161.0s
 => => exporting layers                                                                                                                              0.0s
 => => exporting manifest sha256:b64861ccca65429cadc0b98525467a751f934f95707d2636c32c13ba032f5f90                                                    0.0s
 => => exporting config sha256:45fbab30c3ce24985517c97b9851154ed31bdaffb1ce0233c9b8040775f93054                                                      0.0s
 => => exporting attestation manifest sha256:5095b3a8f717ad1351aa5b9ce553f6828f20820b9772f217a9ba5c9ea4321457                                        0.0s
 => => exporting manifest list sha256:6ffb09b51aced0a462d7dfcd9f5798ad4ef16a6deafa66079cc4d2bc90f522d6                                               0.0s
 => => pushing layers                                                                                                                              156.8s
 => => pushing manifest for docker.io/moonshayne/tp1-exo1:v2@sha256:6ffb09b51aced0a462d7dfcd9f5798ad4ef16a6deafa66079cc4d2bc90f522d6                 4.2s
 => [auth] moonshayne/tp1-exo1:pull,push token for registry-1.docker.io                                                                              0.0s
➜  TP5 git:(main) ✗ cd ..
➜  Introduction_Kubernetes git:(main) ✗ cd ..
➜  ~ git:(master) ✗ cd Introduction_Kubernetes 
➜  Introduction_Kubernetes git:(main) ✗ tree
.
├── TP1
│   ├── 1_docker.md
│   ├── Exo1
│   │   ├── CR_TP1_exo1.md
│   │   ├── Dockerfile
│   │   └── python-api
│   │       ├── requirements.txt
│   │       └── src
│   │           └── main.py
│   └── Exo2
│       ├── CR_TP1_exo2.md
│       ├── Dockerfile
│       └── java-api
│           ├── pom.xml
│           ├── src
│           │   └── main
│           │       └── java
│           │           └── com
│           │               └── example
│           │                   ├── Application.java
│           │                   └── HelloController.java
│           └── target
│               ├── classes
│               │   └── com
│               │       └── example
│               │           ├── Application.class
│               │           └── HelloController.class
│               └── test-classes
├── TP2
│   ├── 2_premiers_pas_kube.md
│   ├── CR_TP2.md
│   └── app.yaml
├── TP3
│   ├── 1.Expo_Cluster
│   │   ├── CR.md
│   │   └── app.yaml
│   ├── 2.Expo_Internet
│   │   └── app.yaml
│   ├── 3.Expo_3_tiers
│   │   ├── CR.md
│   │   ├── backend.yaml
│   │   ├── frontend.yaml
│   │   └── postgres.yaml
│   ├── 3_exposition_application.md
│   └── CR_TP3.md
├── TP4
│   ├── 4_gestion_de_la_persistance.md
│   ├── CR.md
│   ├── CR_TP4.md
│   └── postgres-statefulset.yaml
├── TP5
│   ├── 5_mise_a_jour_application.md
│   ├── CR_TP5.md
│   ├── Dockerfile
│   ├── app.yaml
│   └── python-api
│       ├── requirements.txt
│       └── src
│           └── main.py
├── TP6
│   ├── 6_amélioration_application.md
│   ├── CR_TP6.md
│   ├── backend.yaml
│   ├── frontend.yaml
│   ├── postgres.yaml
│   └── secret.yaml
├── TP7
│   ├── 7_helm.md
│   ├── CR_TP7.md
│   └── backend-app
│       ├── Chart.lock
│       ├── Chart.yaml
│       ├── charts
│       │   └── cluster-0.0.9.tgz
│       ├── templates
│       │   ├── NOTES.txt
│       │   ├── _helpers.tpl
│       │   ├── deployment.yaml
│       │   └── service.yaml
│       └── values.yaml
└── TP8
    ├── 8_hpa.md
    └── CR_TP8.md

32 directories, 52 files
➜  Introduction_Kubernetes git:(main) ✗ cd TP5 
➜  TP5 git:(main) ✗ docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v3 --push .
[+] Building 198.4s (11/11) FINISHED                                                                                                                                                      docker-container:romantic_blackwell
 => [internal] load build definition from Dockerfile                                                                                                                                                                     0.0s
 => => transferring dockerfile: 876B                                                                                                                                                                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                                                                                      1.7s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                                                        0.0s
 => => transferring context: 2B                                                                                                                                                                                          0.0s
 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:bada92bcc2794014c291cd97ac3604eb907746b9d3f4b4ff5a8a1ffeff40ceff                                                                                                0.0s
 => => resolve docker.io/library/python:3.13-slim@sha256:bada92bcc2794014c291cd97ac3604eb907746b9d3f4b4ff5a8a1ffeff40ceff                                                                                                0.0s
 => [internal] load build context                                                                                                                                                                                        0.0s
 => => transferring context: 699B                                                                                                                                                                                        0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                                                                            0.0s
 => [3/4] COPY . .                                                                                                                                                                                                       0.1s
 => [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                                                                                                 14.4s
 => exporting to image                                                                                                                                                                                                 182.1s 
 => => exporting layers                                                                                                                                                                                                  0.7s 
 => => exporting manifest sha256:eeb9000c8c740e9484c2ce068ff1e9ab00de072b9cab9fea7b99bd40ec42eeaa                                                                                                                        0.0s 
 => => exporting config sha256:c2af7e59802fab02e3bdc98f080e1248e0e73f3b03855ea83a49be2e9210cdff                                                                                                                          0.0s 
 => => exporting attestation manifest sha256:e41534f49298cb4ab965557bff2cb31feab860ec7cb4f4e1c8587a7884586923                                                                                                            0.0s 
 => => exporting manifest list sha256:e801482a7458799ee907c147038f6d2a828e965baaa95bea518eb01fe054a36c                                                                                                                   0.0s 
 => => pushing layers                                                                                                                                                                                                  177.7s
 => => pushing manifest for docker.io/moonshayne/tp1-exo1:v3@sha256:e801482a7458799ee907c147038f6d2a828e965baaa95bea518eb01fe054a36c                                                                                     3.6s
 => [auth] moonshayne/tp1-exo1:pull,push token for registry-1.docker.io                                                                                                                                                  0.0s
➜  TP5 git:(main) ✗ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../TP1/Exo1/CR_TP1_exo1.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../TP3/CR_TP3.md
        ../TP4/CR_TP4.md
        CR_TP5.md
        Dockerfile
        app.yaml
        python-api/
        ../TP6/CR_TP6.md
        ../TP7/CR_TP7.md
        ../TP8/CR_TP8.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  TP5 git:(main) ✗ cd ..
➜  Introduction_Kubernetes git:(main) ✗ git add .
➜  Introduction_Kubernetes git:(main) ✗ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   TP1/Exo1/CR_TP1_exo1.md
        new file:   TP3/CR_TP3.md
        new file:   TP4/CR_TP4.md
        new file:   TP5/CR_TP5.md
        new file:   TP5/Dockerfile
        new file:   TP5/app.yaml
        new file:   TP5/python-api/requirements.txt
        new file:   TP5/python-api/src/main.py
        new file:   TP6/CR_TP6.md
        new file:   TP7/CR_TP7.md
        new file:   TP8/CR_TP8.md

➜  Introduction_Kubernetes git:(main) ✗                                             