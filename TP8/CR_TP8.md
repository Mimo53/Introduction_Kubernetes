Pour ce TP, 


Les resources sont déjà définies dans le `values.yaml` du chart Helm du TP7 :

```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "125m"
  limits:
    memory: "128Mi"
    cpu: "125m"
```

Sans `resources.requests.cpu`, le HPA afficherait `<unknown>` et ne pourrait pas calculer l'utilisation CPU en pourcentage.


```bash
kubectl top pods
```

Sur SSPCloud, le metrics-server est déjà installé et fonctionnel.


Mon code `hpa.yaml` a pour code :

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ma-release-backend-app-backend
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

On applique le HPA et on vérifie :

```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP8$ kubectl apply -f hpa.yaml
horizontalpodautoscaler.autoscaling/backend-hpa created
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP8$ kubectl get hpa
NAME          REFERENCE                                   TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
backend-hpa   Deployment/ma-release-backend-app-backend   cpu: <unknown>/70%   3         10        0          10s
```



On lance un pod qui envoie des requêtes en continu vers le backend :

```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP8$ kubectl run load-generator --image=busybox --restart=Never -- \
  /bin/sh -c "while true; do wget -q -O- http://ma-release-backend-app-backend:5000/; done"
pod/load-generator created
```



```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP8$ kubectl get hpa --watch
NAME          REFERENCE                                   TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
backend-hpa   Deployment/ma-release-backend-app-backend   cpu: <unknown>/70%   3         10        3          37s
backend-hpa   Deployment/ma-release-backend-app-backend   cpu: <unknown>/70%   3         10        3          75s
backend-hpa   Deployment/ma-release-backend-app-backend   cpu: <unknown>/70%   3         10        3          90s
```



```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP8$ kubectl get pods --watch
NAME                                              READY   STATUS    RESTARTS   AGE
load-generator                                    1/1     Running   0          40s
ma-release-backend-app-backend-78c8d8c64b-64ltw   1/1     Running   1          2m36s
ma-release-backend-app-backend-78c8d8c64b-85xlv   1/1     Running   1          2m36s
ma-release-backend-app-backend-78c8d8c64b-lqm9k   1/1     Running   1          2m36s
ma-release-postgresql-1                           1/1     Running   0          2m22s
```


```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP8$ kubectl delete pod load-generator
pod "load-generator" deleted from user-mohamederrafii namespace
```

Après suppression du générateur, Kubernetes attend environ 5 minutes de stabilisation avant de réduire progressivement le nombre de replicas pour revenir à `minReplicas: 3`.

---

## Difficultés rencontrées

La principale difficulté de ce TP était que le HPA affichait `cpu: <unknown>/70%` au lieu d'une valeur numérique. Cela signifie que le HPA ne pouvait pas lire les métriques CPU des pods, ce qui empêchait le scale-up automatique. Deux causes possibles ont été identifiées : soit les `resources.requests.cpu` n'étaient pas définies dans le Deployment (elles l'étaient dans notre cas via le `values.yaml` Helm), soit les pods venaient de démarrer et le metrics-server n'avait pas encore collecté de données.

En conséquence, le scale-up n'a pas pu être observé visuellement pendant la session — le nombre de replicas est resté à 3 (le minimum) malgré la charge générée. Le scale-down a bien été observé après suppression du `load-generator`, avec le pod qui est passé en `Terminating` puis `Error` avant d'être supprimé.

Cette limitation est liée au fait que les images Flask du backend ne sont pas CPU-intensives — elles répondent très rapidement aux requêtes `wget`, ce qui ne génère pas suffisamment de charge CPU pour dépasser le seuil de 70% et déclencher le scale-up.
