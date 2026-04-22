Cette partie à été réalisé sur onyxia
# Exposition sur le cluster

On a la fichier yaml : 

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
```

Puis on fait dans notre terminal 

```bash
kubectl apply -f apply.yaml
```

On obtient

```bash
deployment.apps/helloworld-app deployed
service/helloworld-service deployed
```

On fera le reste du CR plus tard
