# TP 5 Mettons a jour nos applications

## Objectifs du TP
- Comprendre et mettre en place une strategie de RollingUpdate
- Configurer des readiness et liveness probes
- Observer le comportement d'une mise a jour progressive
- Effectuer un rollback

Livrable :
- Manifests Kubernetes mis a jour
- Un compte rendu avec les difficultes rencontrees, et les resultats de chaque exercice.

## Prerequis

- Avoir un compte SSPCloud
- Avoir deploye l'application du TP2 (API Python) avec son Service et son Ingress (TP3)

## Exercice 1 : Ajout des probes

Notre application Python expose une route `/hello`. Cependant, elle ne dispose d'aucune route dediee au health check. Nous allons y remedier.

### Etape 1 : Ajouter un endpoint de health check

Modifiez votre application Python pour ajouter une route `/health` qui retourne un status 200 :

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Construisez une nouvelle image Docker avec ce changement et poussez-la sur Docker Hub avec un tag **v2** (en conservant votre image precedente en **v1**).

### Etape 2 : Configurer les probes dans le Deployment

Mettez a jour votre manifest de Deployment pour ajouter les probes suivantes :

- Une **readinessProbe** qui verifie la route `/health` sur le port 8000
  - `initialDelaySeconds: 5`
  - `periodSeconds: 5`

- Une **livenessProbe** qui verifie la route `/health` sur le port 8000
  - `initialDelaySeconds: 10`
  - `periodSeconds: 10`

Appliquez votre manifest et verifiez que les probes fonctionnent correctement.


### Etape 3 : Observer le comportement des probes

Repondez aux questions suivantes dans votre compte rendu :
- Que se passe-t-il si la readiness probe echoue ?
- Que se passe-t-il si la liveness probe echoue ?
- Pourquoi le `initialDelaySeconds` de la liveness probe est-il plus grand que celui de la readiness probe ?

## Exercice 2 : RollingUpdate

L'objectif de cet exercice est de comprendre et utiliser le mécanisme de RollingUpdate. 

Vous devrez donc : 
- Mettre en place ce mécanisme afin d'ajouter un endpoint "ensai"
- Tester les différentes commandes autour de la mise à jour (`kubectl rollout`)

