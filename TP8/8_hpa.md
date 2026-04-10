# TP 8 Autoscaling avec le Horizontal Pod Autoscaler

## Objectifs du TP

- Définir des resources requests et limits sur vos conteneurs
- Configurer des liveness et readiness probes
- Mettre en place un Horizontal Pod Autoscaler (HPA) basé sur la métrique CPU
- Observer le comportement de l'autoscaling en conditions de charge

Livrables :
- Votre fichier `deployment.yaml` complet (avec resources, probes, strategy)
- Votre fichier `hpa.yaml`
- Un compte rendu avec les difficultés rencontrées, les réponses aux questions et des captures d'écran montrant le scale-up et le scale-down du HPA

## Prérequis

- Avoir un compte SSPCloud
- Avoir déployé l'application du TP 7 (chart Helm avec backend et PostgreSQL)

## Exercice: HPA (Horizontal Pod Autoscaler)


### Pré requis : Mise en place de request / limits  

Kubernetes permet de définir les ressources CPU et mémoire que chaque conteneur peut utiliser. C'est indispensable pour que le HPA puisse calculer l'utilisation CPU en pourcentage.

| Champ | Description | Impact |
|-------|-------------|--------|
| `requests` | Ressources garanties au conteneur | Utilisé par le scheduler pour placer le pod |
| `limits` | Maximum autorisé | Le conteneur est throttlé (CPU) ou tué (mémoire) au-delà |

Sans `resources.requests.cpu`, le HPA affichera `<unknown>` et ne pourra pas fonctionner.

L'unité CPU : `100m` = 0.1 CPU (10% d'un cœur). L'unité mémoire : `Mi` = mégaoctets.

Modifiez votre Deployment existant pour ajouter le bloc `resources` dans la spec du conteneur :

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi
```

Appliquez la modification et vérifiez que les resources sont bien prises en compte

**Principe** : Le HPA ajuste automatiquement le nombre de replicas en fonction de l'utilisation des ressources.

### Etape 1 : Vérifier le metrics-server

Le HPA a besoin du metrics-server pour lire les métriques CPU des pods. Sur SSPCloud, il est déjà installé. Vérifiez qu'il fonctionne :

```bash
kubectl top pods
```

### Etape 2 : Créer le HPA

Créez un fichier `hpa.yaml` avec le contenu suivant :

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: <nom>-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: <nom-deployment>
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

```bash
kubectl apply -f hpa.yaml
kubectl get hpa
```

Si le HPA affiche `cpu: <unknown>/70%`, c'est que les `resources.requests.cpu` ne sont pas définies dans le Deployment.

### Etape 3 : Générer de la charge

Lancez un pod qui va envoyer des requêtes en continu à votre API :

```bash
kubectl run load-generator --image=busybox --restart=Never -- \
  /bin/sh -c "while true; do wget -q -O- http://<nom-service>:8000/; done"
```

### Etape 4 : Observer le scaling

Dans un premier terminal, surveillez le HPA :

```bash
kubectl get hpa --watch
```

Dans un second terminal, surveillez les pods :

```bash
kubectl get pods --watch
```

Vous devriez observer le CPU monter progressivement et le nombre de replicas augmenter.

### Etape 5 : Observer le scale-down

Supprimez le générateur de charge :

```bash
kubectl delete pod load-generator
```

Continuez à surveiller le HPA. Après environ 5 minutes de stabilisation, Kubernetes va progressivement réduire le nombre de pods pour revenir à 3 replicas.


