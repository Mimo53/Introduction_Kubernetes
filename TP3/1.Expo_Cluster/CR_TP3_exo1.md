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
deployment.apps/helloworld-app created
service/helloworld-service created
```

Ensuite on fait 
```bash
kubectl get pods
```
On obtient 
```bash
NAME                              READY   STATUS             RESTARTS       AGE
helloworld-app-6df954dd4d-lqsbx   1/1     Running            0              70m
```

et si on fait 
```bash
kubectl get service
```

On a dans notre terminal 
```bash
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
helloworld-service   ClusterIP   10.233.38.163   <none>        8081/TCP   4d6h
```

Enfin on test notre service avec 
```bash
kubectl run test-curl --image=curlimages/curl --rm -it --restart=Never \
  -- curl http://helloworld-service:8081/hello
```

et on obtient : 
```bash
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/test-curl, falling back to streaming logs: Internal error occurred: unable to upgrade connection: container test-curl not found in pod test-curl_user-mohamederrafii
"world"pod "test-curl" deleted from user-mohamederrafii namespace
```

Donc ça marche bien

# Difficultés recontrés
Au début dans mon service je ne mettais pas ClusterIP mais load balncer ce qui faisait que ça ne marchait pas mais c'est tout de mémoire.
