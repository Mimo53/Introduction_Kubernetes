Mon code a pour structure :

```bash
➜  TP5 git:(main) tree
.
├── Dockerfile
├── app.yaml
└── python-api
    ├── requirements.txt
    └── src
        └── main.py
```

`main.py` a pour code :

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

`app.yaml` a pour code :

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
---
apiVersion: v1
kind: Service
metadata:
  name: helloworld-service
spec:
  type: ClusterIP
  selector:
    app: helloworld
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: helloworld-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: helloworld.lab.sspcloud.fr
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: helloworld-service
            port:
              number: 8081
```

La structure du TP5 a d'abord été mise en place en copiant les fichiers du TP1 Exo1 :

```bash
mkdir -p TP5/python-api/src
cp TP1/Exo1/Dockerfile TP5/
cp TP1/Exo1/python-api/requirements.txt TP5/python-api/
cp TP1/Exo1/python-api/src/main.py TP5/python-api/src/
```

Ensuite on a taggé l'image existante en v1, puis on a buildé et pushé les images v2 (avec `/health`) et v3 (avec `/health` et `/ensai`) :

```bash
docker tag moonshayne/tp1-exo1:latest moonshayne/tp1-exo1:v1
docker push moonshayne/tp1-exo1:v1

docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v2 --push .
docker buildx build --platform linux/amd64 -t moonshayne/tp1-exo1:v3 --push .
```

Puis depuis Onyxia, on applique le manifest et on observe le rollout :

```bash
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ kubectl apply -f app.yaml
deployment.apps/helloworld-app configured
service/helloworld-service unchanged
ingress.networking.k8s.io/helloworld-ingress unchanged
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ kubectl rollout status deployment helloworld-app
Waiting for deployment "helloworld-app" rollout to finish: 2 of 3 updated replicas are available...
deployment "helloworld-app" successfully rolled out
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ kubectl rollout history deployment helloworld-app
deployment.apps/helloworld-app 
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

On vérifie ensuite que les trois routes répondent correctement :

```bash
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ curl https://helloworld.lab.sspcloud.fr/hello
"world"
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ curl https://helloworld.lab.sspcloud.fr/health
{"status":"ok"}
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ curl https://helloworld.lab.sspcloud.fr/ensai
{"message":"Bienvenue à l'ENSAI !"}
```

Tout fonctionne. On peut maintenant tester le rollback :

```bash
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ kubectl rollout undo deployment helloworld-app
deployment.apps/helloworld-app rolled back
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP5$ kubectl rollout history deployment helloworld-app
deployment.apps/helloworld-app 
REVISION  CHANGE-CAUSE
2         <none>
3         <none>
```

Le rollback a bien créé une nouvelle révision (3) correspondant au retour à la version précédente.


## Difficultés rencontrées

La principale difficulté de ce TP concernait le **push de l'image v2 vers Docker Hub**, qui a échoué une première fois à cause d'une connexion réseau instable (`write: broken pipe`). Le build s'était pourtant terminé avec succès, mais le transfert des layers vers le registry a été interrompu plusieurs fois de suite. La solution a été simplement de relancer la même commande, qui a réussi au second essai grâce au cache Docker (les layers déjà construits n'ont pas eu besoin d'être reconstruits).

Une erreur de commande a également été rencontrée au démarrage : `docker build -t tp1-exo1` sans spécifier le chemin du contexte (le `.` final), ce qui a produit l'erreur `docker buildx build requires 1 argument`. La syntaxe correcte est `docker build -t <nom> .` où le point désigne le répertoire courant comme contexte de build.

Hormis ces points, le TP s'est déroulé sans difficulté majeure. Les probes et le RollingUpdate sont des fonctionnalités natives de Kubernetes qui ne nécessitent que des ajouts dans le manifest existant. Le point de vigilance principal est de s'assurer que le port spécifié dans les probes correspond bien au port sur lequel l'application écoute réellement (ici 8081 pour uvicorn).