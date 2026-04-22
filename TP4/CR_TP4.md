# TP 4 — Gestion de la persistance

## Objectifs du TP

- Comprendre les mécanismes de persistance dans Kubernetes
- Ajouter de la persistance à une application
- Déployer une application stateful

Livrables :
- Manifest Kubernetes pour déployer les applications
- Un compte rendu avec les difficultés rencontrées, et les résultats de chaque exercice.

## Prérequis

- Avoir un compte SSPCloud

---

## Exercice : Activer la persistance sur l'application

### Problème de départ

Lors du TP3, la base de données PostgreSQL était déployée via un `Deployment`. Ce type d'objet Kubernetes utilise un stockage **éphémère** : à chaque redémarrage ou suppression du pod, toutes les données sont perdues car le disque est recréé à zéro.

### Solution : passer à un StatefulSet

Un `StatefulSet` associe un `PersistentVolumeClaim (PVC)` à chaque pod. Ce volume persiste indépendamment du cycle de vie du pod — les données survivent aux redémarrages, suppressions et mises à jour.

### Manifest utilisé (`postgres-statefulset.yaml`)

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

### Déploiement

```bash
# Supprimer l'ancien Deployment postgres
kubectl delete deployment postgres-db

# Appliquer le StatefulSet
kubectl apply -f postgres-statefulset.yaml

# Vérifier que le PVC est créé automatiquement
kubectl get pvc
kubectl get pods
```

Résultat :
```
NAME                              READY   STATUS    RESTARTS   AGE
postgres-db-0                     1/1     Running   0          3m35s

NAME                                STATUS   VOLUME   CAPACITY   STORAGECLASS   AGE
postgres-data-postgres-db-0         Bound    ...      1Gi        ...            3m35s
```

---

## Démonstration de la persistance

### Étape 1 — Créer la table et insérer des données

La table `reviews` n'étant pas créée automatiquement par l'image postgres, elle a été créée manuellement :

```bash
kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "
CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  review TEXT
);"
```

Des données ont ensuite été insérées via le frontend (port-forward sur le service frontend), puis vérifiées en base :

```bash
kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
```

Résultat avant suppression du pod :
```
 id |  name  |    review
----+--------+---------------
  1 | Alice  | Très bien !
(1 row)
```

### Étape 2 — Supprimer le pod et vérifier la persistance

```bash
# Supprimer le pod (le StatefulSet le recrée automatiquement)
kubectl delete pod postgres-db-0

# Attendre le redémarrage
kubectl get pods -w
# postgres-db-0   0/1   Pending   0   1s
# postgres-db-0   0/1   Running   0   3s
# postgres-db-0   1/1   Running   0   5s

# Vérifier que les données sont toujours présentes
kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
```

Résultat après redémarrage du pod :
```
 id |  name  |    review
----+--------+---------------
  1 | Alice  | Très bien !
(1 row)
```

Les données sont bien persistées. Le StatefulSet a recréé le pod et l'a rattaché automatiquement au même PVC.

---

## Difficultés rencontrées

**1. Erreur `exec format error` sur le container postgres**

Lors de la première tentative de connexion au pod :

```bash
kubectl exec -it postgres-db-0 -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
# error: Internal error occurred: unable to upgrade connection: container not found ("postgres")
```

Le nom du container dans le StatefulSet est `postgres`, mais kubectl ne le trouvait pas car le pod n'était pas encore complètement démarré. La solution est d'attendre que le pod soit `READY 1/1` et de préciser le nom du container avec `-c postgres`.

**2. Erreur `initdb: directory exists but is not empty`**

```bash
kubectl logs postgres-db-0
# initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
# It contains a lost+found directory, perhaps due to it being a mount point.
```

Quand un PersistentVolume est monté directement sur `/var/lib/postgresql/data`, le système de fichiers y crée automatiquement un dossier `lost+found`. PostgreSQL refuse de s'initialiser dans un dossier non vide.

La solution est de définir la variable d'environnement `PGDATA` pour pointer vers un sous-dossier :

```yaml
- name: PGDATA
  value: /var/lib/postgresql/data/pgdata
```

Cela laisse `lost+found` au niveau supérieur et donne à postgres un dossier propre.

**3. Table `reviews` inexistante après recréation du StatefulSet**

```bash
kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
# ERROR: relation "reviews" does not exist
```

Le backend de l'application ne crée pas automatiquement le schéma de base de données. Après suppression du PVC et recréation du StatefulSet, la base est vide. La table a dû être créée manuellement. En production, ce problème se résout avec des **migrations** (outils comme Alembic ou Flyway) lancées au démarrage du backend — ce qui sera adressé dans un TP suivant via un `initContainer`.

**4. Mise à jour du StatefulSet impossible**

```bash
kubectl apply -f postgres-statefulset.yaml
# The StatefulSet "postgres-db" is invalid: spec: Forbidden: updates to statefulset spec
# for fields other than 'replicas', 'template', 'updateStrategy'...
```

Kubernetes interdit la modification du champ `serviceName` d'un StatefulSet existant. La solution est de supprimer le StatefulSet puis de le recréer — sans supprimer le PVC pour conserver les données.

```bash
kubectl delete statefulset postgres-db   # conserve le PVC
kubectl apply -f postgres-statefulset.yaml
```

---

## Comparaison Deployment vs StatefulSet

| Critère | Deployment | StatefulSet |
|---|---|---|
| Stockage | Éphémère (détruit avec le pod) | Persistant (PVC survit au pod) |
| Nom du pod | Aléatoire (`postgres-xxx-yyy`) | Stable et ordonné (`postgres-db-0`) |
| Redémarrage | Nouveau pod, nouvelles données | Même pod, mêmes données |
| Usage recommandé | Applications sans état (frontend, API) | Bases de données, applications stateful |

Le `StatefulSet` est indispensable pour toute base de données en production sur Kubernetes. Sans lui, chaque redémarrage de pod détruit l'intégralité des données.
