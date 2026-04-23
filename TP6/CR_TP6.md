Pour ce TP, mon code a pour structure : 
```bash 
 TP6 git:(main) tree
.
├── 6_amélioration_application.md
├── CR_TP6.md
├── backend.yaml
├── frontend.yaml
├── postgres.yaml
└── secret.yaml

1 directory, 6 files
```

et je vais pas remettre tout le code car on peut le trouver sur github 

ensuite pour les commandes dnas le terminal, il faut d'abord faire du nettoyage : 
```bash 
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP6$ kubectl delete deployment backend-app frontend-app 
kubectl delete statefulset postgres-db 
kubectl delete service backend frontend-service db db-headless 
kubectl delete secret postgres-secret
```

Ensuite on peut lancer nos nouveaux fichier (atttention l'ordre est encore une fois important): 
```bash
kubectl apply -f secret.yaml
```

```bash
kubectl apply -f postgres.yaml
```
```bash
kubectl apply -f backend.yaml
```
```bash
kubectl apply -f frontend.yaml
```
```bash
kubectl get pods
```
et ça donne 
```bash 
NAME                              READY   STATUS             RESTARTS          AGE
backend-app-7b48f9489b-jsz5k      0/1     Running            0                 14s
frontend-app-7bb8dc7b99-k9tg8     0/1     Running            0                 8s
postgres-db-0                     1/1     Running            0                 5m34s
```
```bash
kubectl get services
```
```bash
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend                ClusterIP   10.233.6.227    <none>        5000/TCP   25s
db                     ClusterIP   10.233.49.78    <none>        5432/TCP   5m45s
db-headless            ClusterIP   None            <none>        5432/TCP   5m45s
frontend-service       ClusterIP   10.233.7.107    <none>        5000/TCP   19s
vscode-python-970652   ClusterIP   None            <none>        8080/TCP   9h
```
```bash
kubectl get pvc
```
```bash
NAME                          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS      VOLUMEATTRIBUTESCLASS   AGE
data-postgresql-439617-0      Bound    pvc-5f3dd795-a5b5-4d98-96ee-1f1ed86bf1eb   10Gi       RWO            rook-ceph-block   <unset>                 380d
data-postgresql-777147-0      Bound    pvc-872aac8f-3d25-4c8d-b54c-52e31e9a69e9   10Gi       RWO            rook-ceph-block   <unset>                 104d
postgres-data-postgres-db-0   Bound    pvc-f609484e-dc2e-476e-981d-913cf7965169   1Gi        RWO            rook-ceph-block   <unset>                 4d14h
vscode-python-970652          Bound    pvc-1637e00a-87eb-4dd3-bdbb-17bea94a0933   10Gi       RWO            rook-ceph-block   <unset>                 9h
```
```bash
kubectl get secrets | grep postgres
```
```bash
postgres-secret                              Opaque                 3      6m5s
```
```bash
kubectl get pod postgres-db-0 -o jsonpath='{.status.qosClass}'
```
```bash
kubectl describe pod -l app=backend | grep -A10 "Init Containers"
```
```bash
Init Containers:
  init-db:
    Container ID:  containerd://ed6314c3e4d7d09571026493781ac44a9efc912bb237e3b33861831341b8ffb6
    Image:         postgres:13
    Image ID:      docker.io/library/postgres@sha256:4689940c683801b4ab839ab3b0a0a3555a5fe425371422310944e89eca7d8068
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      until pg_isready -h db -U admin; do echo "Attente postgres..."; sleep 2; done; psql postgresql://admin:password@db/reviews -c "CREATE TABLE IF NOT EXISTS reviews (id SERIAL PRIMARY KEY, name VARCHAR(100), review TEXT);"
```
```bash
kubectl port-forward service/frontend-service 5000:5000
```
qui donne : 
```bash 
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
Handling connection for 5000
```
et dans un autre terminal 

```bash
kubectl logs deployment/backend-app
```

et avant et après de soumettre une review j'ai : 
```bash 
nyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP6$ kubectl logs deployment/backend-app
Defaulted container "backend-container" out of: backend-container, init-db (init)
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.106.63:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP6$ kubectl logs deployment/backend-app
Defaulted container "backend-container" out of: backend-container, init-db (init)
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.106.63:5000/ (Press CTRL+C to quit)
10.233.106.117 - - [23/Apr/2026 00:18:57] "POST /reviews/add HTTP/1.1" 200 -
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP6$ 
```

ça marche on est content