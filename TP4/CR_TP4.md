Pour ce TP on a utilisé le fichier yaml 
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres-db
spec:
  serviceName: db
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
        - name: PGDATA
          value: /var/lib/postgresql/data/pgdata
        volumeMounts:
        - name: postgres-data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: postgres-data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi
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
Ensuite dnas le terminal, il faut faire du tri : 

```bash 
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP4$ kubectl delete deployment postgres-db
deployment.apps "postgres-db" deleted from user-mohamederrafii namespace
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP4$ kubectl delete service db
service "db" deleted from user-mohamederrafii namespace
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP4$ kubectl delete statefulset postgres-db
statefulset.apps "postgres-db" deleted from user-mohamederrafii namespace
```

Puis on peut faire notre kubectl apply 

On obtient avec 
```bash 
kubectl get pods
```

le résultat : 
```bash 
NAME                              READY   STATUS             RESTARTS          AGE
postgres-db-0                     1/1     Running            0                 19s
```
et avec 
```bash 
kubectl get pvc
```

```bash 
NAME                          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS      VOLUMEATTRIBUTESCLASS   AGE
data-postgresql-439617-0      Bound    pvc-5f3dd795-a5b5-4d98-96ee-1f1ed86bf1eb   10Gi       RWO            rook-ceph-block   <unset>                 380d
data-postgresql-777147-0      Bound    pvc-872aac8f-3d25-4c8d-b54c-52e31e9a69e9   10Gi       RWO            rook-ceph-block   <unset>                 104d
postgres-data-postgres-db-0   Bound    pvc-f609484e-dc2e-476e-981d-913cf7965169   1Gi        RWO            rook-ceph-block   <unset>                 4d13h
vscode-python-970652          Bound    pvc-1637e00a-87eb-4dd3-bdbb-17bea94a0933   10Gi       RWO            rook-ceph-block   <unset>                 7h57m
```
ensuite on crée une table 
```bash 
kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "
CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  review TEXT
);"
```
puis on peut passer par la page pour soumettre un review, on peut ensuite la regarder avec : 

```bash 
kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
```
moi j'avais : 
```bash 
 id | name | review 
----+------+--------
  1 | Chef | étoile
(1 row)
```

ensuite on va tester la persistance avec
```bash 
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP4$ kubectl delete pod postgres-db-0
pod "postgres-db-0" deleted from user-mohamederrafii namespace
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;";"
 id | name | review 
----+------+--------
  1 | Chef | étoile
(1 row)
```
Tout marche bien


# Difficulté Rencontré : 


Plusieurs difficultés ont été rencontrées lors de ce TP. La première était liée à la **table `reviews` inexistante** : le backend de l'application ne crée pas automatiquement le schéma de base de données. Après le déploiement du StatefulSet, la base était vide et le backend retournait une erreur `psycopg2.errors.UndefinedTable: relation "reviews" does not exist` lors des tentatives d'insertion. La solution a été de créer la table manuellement via `kubectl exec`.

La deuxième difficulté concernait l'erreur **`initdb: directory exists but is not empty`** lors du premier démarrage du pod postgres avec le PVC. Le système de fichiers du volume crée automatiquement un dossier `lost+found` au montage, ce qui empêche postgres de s'initialiser car il refuse de démarrer dans un dossier non vide. La solution a été d'ajouter la variable d'environnement `PGDATA` pointant vers un sous-dossier (`/var/lib/postgresql/data/pgdata`), laissant `lost+found` au niveau supérieur. Il a également fallu supprimer le StatefulSet et le PVC existants avant de réappliquer le manifest corrigé.

La troisième difficulté était une **erreur de syntaxe kubectl** : `kubectrl` (faute de frappe) et `kubectl get serviced` ont été essayés avant d'utiliser les bonnes commandes. Ces erreurs sont typiques de la prise en main d'un nouvel outil.

Une fois ces obstacles surmontés, la démonstration de persistance a été concluante : après suppression du pod `postgres-db-0`, le StatefulSet l'a recréé automatiquement et les données (`Chef | étoile`) étaient toujours présentes lors du `SELECT * FROM reviews` suivant, confirmant l'intérêt du StatefulSet par rapport au Deployment.



