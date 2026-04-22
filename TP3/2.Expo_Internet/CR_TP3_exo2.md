Alors pour cette partie on a utilisé Ingress 

Notre fichier app.yaml a pour code :
```YAML
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

Et dans notre termoinal on doit faire les commandes suivantes pour que ça marche (les mêmes que d'habitude mais on va chercher le ingress au lieu du reste)

On commence par : 
```bash 
kubectl apply -f app.yaml
```
et on obtient : 
```bash
ingress.networking.k8s.io/helloworld-ingress created
```

Puis on fait 
```bash
kubectl get ingress
```
et on a 
```bash
NAME                      CLASS    HOSTS                                               ADDRESS       PORTS     AGE
helloworld-ingress        <none>   helloworld.lab.sspcloud.fr                                        80        7d8h
```
et enfin on fait : 
```bash
curl https://helloworld.lab.sspcloud.fr/hello
```
et on obitent : 

```bash
"world"
```

donc ça marche, nice on peut passer à la suite (la plupart des TPs ont été réalisé il y a un moment déjà mais ont été refait plusieurs fois pour être sûr de bien comprendre toute les notions c'est pour ça que les temps de création ne sont pas toujours cohérent ni les sorties bash que je modifie des fois à la main)