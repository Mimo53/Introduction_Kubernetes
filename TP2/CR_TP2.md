# TP2 
On reprends l'image docker que l'on a pushé lors de l'exercice 1 du TP1 et on va utiliser Kubernetes pour faire un deployment.
Pour l'utilisation de kubernetes j'ai arrété d'utiliser mon ordinateur personnelle (même si cela est possible notamment avec minikube) et j'ai travaillé sur un service Onyxia (VSCode-python)
Or les containeurs onyxia tourne sur linux est j'ai pushé mes images depuis mon mac donc j'ai du corriger ça en modifiant mon push avec la commande : 

```bash
# 1. Créer un builder multi-arch (une seule fois)
docker buildx create --use

# 2. Builder et pousser directement sur Docker Hub pour amd64
docker buildx build \
  --platform linux/amd64 \
  -t moonshayne/tp1-exo1:latest \
  --push \
  .
```

Pour que ce soit à la fois compatibles avec mon mac et linux. 

Une fois que j'ai eu les prérequis. 

## Structure du projet, fichier app.yaml et commande dans le terminal

Mon projet a pour structure :

```bash
➜  Introduction_Kubernetes git:(main) cd TP2 
➜  TP2 git:(main) tree
.
├── 2_premiers_pas_kube.md
├── CR.md
└── app.yaml

1 directory, 3 files
```
le fichier app.yaml est :

```YAML
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
        image: moonshayne/tp1-exo1:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 8081
---
```
et une fois placé dans le dossier TP2, les commandes à réaliser sont : 

```bash
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
deployment.apps/helloworld-app created
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods --selector=app=helloworld
NAME                              READY   STATUS             RESTARTS      AGE
helloworld-app-5b9599f4f7-67zzp        1/1     Running   0               6m40s
helloworld-app-5b9599f4f7-c7plk        1/1     Running   0               6m28s
helloworld-app-5b9599f4f7-jw828        1/1     Running   0               6m34s
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get deployment 
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
helloworld-app          3/3     3            3           17m
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs -f helloworld-app-5b9599f4f7-67zzp
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl port-forward pod/helloworld-app-5b9599f4f7-67zzp 8081:8081
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld-app-5b9599f4f7-67zzp
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
INFO:     192.168.1.136:0 - "GET / HTTP/1.1" 404 Not Found
INFO:     192.168.1.136:0 - "GET / HTTP/1.1" 404 Not Found
INFO:     192.168.1.136:0 - "GET /hello HTTP/1.1" 200 OK
INFO:     192.168.1.136:0 - "GET /hello HTTP/1.1" 200 OK
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl describe pods helloworld-app-5b9599f4f7-67zzp
Name:             helloworld-app-5b9599f4f7-67zzp
Namespace:        user-mohamederrafii
Priority:         0
Service Account:  default
Node:             boss7/192.168.253.167
Start Time:       Tue, 14 Apr 2026 09:34:58 +0000
Labels:           app=helloworld
                  pod-template-hash=5b9599f4f7
Annotations:      kubectl.kubernetes.io/restartedAt: 2026-04-14T09:34:58Z
Status:           Running
IP:               10.233.122.35
IPs:
  IP:           10.233.122.35
Controlled By:  ReplicaSet/helloworld-app-5b9599f4f7
Containers:
  helloworld-container:
    Container ID:   containerd://e958b200ba09e75b707a0dd4589a99bb1d32ea0bf0ec5e9acbeef8d5d8769503
    Image:          moonshayne/tp1-exo1:latest
    Image ID:       docker.io/moonshayne/tp1-exo1@sha256:54370a2d60a343e7d67caddefaf8873e3c84ef0c4c20a5fcb845eb2cef1b862d
    Port:           8081/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 14 Apr 2026 09:35:03 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-72rll (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-72rll:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  14m   default-scheduler  Successfully assigned user-mohamederrafii/helloworld-app-5b9599f4f7-67zzp to boss7
  Normal  Pulling    14m   kubelet            spec.containers{helloworld-container}: Pulling image "moonshayne/tp1-exo1:latest"
  Normal  Pulled     14m   kubelet            spec.containers{helloworld-container}: Successfully pulled image "moonshayne/tp1-exo1:latest" in 3.875s (3.875s including waiting). Image size: 54174068 bytes.
  Normal  Created    14m   kubelet            spec.containers{helloworld-container}: Created container: helloworld-container
  Normal  Started    14m   kubelet            spec.containers{helloworld-container}: Started container helloworld-container
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get all -l app=helloworld
NAME                                  READY   STATUS    RESTARTS   AGE
pod/helloworld-app-5b9599f4f7-67zzp   1/1     Running   0          19m
pod/helloworld-app-5b9599f4f7-c7plk   1/1     Running   0          19m
pod/helloworld-app-5b9599f4f7-jw828   1/1     Running   0          19m

NAME                                        DESIRED   CURRENT   READY   AGE
replicaset.apps/helloworld-app-56988bb556   0         0         0       30m
replicaset.apps/helloworld-app-5b9599f4f7   3         3         3       19m
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl describe deployment helloworld-app
kubectl describe service helloworld-service
kubectl describe pod helloworld-app-5b9599f4f7-67zzp
Name:                   helloworld-app
Namespace:              user-mohamederrafii
CreationTimestamp:      Tue, 14 Apr 2026 09:24:36 +0000
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 2
Selector:               app=helloworld
Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:       app=helloworld
  Annotations:  kubectl.kubernetes.io/restartedAt: 2026-04-14T09:34:58Z
  Containers:
   helloworld-container:
    Image:         moonshayne/tp1-exo1:latest
    Port:          8081/TCP
    Host Port:     0/TCP
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  helloworld-app-56988bb556 (0/0 replicas created)
NewReplicaSet:   helloworld-app-5b9599f4f7 (3/3 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  30m   deployment-controller  Scaled up replica set helloworld-app-56988bb556 from 0 to 3
  Normal  ScalingReplicaSet  20m   deployment-controller  Scaled up replica set helloworld-app-5b9599f4f7 from 0 to 1
  Normal  ScalingReplicaSet  20m   deployment-controller  Scaled down replica set helloworld-app-56988bb556 from 3 to 2
  Normal  ScalingReplicaSet  20m   deployment-controller  Scaled up replica set helloworld-app-5b9599f4f7 from 1 to 2
  Normal  ScalingReplicaSet  20m   deployment-controller  Scaled down replica set helloworld-app-56988bb556 from 2 to 1
  Normal  ScalingReplicaSet  20m   deployment-controller  Scaled up replica set helloworld-app-5b9599f4f7 from 2 to 3
  Normal  ScalingReplicaSet  20m   deployment-controller  Scaled down replica set helloworld-app-56988bb556 from 1 to 0
Error from server (NotFound): services "helloworld-service" not found
Name:             helloworld-app-5b9599f4f7-67zzp
Namespace:        user-mohamederrafii
Priority:         0
Service Account:  default
Node:             boss7/192.168.253.167
Start Time:       Tue, 14 Apr 2026 09:34:58 +0000
Labels:           app=helloworld
                  pod-template-hash=5b9599f4f7
Annotations:      kubectl.kubernetes.io/restartedAt: 2026-04-14T09:34:58Z
Status:           Running
IP:               10.233.122.35
IPs:
  IP:           10.233.122.35
Controlled By:  ReplicaSet/helloworld-app-5b9599f4f7
Containers:
  helloworld-container:
    Container ID:   containerd://e958b200ba09e75b707a0dd4589a99bb1d32ea0bf0ec5e9acbeef8d5d8769503
    Image:          moonshayne/tp1-exo1:latest
    Image ID:       docker.io/moonshayne/tp1-exo1@sha256:54370a2d60a343e7d67caddefaf8873e3c84ef0c4c20a5fcb845eb2cef1b862d
    Port:           8081/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 14 Apr 2026 09:35:03 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-72rll (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-72rll:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  20m   default-scheduler  Successfully assigned user-mohamederrafii/helloworld-app-5b9599f4f7-67zzp to boss7
  Normal  Pulling    20m   kubelet            spec.containers{helloworld-container}: Pulling image "moonshayne/tp1-exo1:latest"
  Normal  Pulled     20m   kubelet            spec.containers{helloworld-container}: Successfully pulled image "moonshayne/tp1-exo1:latest" in 3.875s (3.875s including waiting). Image size: 54174068 bytes.
  Normal  Created    20m   kubelet            spec.containers{helloworld-container}: Created container: helloworld-container
  Normal  Started    20m   kubelet            spec.containers{helloworld-container}: Started container helloworld-container
```


Difficultés rencontré : 

Tout d'abord, lors de la rédaction du app.yaml, en metadata.name j'avai mis des majuscules ce qui avait causé des erreurs. Ensuite j'avais des missmatchs entre mes noms et mes selectors (j'avais pas bien compris comment focntionne les selectors):
```bash
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
The Deployment "helloworld" is invalid: 
* spec.selector: Required value
* spec.template.metadata.labels: Invalid value: {"app":"helloworld"}: `selector` does not match template `labels`
```


Ensuite j'ai eu des erreurs : 
```bash
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods
NAME                                   READY   STATUS             RESTARTS           AGE
helloworld-app-56988bb556-46twz        0/1     Error              5 (93s ago)        3m19s
helloworld-app-56988bb556-4qzcs        0/1     CrashLoopBackOff   5 (14s ago)        3m19s
helloworld-app-56988bb556-55m7j        0/1     Error              5 (95s ago)        3m19s
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods --selector=app=helloworld
NAME                              READY   STATUS             RESTARTS      AGE
helloworld-app-56988bb556-46twz   0/1     CrashLoopBackOff   5 (93s ago)   4m44s
helloworld-app-56988bb556-4qzcs   0/1     CrashLoopBackOff   5 (99s ago)   4m44s
helloworld-app-56988bb556-55m7j   0/1     CrashLoopBackOff   5 (95s ago)   4m44s
```
Quand je regardais les logs, j'avais la raison : 

```bash
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld-app-56988bb556-46twz
exec /usr/local/bin/uvicorn: exec format error
```

La raison était que mon image avait était crée sur une arhitecture différente que celle où j'essayais de la lancer (je l'avais construit sur mon mac et j'essayais de la lancer sur onyxia ce qui ne marchait pas)

Donc j'ai du psuh depuis mon mac une nouvelle image compatibles avec différentes architectures :

```bash
# 1. Créer un builder multi-arch (une seule fois)
docker buildx create --use

# 2. Builder et pousser directement sur Docker Hub pour amd64
docker buildx build \
  --platform linux/amd64 \
  -t moonshayne/tp1-exo1:latest \
  --push \
  .
```

Aussi pour deployer j'ai voulu utiliser un service mais j'ai vu que ce n'était pas ce qui était attendu donc j'ai dû changer.
et quand je lancais le service, sur les pages : https://user-mohamederrafii-898847-0.user.lab.sspcloud.fr/proxy/8081 et https://user-mohamederrafii-898847-0.user.lab.sspcloud.fr/proxy/8081/hello

j'avais l'erreur : 
```bash
connect ECONNREFUSED 0.0.0.0:8081
```

Donc au lieu de lancer un service il fallait faire un port-forward sur le pod avec : 
```bash
kubectl port-forward pod/helloworld-app-5b9599f4f7-67zzp 8081:8081
```