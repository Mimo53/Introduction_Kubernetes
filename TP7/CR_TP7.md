Vu commenbt il tard quand je fais ce CR je vais juste mettre les sorties de mon terminal je nettoyerais plus tard mais tout marche : 


J'ai commencer par faire ces commandes 
```bash
helm version
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm repo update
helm search repo cnpg
helm show values cnpg/cluster
```
Puis voici la suite

```bash
  
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl delete deployment backend-app 
deployment.apps "backend-app" deleted from user-mohamederrafii namespace
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm lint ./backend-app
==> Linting ./backend-app
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm template ma-release ./backend-app
---
# Source: backend-app/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: ma-release-backend-app-backend
  labels:
    helm.sh/chart: backend-app-0.2.0
    app.kubernetes.io/name: backend-app
    app.kubernetes.io/instance: ma-release
    app.kubernetes.io/version: "1.1"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  selector:
    app.kubernetes.io/name: backend-app
    app.kubernetes.io/instance: ma-release
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
---
# Source: backend-app/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ma-release-backend-app-backend
  labels:
    helm.sh/chart: backend-app-0.2.0
    app.kubernetes.io/name: backend-app
    app.kubernetes.io/instance: ma-release
    app.kubernetes.io/version: "1.1"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 3
  selector:
    matchLabels:
      app.kubernetes.io/name: backend-app
      app.kubernetes.io/instance: ma-release
  template:
    metadata:
      labels:
        app.kubernetes.io/name: backend-app
        app.kubernetes.io/instance: ma-release
    spec:
      containers:
      - name: backend-container
        image: "hugosmn5/backend-3-tier:1.1"
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
        env:
        - name: DB
          value: "reviews"
        - name: DB_HOST
          value: "ma-release-postgresql-rw"
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: ma-release-postgresql-app
              key: username
        - name: DB_PASS
          valueFrom:
            secretKeyRef:
              name: ma-release-postgresql-app
              key: password
---
# Source: backend-app/charts/postgresql/templates/cluster.yaml
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: ma-release-postgresql
  labels:
    helm.sh/chart: postgresql-0.0.9
    app.kubernetes.io/name: postgresql
    app.kubernetes.io/instance: ma-release
    app.kubernetes.io/part-of: cloudnative-pg
    app.kubernetes.io/managed-by: Helm
spec:
  instances: 1
  imageName: ghcr.io/cloudnative-pg/postgresql:15.2
  imagePullPolicy: IfNotPresent
  postgresUID: 26
  postgresGID: 26
  storage:
    size: 1Gi
    storageClass: 
  affinity:
    topologyKey: topology.kubernetes.io/zone
  priorityClassName: 

  primaryUpdateMethod: switchover
  primaryUpdateStrategy: unsupervised
  logLevel: info
  enableSuperuserAccess: true
  postgresql:
    shared_preload_libraries:

  managed:

  monitoring:
    enablePodMonitor: false
  
  
  bootstrap:
    initdb:
      database: reviews
      owner: admin
      postInitApplicationSQL:
---
# Source: backend-app/charts/postgresql/templates/tests/ping.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: ma-release-postgresql-ping-test
  labels:
    app.kubernetes.io/component: database-ping-test
  annotations:
    "helm.sh/hook": test
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  template:
    metadata:
      name: ma-release-postgresql-ping-test
      labels:
        app.kubernetes.io/component: database-ping-test
    spec:
      restartPolicy: Never
      containers:
        - name: alpine
          image: alpine:3.17
          command: [ 'sh' ]
          env:
            - name: PGUSER
              valueFrom:
                secretKeyRef:
                  name: ma-release-postgresql-app
                  key: username
            - name: PGPASS
              valueFrom:
                secretKeyRef:
                  name: ma-release-postgresql-app
                  key: password
          args:
            - "-c"
            - >-
              apk add postgresql-client &&
              psql "postgresql://$PGUSER:$PGPASS@ma-release-postgresql-rw.user-mohamederrafii.svc.cluster.local:5432" -c 'SELECT 1'
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm install ma-release ./backend-app
NAME: ma-release
LAST DEPLOYED: Thu Apr 23 00:29:32 2026
NAMESPACE: user-mohamederrafii
STATUS: deployed
REVISION: 1
NOTES:
Backend déployé avec succès !

Pour accéder au service :
  kubectl port-forward service/ma-release-backend-app-backend 5000:5000
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get deployments,svc,pods
NAME                                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/frontend-app                     1/1     1            1           12m
deployment.apps/helloworld-app                   1/3     3            1           4d15h
deployment.apps/ma-release-backend-app-backend   3/3     3            3           10s

NAME                                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/backend                          ClusterIP   10.233.6.227    <none>        5000/TCP   12m
service/db                               ClusterIP   10.233.49.78    <none>        5432/TCP   18m
service/db-headless                      ClusterIP   None            <none>        5432/TCP   18m
service/frontend-service                 ClusterIP   10.233.7.107    <none>        5000/TCP   12m
service/helloworld-service               ClusterIP   10.233.38.163   <none>        8081/TCP   4d15h
service/ma-release-backend-app-backend   ClusterIP   10.233.7.139    <none>        5000/TCP   10s
service/ma-release-postgresql-r          ClusterIP   10.233.16.195   <none>        5432/TCP   10s
service/ma-release-postgresql-ro         ClusterIP   10.233.42.250   <none>        5432/TCP   10s
service/ma-release-postgresql-rw         ClusterIP   10.233.63.117   <none>        5432/TCP   10s
service/vscode-python-970652             ClusterIP   None            <none>        8080/TCP   9h

NAME                                                  READY   STATUS             RESTARTS         AGE
pod/frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0                12m
pod/helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   126 (84s ago)    10h
pod/helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   126 (87s ago)    10h
pod/helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   126 (107s ago)   10h
pod/helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0                10h
pod/ma-release-backend-app-backend-78c8d8c64b-g2m5x   1/1     Running            0                10s
pod/ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            0                10s
pod/ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            0                10s
pod/ma-release-postgresql-1-initdb-6gv7z              0/1     PodInitializing    0                10s
pod/postgres-db-0                                     1/1     Running            0                18m
pod/vscode-python-970652-0                            1/1     Running            0                9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl logs deployment/ma-release-backend-app-backend
Found 3 pods, using pod/ma-release-backend-app-backend-78c8d8c64b-srt4n
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm dependency update ./backend-app
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "cnpg" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Downloading cluster from repo https://cloudnative-pg.github.io/charts
Deleting outdated charts
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm upgrade ma-release ./backend-app
Release "ma-release" has been upgraded. Happy Helming!
NAME: ma-release
LAST DEPLOYED: Thu Apr 23 00:30:17 2026
NAMESPACE: user-mohamederrafii
STATUS: deployed
REVISION: 2
NOTES:
Backend déployé avec succès !

Pour accéder au service :
  kubectl port-forward service/ma-release-backend-app-backend 5000:5000
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get deployments,clusters,svc,pods
NAME                                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/frontend-app                     1/1     1            1           13m
deployment.apps/helloworld-app                   1/3     3            1           4d15h
deployment.apps/ma-release-backend-app-backend   3/3     3            3           59s

NAME                                               AGE   INSTANCES   READY   STATUS                     PRIMARY
cluster.postgresql.cnpg.io/ma-release-postgresql   59s   1           1       Cluster in healthy state   ma-release-postgresql-1

NAME                                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/backend                          ClusterIP   10.233.6.227    <none>        5000/TCP   13m
service/db                               ClusterIP   10.233.49.78    <none>        5432/TCP   18m
service/db-headless                      ClusterIP   None            <none>        5432/TCP   18m
service/frontend-service                 ClusterIP   10.233.7.107    <none>        5000/TCP   13m
service/helloworld-service               ClusterIP   10.233.38.163   <none>        8081/TCP   4d15h
service/ma-release-backend-app-backend   ClusterIP   10.233.7.139    <none>        5000/TCP   59s
service/ma-release-postgresql-r          ClusterIP   10.233.16.195   <none>        5432/TCP   59s
service/ma-release-postgresql-ro         ClusterIP   10.233.42.250   <none>        5432/TCP   59s
service/ma-release-postgresql-rw         ClusterIP   10.233.63.117   <none>        5432/TCP   59s
service/vscode-python-970652             ClusterIP   None            <none>        8080/TCP   9h

NAME                                                  READY   STATUS             RESTARTS          AGE
pod/frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0                 13m
pod/helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   126 (2m13s ago)   10h
pod/helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   126 (2m16s ago)   10h
pod/helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   126 (2m36s ago)   10h
pod/helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0                 10h
pod/ma-release-backend-app-backend-78c8d8c64b-g2m5x   1/1     Running            1 (36s ago)       59s
pod/ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            1 (37s ago)       59s
pod/ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            1 (35s ago)       59s
pod/ma-release-postgresql-1                           1/1     Running            0                 37s
pod/postgres-db-0                                     1/1     Running            0                 18m
pod/vscode-python-970652-0                            1/1     Running            0                 9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl describe cluster ma-release-postgresql
Name:         ma-release-postgresql
Namespace:    user-mohamederrafii
Labels:       app.kubernetes.io/instance=ma-release
              app.kubernetes.io/managed-by=Helm
              app.kubernetes.io/name=postgresql
              app.kubernetes.io/part-of=cloudnative-pg
              helm.sh/chart=postgresql-0.0.9
Annotations:  meta.helm.sh/release-name: ma-release
              meta.helm.sh/release-namespace: user-mohamederrafii
API Version:  postgresql.cnpg.io/v1
Kind:         Cluster
Metadata:
  Creation Timestamp:  2026-04-23T00:29:32Z
  Generation:          1
  Resource Version:    3901316171
  UID:                 ac9460d6-bd6b-4cb1-a5c7-4419067383ed
Spec:
  Affinity:
    Pod Anti Affinity Type:  preferred
    Topology Key:            topology.kubernetes.io/zone
  Bootstrap:
    Initdb:
      Database:             reviews
      Encoding:             UTF8
      Locale C Type:        C
      Locale Collate:       C
      Owner:                admin
  Enable Pdb:               true
  Enable Superuser Access:  true
  Failover Delay:           0
  Image Name:               ghcr.io/cloudnative-pg/postgresql:15.2
  Image Pull Policy:        IfNotPresent
  Instances:                1
  Log Level:                info
  Max Sync Replicas:        0
  Min Sync Replicas:        0
  Monitoring:
    Custom Queries Config Map:
      Key:                    queries
      Name:                   cnpg-default-monitoring
    Disable Default Queries:  false
    Enable Pod Monitor:       false
  Postgres Gid:               26
  Postgres UID:               26
  Postgresql:
    Parameters:
      archive_mode:                on
      archive_timeout:             5min
      dynamic_shared_memory_type:  posix
      full_page_writes:            on
      log_destination:             csvlog
      log_directory:               /controller/log
      log_filename:                postgres
      log_rotation_age:            0
      log_rotation_size:           0
      log_truncate_on_rotation:    false
      logging_collector:           on
      max_parallel_workers:        32
      max_replication_slots:       32
      max_worker_processes:        32
      shared_memory_type:          mmap
      shared_preload_libraries:    
      ssl_max_protocol_version:    TLSv1.3
      ssl_min_protocol_version:    TLSv1.3
      wal_keep_size:               512MB
      wal_level:                   logical
      wal_log_hints:               on
      wal_receiver_timeout:        5s
      wal_sender_timeout:          5s
    Sync Replica Election Constraint:
      Enabled:              false
  Primary Update Method:    switchover
  Primary Update Strategy:  unsupervised
  Probes:
    Liveness:
      Isolation Check:
        Connection Timeout:  1000
        Enabled:             true
        Request Timeout:     1000
  Replication Slots:
    High Availability:
      Enabled:      true
      Slot Prefix:  _cnpg_
    Synchronize Replicas:
      Enabled:        true
    Update Interval:  30
  Resources:
  Smart Shutdown Timeout:  180
  Start Delay:             3600
  Stop Delay:              1800
  Storage:
    Resize In Use Volumes:  true
    Size:                   1Gi
  Switchover Delay:         3600
Status:
  Available Architectures:
    Go Arch:  amd64
    Hash:     b77f8f908fdc909122fe24fa164f8247c0689c4ca8c01ccef07fc50e7be8f6f1
    Go Arch:  arm64
    Hash:     97fa01dc1c6abcd7f64a51d16f2e4ef9c7bb8d4d842e01adc9d07060e6b84157
  Certificates:
    Client Ca Secret:  ma-release-postgresql-ca
    Expirations:
      Ma - Release - Postgresql - Ca:           2026-07-22 00:24:32 +0000 UTC
      Ma - Release - Postgresql - Replication:  2026-07-22 00:24:32 +0000 UTC
      Ma - Release - Postgresql - Server:       2026-07-22 00:24:32 +0000 UTC
    Replication Tls Secret:                     ma-release-postgresql-replication
    Server Alt Dns Names:
      ma-release-postgresql-rw
      ma-release-postgresql-rw.user-mohamederrafii
      ma-release-postgresql-rw.user-mohamederrafii.svc
      ma-release-postgresql-rw.user-mohamederrafii.svc.cluster.local
      ma-release-postgresql-r
      ma-release-postgresql-r.user-mohamederrafii
      ma-release-postgresql-r.user-mohamederrafii.svc
      ma-release-postgresql-r.user-mohamederrafii.svc.cluster.local
      ma-release-postgresql-ro
      ma-release-postgresql-ro.user-mohamederrafii
      ma-release-postgresql-ro.user-mohamederrafii.svc
      ma-release-postgresql-ro.user-mohamederrafii.svc.cluster.local
    Server Ca Secret:             ma-release-postgresql-ca
    Server Tls Secret:            ma-release-postgresql-server
  Cloud Native Pg Commit Hash:    23eae00cd
  Cloud Native Pg Operator Hash:  b77f8f908fdc909122fe24fa164f8247c0689c4ca8c01ccef07fc50e7be8f6f1
  Conditions:
    Last Transition Time:  2026-04-23T00:30:02Z
    Message:               A single, unique system ID was found across reporting instances.
    Reason:                Unique
    Status:                True
    Type:                  ConsistentSystemID
    Last Transition Time:  2026-04-23T00:30:08Z
    Message:               Cluster is Ready
    Reason:                ClusterIsReady
    Status:                True
    Type:                  Ready
    Last Transition Time:  2026-04-23T00:30:01Z
    Message:               Continuous archiving is working
    Reason:                ContinuousArchivingSuccess
    Status:                True
    Type:                  ContinuousArchiving
  Config Map Resource Version:
    Metrics:
      Cnpg - Default - Monitoring:  3901315380
  Current Primary:                  ma-release-postgresql-1
  Current Primary Timestamp:        2026-04-23T00:30:01.287148Z
  Healthy Pvc:
    ma-release-postgresql-1
  Image:  ghcr.io/cloudnative-pg/postgresql:15.2
  Instance Names:
    ma-release-postgresql-1
  Instances:  1
  Instances Reported State:
    ma-release-postgresql-1:
      Ip:            10.233.106.116
      Is Primary:    true
      Time Line Id:  1
  Instances Status:
    Healthy:
      ma-release-postgresql-1
  Latest Generated Node:  1
  Managed Roles Status:
  Pg Data Image Info:
    Image:          ghcr.io/cloudnative-pg/postgresql:15.2
    Major Version:  15
  Phase:            Cluster in healthy state
  Pooler Integrations:
    Pg Bouncer Integration:
  Pvc Count:        1
  Read Service:     ma-release-postgresql-r
  Ready Instances:  1
  Secrets Resource Version:
    Application Secret Version:  3901315334
    Client Ca Secret Version:    3901315323
    Replication Secret Version:  3901315328
    Server Ca Secret Version:    3901315323
    Server Secret Version:       3901315325
    Superuser Secret Version:    3901315332
  Switch Replica Cluster Status:
  System Id:                 7631745380660527151
  Target Primary:            ma-release-postgresql-1
  Target Primary Timestamp:  2026-04-23T00:29:32.834299Z
  Timeline Id:               1
  Topology:
    Instances:
      ma-release-postgresql-1:
    Nodes Used:              1
    Successfully Extracted:  true
  Write Service:             ma-release-postgresql-rw
Events:
  Type    Reason                       Age   From            Message
  ----    ------                       ----  ----            -------
  Normal  CreatingPodDisruptionBudget  67s   cloudnative-pg  Creating PodDisruptionBudget ma-release-postgresql-primary
  Normal  CreatingServiceAccount       67s   cloudnative-pg  Creating ServiceAccount
  Normal  CreatingRole                 67s   cloudnative-pg  Creating Cluster Role
  Normal  CreatingInstance             67s   cloudnative-pg  Primary instance (initdb)
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get secrets | grep postgresql
ma-release-postgresql-app                    kubernetes.io/basic-auth   11     78s
ma-release-postgresql-ca                     Opaque                     2      78s
ma-release-postgresql-replication            kubernetes.io/tls          2      78s
ma-release-postgresql-server                 kubernetes.io/tls          2      78s
ma-release-postgresql-superuser              kubernetes.io/basic-auth   11     78s
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl logs deployment/ma-release-backend-app-backend
Found 3 pods, using pod/ma-release-backend-app-backend-78c8d8c64b-srt4n
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.106.166:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm upgrade ma-release ./backend-app
Release "ma-release" has been upgraded. Happy Helming!
NAME: ma-release
LAST DEPLOYED: Thu Apr 23 00:31:10 2026
NAMESPACE: user-mohamederrafii
STATUS: deployed
REVISION: 3
NOTES:
Backend déployé avec succès !

Pour accéder au service :
  kubectl port-forward service/ma-release-backend-app-backend 5000:5000
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get pods
NAME                                              READY   STATUS             RESTARTS          AGE
frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0                 14m
helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   126 (3m2s ago)    10h
helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   126 (3m5s ago)    10h
helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   126 (3m25s ago)   10h
helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0                 10h
ma-release-backend-app-backend-78c8d8c64b-g2m5x   1/1     Running            1 (85s ago)       108s
ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            1 (86s ago)       108s
ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            1 (84s ago)       108s
ma-release-postgresql-1                           1/1     Running            0                 86s
postgres-db-0                                     1/1     Running            0                 19m
vscode-python-970652-0                            1/1     Running            0                 9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm history ma-release
REVISION        UPDATED                         STATUS          CHART                   APP VERSION     DESCRIPTION     
1               Thu Apr 23 00:29:32 2026        superseded      backend-app-0.2.0       1.1             Install complete
2               Thu Apr 23 00:30:17 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
3               Thu Apr 23 00:31:10 2026        deployed        backend-app-0.2.0       1.1             Upgrade complete
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm rollback ma-release 2
Rollback was a success! Happy Helming!
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get pods
NAME                                              READY   STATUS             RESTARTS          AGE
frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0                 14m
helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   126 (3m28s ago)   10h
helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   126 (3m31s ago)   10h
helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   126 (3m51s ago)   10h
helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0                 10h
ma-release-backend-app-backend-78c8d8c64b-g2m5x   1/1     Running            1 (111s ago)      2m14s
ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            1 (112s ago)      2m14s
ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            1 (110s ago)      2m14s
ma-release-postgresql-1                           1/1     Running            0                 112s
postgres-db-0                                     1/1     Running            0                 20m
vscode-python-970652-0                            1/1     Running            0                 9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm history ma-release
REVISION        UPDATED                         STATUS          CHART                   APP VERSION     DESCRIPTION     
1               Thu Apr 23 00:29:32 2026        superseded      backend-app-0.2.0       1.1             Install complete
2               Thu Apr 23 00:30:17 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
3               Thu Apr 23 00:31:10 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
4               Thu Apr 23 00:31:38 2026        deployed        backend-app-0.2.0       1.1             Rollback to 2   
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm upgrade ma-release ./backend-app -f values-prod.yaml
Error: open values-prod.yaml: no such file or directory
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm upgrade ma-release ./backend-app -f values-prod.yaml
Error: open values-prod.yaml: no such file or directory
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm upgrade ma-release ./backend-app
Release "ma-release" has been upgraded. Happy Helming!
NAME: ma-release
LAST DEPLOYED: Thu Apr 23 00:33:43 2026
NAMESPACE: user-mohamederrafii
STATUS: deployed
REVISION: 5
NOTES:
Backend déployé avec succès !

Pour accéder au service :
  kubectl port-forward service/ma-release-backend-app-backend 5000:5000
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get pods
NAME                                              READY   STATUS             RESTARTS        AGE
frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0               16m
helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   127 (23s ago)   10h
helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   127 (35s ago)   10h
helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   127 (45s ago)   10h
helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0               10h
ma-release-backend-app-backend-78c8d8c64b-g2m5x   1/1     Terminating        1 (3m57s ago)   4m20s
ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            1 (3m58s ago)   4m20s
ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            1 (3m56s ago)   4m20s
ma-release-postgresql-1                           1/1     Running            0               3m58s
postgres-db-0                                     1/1     Running            0               22m
vscode-python-970652-0                            1/1     Running            0               9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ 
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm history ma-release
REVISION        UPDATED                         STATUS          CHART                   APP VERSION     DESCRIPTION     
1               Thu Apr 23 00:29:32 2026        superseded      backend-app-0.2.0       1.1             Install complete
2               Thu Apr 23 00:30:17 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
3               Thu Apr 23 00:31:10 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
4               Thu Apr 23 00:31:38 2026        superseded      backend-app-0.2.0       1.1             Rollback to 2   
5               Thu Apr 23 00:33:43 2026        deployed        backend-app-0.2.0       1.1             Upgrade complete
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm rollback ma-release 2
Rollback was a success! Happy Helming!
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get pods
NAME                                              READY   STATUS             RESTARTS        AGE
frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0               17m
helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   127 (51s ago)   10h
helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   127 (63s ago)   10h
helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   127 (73s ago)   10h
helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0               10h
ma-release-backend-app-backend-78c8d8c64b-8dhr4   1/1     Running            0               7s
ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            1 (4m26s ago)   4m48s
ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            1 (4m24s ago)   4m48s
ma-release-postgresql-1                           1/1     Running            0               4m26s
postgres-db-0                                     1/1     Running            0               22m
vscode-python-970652-0                            1/1     Running            0               9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm history ma-release
REVISION        UPDATED                         STATUS          CHART                   APP VERSION     DESCRIPTION     
1               Thu Apr 23 00:29:32 2026        superseded      backend-app-0.2.0       1.1             Install complete
2               Thu Apr 23 00:30:17 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
3               Thu Apr 23 00:31:10 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
4               Thu Apr 23 00:31:38 2026        superseded      backend-app-0.2.0       1.1             Rollback to 2   
5               Thu Apr 23 00:33:43 2026        superseded      backend-app-0.2.0       1.1             Upgrade complete
6               Thu Apr 23 00:34:12 2026        deployed        backend-app-0.2.0       1.1             Rollback to 2   
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ cat > values-prod.yaml << 'EOF'
replicaCount: 3
EOF
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ cat values-prod.yaml
replicaCount: 3
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm upgrade ma-release ./backend-app -f values-prod.yaml
Release "ma-release" has been upgraded. Happy Helming!
NAME: ma-release
LAST DEPLOYED: Thu Apr 23 00:35:18 2026
NAMESPACE: user-mohamederrafii
STATUS: deployed
REVISION: 7
NOTES:
Backend déployé avec succès !

Pour accéder au service :
  kubectl port-forward service/ma-release-backend-app-backend 5000:5000
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get pods
NAME                                              READY   STATUS             RESTARTS          AGE
frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0                 18m
helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   127 (2m2s ago)    10h
helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   127 (2m14s ago)   10h
helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   127 (2m24s ago)   10h
helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0                 10h
ma-release-backend-app-backend-78c8d8c64b-8dhr4   1/1     Running            0                 78s
ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Running            1 (5m37s ago)     5m59s
ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Running            1 (5m35s ago)     5m59s
ma-release-postgresql-1                           1/1     Running            0                 5m37s
postgres-db-0                                     1/1     Running            0                 23m
vscode-python-970652-0                            1/1     Running            0                 9h
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ helm uninstall ma-release
release "ma-release" uninstalled
onyxia@vscode-python-970652-0:~/work/Introduction_Kubernetes/TP7$ kubectl get all
NAME                                                  READY   STATUS             RESTARTS          AGE
pod/frontend-app-7bb8dc7b99-k9tg8                     1/1     Running            0                 18m
pod/helloworld-app-56988bb556-47xl5                   0/1     CrashLoopBackOff   127 (2m18s ago)   10h
pod/helloworld-app-56988bb556-6dvbb                   0/1     CrashLoopBackOff   127 (2m30s ago)   10h
pod/helloworld-app-56988bb556-c8rx5                   0/1     CrashLoopBackOff   127 (2m40s ago)   10h
pod/helloworld-app-6df954dd4d-lqsbx                   1/1     Running            0                 10h
pod/ma-release-backend-app-backend-78c8d8c64b-8dhr4   1/1     Terminating        0                 94s
pod/ma-release-backend-app-backend-78c8d8c64b-srt4n   1/1     Terminating        1 (5m53s ago)     6m15s
pod/ma-release-backend-app-backend-78c8d8c64b-vlbjg   1/1     Terminating        1 (5m51s ago)     6m15s
pod/ma-release-postgresql-1                           1/1     Terminating        0                 5m53s
pod/postgres-db-0                                     1/1     Running            0                 24m
pod/vscode-python-970652-0                            1/1     Running            0                 9h

NAME                           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/backend                ClusterIP   10.233.6.227    <none>        5000/TCP   18m
service/db                     ClusterIP   10.233.49.78    <none>        5432/TCP   24m
service/db-headless            ClusterIP   None            <none>        5432/TCP   24m
service/frontend-service       ClusterIP   10.233.7.107    <none>        5000/TCP   18m
service/helloworld-service     ClusterIP   10.233.38.163   <none>        8081/TCP   4d15h
service/vscode-python-970652   ClusterIP   None            <none>        8080/TCP   9h

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/frontend-app     1/1     1            1           18m
deployment.apps/helloworld-app   1/3     3            1           4d15h

NAME                                        DESIRED   CURRENT   READY   AGE
replicaset.apps/frontend-app-7bb8dc7b99     1         1         1       18m
replicaset.apps/helloworld-app-56988bb556   3         3         0       4d15h
replicaset.apps/helloworld-app-6df954dd4d   1         1         1       10h

NAME                                    READY   AGE
statefulset.apps/postgres-db            1/1     24m
statefulset.apps/vscode-python-970652   1/1     9h
```
