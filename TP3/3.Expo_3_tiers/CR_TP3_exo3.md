Mon code a pour structure :

```bash
➜  3.Expo_3_tiers git:(main) tree
.
├── backend.yaml
├── frontend.yaml
└── postgres.yaml
```

backend.yaml a pour code : 
```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend-container
        image: hugosmn5/backend-3-tier:1.1
        imagePullPolicy: Always
        ports:
        - containerPort: 5000 
        env:
        - name: DB_HOST
          value: "db"
        - name: DB_USER
          value: "admin"
        - name: DB_PASS
          value: "password"
        - name: DB
          value: "reviews"
---
apiVersion: v1
kind: Service
metadata:
  name: backend 
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
```

frontend.yaml a pour code :

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend-container
        image: hugosmn5/frontend-3-tier:1.1
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  type: ClusterIP
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
```

et postgres.yaml a pour code : 
```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-db
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:13
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_USER
          value: "admin"
        - name: POSTGRES_PASSWORD
          value: "password"
        - name: POSTGRES_DB
          value: "reviews"
---
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  type: ClusterIP
  selector:
    app: postgres
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
```

Ensuite dans le terminal après s'être placé dans le bon dossier (là où il y a tout les fichiers) il faut faire les kbectl apply dans le bon ordre (c'est important)

On fait : 

```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f postgres.yaml
deployment.apps/postgres-db created
service/db configured
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f backend.yaml
deployment.apps/backend-app configured
service/backend configured
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f frontend.yaml
deployment.apps/frontend-app configured
service/frontend-service configured
```
Ensuite on regarde que tout marche bien : 

```bash
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get pods
NAME                              READY   STATUS             RESTARTS          AGE
backend-app-85f948fd95-fzkmw      1/1     Running            0                 48s
frontend-app-f9767664-7xpr6       1/1     Running            0                 29s
postgres-db-7f6c48dc7f-rhpt8      1/1     Running            0                 65s
```

Tout à l'air de marcher, on va maintenant regarder les services : 
 ```bash 
 onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get service
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend                ClusterIP   10.233.51.125   <none>        5000/TCP   4d13h
db                     ClusterIP   10.233.9.248    <none>        5432/TCP   4d13h
frontend-service       ClusterIP   10.233.34.156   <none>        5000/TCP   4d13h
```

Et enfin on regarde si ça marche avec  
```bash
kubectl port-forward service/frontend-service 5000:5000
```
on obtient 
```bash
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
```
Puis on peut ouvrir la page qui a pour url : 

```text
https://user-mohamederrafii-970652-0.user.lab.sspcloud.fr/proxy/5000/
```

et enfin on regarde les logs  : 

```bash
kubectl logs deployment/backend-app
```

et on a comme sortie : 
```bash
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.127.219:5000/ (Press CTRL+C to quit)
 ```

 Donc tout est bon on peut passer au TP4

# Difficulté Rencontré : 

Plusieurs difficultés ont été rencontrées lors de ce déploiement. La première concernait les mauvais ports dans les manifests : le frontend et le backend étaient initialement configurés sur les ports 8501 et 8000 respectivement, alors que les deux images Flask écoutaient en réalité sur le port 5000. C'est la commande kubectl logs | grep "Running on" qui a permis d'identifier les ports réels. Cette erreur s'est manifestée par un port-forward qui échouait immédiatement avec connection refused.
La deuxième difficulté était liée à la confusion entre kubectl get et kubectl logs : les commandes kubectl get logs et kubectl get log ont été essayées avant de comprendre que logs est un sous-commande directe de kubectl et non un type de ressource (kubectl logs <pod>).
Enfin, lors du test fonctionnel, le port-forward sur le port 5000 échouait avec address already in use car un autre processus occupait déjà ce port localement. La solution a été d'attendre la libération du port ou de redémarrer le port-forward.
Malgré ces difficultés, l'application a bien fonctionné une fois les ports corrigés, comme en témoignent les logs du backend affichant POST /reviews/add HTTP/1.1" 200 et POST / HTTP/1.1" 302 confirmant que la chaîne frontend → backend → postgres était opérationnelle.

