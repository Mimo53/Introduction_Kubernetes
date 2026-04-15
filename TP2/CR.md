onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes$ cd TP2/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
Error from server (Invalid): error when creating "app.yaml": Deployment.apps "HelloWorld" is invalid: [metadata.name: Invalid value: "HelloWorld": a lowercase RFC 1123 subdomain must consist of lower case alphanumeric characters, '-' or '.', and must start and end with an alphanumeric character (e.g. 'example.com', regex used for validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*'), spec.selector: Required value, spec.template.metadata.labels: Invalid value: {"app":"HelloWorld"}: `selector` does not match template `labels`, spec.template.spec.containers[0].name: Invalid value: "HelloWorld-container": a lowercase RFC 1123 label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character (e.g. 'my-name',  or '123-abc', regex used for validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?')]
Error from server (Invalid): error when creating "app.yaml": Service "TP2-service" is invalid: metadata.name: Invalid value: "TP2-service": a DNS-1035 label must consist of lower case alphanumeric characters or '-', start with an alphabetic character, and end with an alphanumeric character (e.g. 'my-name',  or 'abc-123', regex used for validation is '[a-z]([-a-z0-9]*[a-z0-9])?')
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git add .
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git commit -m"Dernier push du lundi 13/04"
[main e91ff26] Dernier push du lundi 13/04
 1 file changed, 28 insertions(+)
 create mode 100644 TP2/app.yaml
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 104 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 602 bytes | 602.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Mimo53/Introduction_Kubernetes.git
   d5be729..e91ff26  main -> main
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ ls
2_premiers_pas_kube.md  app.yaml
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
Error from server (Invalid): error when creating "app.yaml": Deployment.apps "helloworld" is invalid: [spec.selector: Required value, spec.template.metadata.labels: Invalid value: {"app":"helloworld"}: `selector` does not match template `labels`]
Error from server (Invalid): error when creating "app.yaml": Service "TP2-service" is invalid: metadata.name: Invalid value: "TP2-service": a DNS-1035 label must consist of lower case alphanumeric characters or '-', start with an alphabetic character, and end with an alphanumeric character (e.g. 'my-name',  or 'abc-123', regex used for validation is '[a-z]([-a-z0-9]*[a-z0-9])?')
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git add .
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git commit -m"Push pour éviter le conflit avec le fichier sur le mac"
[main 237a285] Push pour éviter le conflit avec le fichier sur le mac
 1 file changed, 3 insertions(+), 3 deletions(-)
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 104 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 426 bytes | 426.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Mimo53/Introduction_Kubernetes.git
   e91ff26..237a285  main -> main
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 414 bytes | 207.00 KiB/s, done.
From https://github.com/Mimo53/Introduction_Kubernetes
   237a285..c0c10d7  main       -> origin/main
Updating 237a285..c0c10d7
Fast-forward
 TP2/app.yaml | 19 ++++++-------------
 1 file changed, 6 insertions(+), 13 deletions(-)
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
deployment.apps/helloworld-app created
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs
error: expected 'logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER]'.
POD or TYPE/NAME is a required argument for the logs command
See 'kubectl logs -h' for help and examples
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs -h
Print the logs for a container in a pod or specified resource. If the pod has only one container, the container name is
optional.

Examples:
  # Return snapshot logs from pod nginx with only one container
  kubectl logs nginx
  
  # Return snapshot logs from pod nginx, prefixing each line with the source pod and container name
  kubectl logs nginx --prefix
  
  # Return snapshot logs from pod nginx, limiting output to 500 bytes
  kubectl logs nginx --limit-bytes=500
  
  # Return snapshot logs from pod nginx, waiting up to 20 seconds for it to start running.
  kubectl logs nginx --pod-running-timeout=20s
  
  # Return snapshot logs from pod nginx with multi containers
  kubectl logs nginx --all-containers=true
  
  # Return snapshot logs from all pods in the deployment nginx
  kubectl logs deployment/nginx --all-pods=true
  
  # Return snapshot logs from all containers in pods defined by label app=nginx
  kubectl logs -l app=nginx --all-containers=true
  
  # Return snapshot logs from all pods defined by label app=nginx, limiting concurrent log requests to 10 pods
  kubectl logs -l app=nginx --max-log-requests=10
  
  # Return snapshot of previous terminated ruby container logs from pod web-1
  kubectl logs -p -c ruby web-1
  
  # Begin streaming the logs from pod nginx, continuing even if errors occur
  kubectl logs nginx -f --ignore-errors=true
  
  # Begin streaming the logs of the ruby container in pod web-1
  kubectl logs -f -c ruby web-1
  
  # Begin streaming the logs from all containers in pods defined by label app=nginx
  kubectl logs -f -l app=nginx --all-containers=true
  
  # Display only the most recent 20 lines of output in pod nginx
  kubectl logs --tail=20 nginx
  
  # Show all logs from pod nginx written in the last hour
  kubectl logs --since=1h nginx
  
  # Show all logs with timestamps from pod nginx starting from August 30, 2024, at 06:00:00 UTC
  kubectl logs nginx --since-time=2024-08-30T06:00:00Z --timestamps=true
  
  # Show logs from a kubelet with an expired serving certificate
  kubectl logs --insecure-skip-tls-verify-backend nginx
  
  # Return snapshot logs from first container of a job named hello
  kubectl logs job/hello
  
  # Return snapshot logs from container nginx-1 of a deployment named nginx
  kubectl logs deployment/nginx -c nginx-1

Options:
    --all-containers=false:
        Get all containers' logs in the pod(s).

    --all-pods=false:
        Get logs from all pod(s). Sets prefix to true.

    -c, --container='':
        Print the logs of this container

    -f, --follow=false:
        Specify if the logs should be streamed.

    --ignore-errors=false:
        If watching / following pod logs, allow for any errors that occur to be non-fatal

    --insecure-skip-tls-verify-backend=false:
        Skip verifying the identity of the kubelet that logs are requested from.  In theory, an attacker could provide
        invalid log content back. You might want to use this if your kubelet serving certificates have expired.

    --limit-bytes=0:
        Maximum bytes of logs to return. Defaults to no limit.

    --max-log-requests=5:
        Specify maximum number of concurrent logs to follow when using by a selector. Defaults to 5.

    --pod-running-timeout=20s:
        The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running

    --prefix=false:
        Prefix each log line with the log source (pod name and container name)

    -p, --previous=false:
        If true, print the logs for the previous instance of the container in a pod if it exists.

    -l, --selector='':
        Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l
        key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label
        constraints.

    --since=0s:
        Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs. Only one of
        since-time / since may be used.

    --since-time='':
        Only return logs after a specific date (RFC3339). Defaults to all logs. Only one of since-time / since may be
        used.

    --tail=-1:
        Lines of recent log file to display. Defaults to -1 with no selector, showing all log lines otherwise 10, if a
        selector is provided.

    --timestamps=false:
        Include timestamps on each line in the log output

Usage:
  kubectl logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER] [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl explain pods
KIND:       Pod
VERSION:    v1

DESCRIPTION:
    Pod is a collection of containers that can run on a host. This resource is
    created by clients and scheduled onto hosts.
    
FIELDS:
  apiVersion    <string>
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

  kind  <string>
    Kind is a string value representing the REST resource this object
    represents. Servers may infer this from the endpoint the client submits
    requests to. Cannot be updated. In CamelCase. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

  metadata      <ObjectMeta>
    Standard object's metadata. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

  spec  <PodSpec>
    Specification of the desired behavior of the pod. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

  status        <PodStatus>
    Most recently observed status of the pod. This data may not be up to date.
    Populated by the system. Read-only. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status


onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get services
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend-service        ClusterIP   10.233.56.32    <none>        8080/TCP   62d
database               ClusterIP   10.233.54.207   <none>        5432/TCP   62d
frontend-service       ClusterIP   10.233.34.44    <none>        80/TCP     62d
python-api-service     ClusterIP   10.233.29.18    <none>        80/TCP     62d
vscode-python-898847   ClusterIP   None            <none>        8080/TCP   12h
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods
NAME                                   READY   STATUS             RESTARTS           AGE
backend-65775c467c-6zfkr               0/1     CrashLoopBackOff   1676 (2m41s ago)   8d
database-d55d8545f-98pzp               1/1     Running            1 (3d17h ago)      8d
frontend-6786fb9868-66bjg              0/1     Error              1390               8d
frontend-6786fb9868-lxwft              0/1     Error              2                  3d17h
frontend-6786fb9868-v6zkv              0/1     Error              282 (5m13s ago)    24h
helloworld-app-56988bb556-46twz        0/1     Error              5 (93s ago)        3m19s
helloworld-app-56988bb556-4qzcs        0/1     CrashLoopBackOff   5 (14s ago)        3m19s
helloworld-app-56988bb556-55m7j        0/1     Error              5 (95s ago)        3m19s
python-api-deployment-f59ff958-lmw28   1/1     Running            1 (3d17h ago)      41d
python-api-deployment-f59ff958-lx9cr   1/1     Running            1 (3d17h ago)      8d
python-api-deployment-f59ff958-v6sfn   1/1     Running            1 (3d17h ago)      20d
vscode-python-898847-0                 1/1     Running            0                  12h
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods --selector=app=helloworld
NAME                              READY   STATUS             RESTARTS      AGE
helloworld-app-56988bb556-46twz   0/1     CrashLoopBackOff   5 (93s ago)   4m44s
helloworld-app-56988bb556-4qzcs   0/1     CrashLoopBackOff   5 (99s ago)   4m44s
helloworld-app-56988bb556-55m7j   0/1     CrashLoopBackOff   5 (95s ago)   4m44s
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld-app-56988bb556-46twz
exec /usr/local/bin/uvicorn: exec format error
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld
error: error from server (NotFound): pods "helloworld" not found in namespace "user-mohamederrafii"
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl exec helloworld-app-56988bb556-46twz -- ls  / 
error: Internal error occurred: unable to upgrade connection: container not found ("helloworld-container")
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ cd ..
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes$ cd TP1/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1$ cd Exo1/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo1$ docker run -p 8081:8081 tp1-exo1
bash: docker: command not found
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo1$ docker images
bash: docker: command not found
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo1$ # Supprimer les déploiements en erreur (supprime aussi les pods associés automatiquement)
kubectl delete deployment frontend
kubectl delete deployment backend-65775c467c   # adapter si le nom exact diffère
kubectl delete deployment helloworld-app

# Supprimer les services associés devenus inutiles
kubectl delete service frontend-service
kubectl delete service backend-service
kubectl delete service helloworld-service

# Vérifier le résultat
kubectl get pods
kubectl get services
deployment.apps "frontend" deleted from user-mohamederrafii namespace
Error from server (NotFound): deployments.apps "backend-65775c467c" not found
deployment.apps "helloworld-app" deleted from user-mohamederrafii namespace
service "frontend-service" deleted from user-mohamederrafii namespace
service "backend-service" deleted from user-mohamederrafii namespace
Error from server (NotFound): services "helloworld-service" not found
NAME                                   READY   STATUS             RESTARTS         AGE
backend-65775c467c-6zfkr               0/1     CrashLoopBackOff   1680 (74s ago)   8d
database-d55d8545f-98pzp               1/1     Running            1 (3d17h ago)    8d
python-api-deployment-f59ff958-lmw28   1/1     Running            1 (3d17h ago)    41d
python-api-deployment-f59ff958-lx9cr   1/1     Running            1 (3d17h ago)    8d
python-api-deployment-f59ff958-v6sfn   1/1     Running            1 (3d17h ago)    20d
vscode-python-898847-0                 1/1     Running            0                13h
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
database               ClusterIP   10.233.54.207   <none>        5432/TCP   62d
python-api-service     ClusterIP   10.233.29.18    <none>        80/TCP     62d
vscode-python-898847   ClusterIP   None            <none>        8080/TCP   13h
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo1$ kubectl delete deployment backend-65775c467c-6zfkr
Error from server (NotFound): deployments.apps "backend-65775c467c-6zfkr" not found
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo1$ kubectl deployment
error: unknown command "deployment" for "kubectl"
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo1$ cd ..
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1$ kubectl get deployment
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
backend                 0/1     1            0           62d
database                1/1     1            1           62d
python-api-deployment   3/3     3            3           62d
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1$ kubectl delete deployment backend
deployment.apps "backend" deleted from user-mohamederrafii namespace
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1$ cd ..
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes$ cd TP2/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
error: error parsing app.yaml: error converting YAML to JSON: yaml: line 22: could not find expected ':'
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
The Deployment "helloworld" is invalid: 
* spec.selector: Required value
* spec.template.metadata.labels: Invalid value: {"app":"helloworld"}: `selector` does not match template `labels`
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
deployment.apps/helloworld-app created
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods
NAME                                   READY   STATUS             RESTARTS        AGE
database-d55d8545f-98pzp               1/1     Running            1 (3d18h ago)   8d
helloworld-app-56988bb556-9rdt7        0/1     CrashLoopBackOff   1 (9s ago)      15s
helloworld-app-56988bb556-hb6k5        0/1     Error              1 (14s ago)     15s
helloworld-app-56988bb556-jsbqw        0/1     CrashLoopBackOff   1 (9s ago)      15s
python-api-deployment-f59ff958-lmw28   1/1     Running            1 (3d18h ago)   41d
python-api-deployment-f59ff958-lx9cr   1/1     Running            1 (3d18h ago)   8d
python-api-deployment-f59ff958-v6sfn   1/1     Running            1 (3d18h ago)   20d
vscode-python-898847-0                 1/1     Running            0               14h
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get deployment
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
database                1/1     1            1           62d
helloworld-app          0/3     3            0           37s
python-api-deployment   3/3     3            3           62d
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld-app-56988bb556-9rdt7
exec /usr/local/bin/uvicorn: exec format error
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld-app-56988bb556-hb6k5
exec /usr/local/bin/uvicorn: exec format error
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs helloworld-app-56988bb556-jsbqw
exec /usr/local/bin/uvicorn: exec format error
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ git pull
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 1), reused 4 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 382 bytes | 382.00 KiB/s, done.
From https://github.com/Mimo53/Introduction_Kubernetes
   c0c10d7..f8a7027  main       -> origin/main
Updating c0c10d7..f8a7027
Fast-forward
 TP2/CR.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 TP2/CR.md
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl rollout restart deploymeny helloworld-app
error: the server doesn't have a resource type "deploymeny"
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl rollout restart deployment helloworld-app
deployment.apps/helloworld-app restarted
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get pods
NAME                                   READY   STATUS    RESTARTS        AGE
database-d55d8545f-98pzp               1/1     Running   1 (3d18h ago)   8d
helloworld-app-5b9599f4f7-67zzp        1/1     Running   0               6m40s
helloworld-app-5b9599f4f7-c7plk        1/1     Running   0               6m28s
helloworld-app-5b9599f4f7-jw828        1/1     Running   0               6m34s
python-api-deployment-f59ff958-lmw28   1/1     Running   1 (3d18h ago)   41d
python-api-deployment-f59ff958-lx9cr   1/1     Running   1 (3d18h ago)   8d
python-api-deployment-f59ff958-v6sfn   1/1     Running   1 (3d18h ago)   20d
vscode-python-898847-0                 1/1     Running   0               14h
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get deployment
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
database                1/1     1            1           62d
helloworld-app          3/3     3            3           17m
python-api-deployment   3/3     3            3           62d
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get logs -f helloworld-app-5b9599f4f7-67zzp
error: the path "helloworld-app-5b9599f4f7-67zzp" does not exist
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl get logs -f helloworld-app
error: the path "helloworld-app" does not exist
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl logs -f helloworld-app-5b9599f4f7-67zzp
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
^Conyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ kubectl describe pods helloworld-app-5b9599f4f7-67zzp
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
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ cd ..
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes$ cd TP1/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1$ cd Exo2/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo2$ tree
bash: tree: command not found
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo2$ lq
bash: lq: command not found
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo2$ ls
CR_TP1_exo2.md  Dockerfile  java-api
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo2$ sudo apt install tree
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package tree
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1/Exo2$ cd ..
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP1$ cd ..
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes$ cd TP2/
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$ docker ps
bash: docker: command not found
onyxia@vscode-python-898847-0:~/work/Introduction_Kubernetes/TP2$







cd TP2 
➜  TP2 git:(main) ✗ kubectl apply -f app.yaml
error: error validating "app.yaml": error validating data: failed to download openapi: Get "https://127.0.0.1:60632/openapi/v2?timeout=32s": dial tcp 127.0.0.1:60632: connect: connection refused; if you choose to ignore these errors, turn validation off with --validate=false
➜  TP2 git:(main) ✗ kubectl apply -f app.yaml
error: error validating "app.yaml": error validating data: failed to download openapi: Get "https://127.0.0.1:60632/openapi/v2?timeout=32s": dial tcp 127.0.0.1:60632: connect: connection refused; if you choose to ignore these errors, turn validation off with --validate=false
➜  TP2 git:(main) ✗ minikube start
😄  minikube v1.38.1 on Darwin 26.4.1 (arm64)
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.50 ...
🔄  Restarting existing docker container for "minikube" ...
🐳  Preparing Kubernetes v1.35.1 on Docker 29.2.1 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
➜  TP2 git:(main) ✗ kubectl apply -f app.yaml
deployment.apps/helloworld-app created
service/helloworld-service created
➜  TP2 git:(main) ✗ minikube service helloworld-service
┌───────────┬────────────────────┬─────────────┬───────────────────────────┐
│ NAMESPACE │        NAME        │ TARGET PORT │            URL            │
├───────────┼────────────────────┼─────────────┼───────────────────────────┤
│ default   │ helloworld-service │ 8081        │ http://192.168.49.2:32757 │
└───────────┴────────────────────┴─────────────┴───────────────────────────┘
🔗  Starting tunnel for service helloworld-service.
┌───────────┬────────────────────┬─────────────┬────────────────────────┐
│ NAMESPACE │        NAME        │ TARGET PORT │          URL           │
├───────────┼────────────────────┼─────────────┼────────────────────────┤
│ default   │ helloworld-service │             │ http://127.0.0.1:54459 │
└───────────┴────────────────────┴─────────────┴────────────────────────┘
🎉  Opening service default/helloworld-service in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
^C✋  Stopping tunnel for service helloworld-service.
➜  TP2 git:(main) ✗ kubectl apply -f app.yaml          
deployment.apps/helloworld-app unchanged
➜  TP2 git:(main) ✗ minikube service helloworld-service
┌───────────┬────────────────────┬─────────────┬───────────────────────────┐
│ NAMESPACE │        NAME        │ TARGET PORT │            URL            │
├───────────┼────────────────────┼─────────────┼───────────────────────────┤
│ default   │ helloworld-service │ 8081        │ http://192.168.49.2:32757 │
└───────────┴────────────────────┴─────────────┴───────────────────────────┘
🔗  Starting tunnel for service helloworld-service.
┌───────────┬────────────────────┬─────────────┬────────────────────────┐
│ NAMESPACE │        NAME        │ TARGET PORT │          URL           │
├───────────┼────────────────────┼─────────────┼────────────────────────┤
│ default   │ helloworld-service │             │ http://127.0.0.1:54491 │
└───────────┴────────────────────┴─────────────┴────────────────────────┘
🎉  Opening service default/helloworld-service in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
^C✋  Stopping tunnel for service helloworld-service.
➜  TP2 git:(main) ✗ kubctl pods
zsh: command not found: kubctl
➜  TP2 git:(main) ✗ kubectl pods
error: unknown command "pods" for "kubectl"

Did you mean this?
        logs
➜  TP2 git:(main) ✗ kubectl logs
error: expected 'logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER]'.
POD or TYPE/NAME is a required argument for the logs command
See 'kubectl logs -h' for help and examples
➜  TP2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS         PORTS                                                                                                                                  NAMES
dc1720130576   tp1-exo2                 "java -jar app.jar"      12 hours ago   Up 12 hours    0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp                                                                                            lucid_yalow
44891350518b   tp1-exo1                 "uvicorn python-api.…"   18 hours ago   Up 18 hours    0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp                                                                                            peaceful_herschel
d492cf4ac56d   kicbase/stable:v0.0.50   "/usr/local/bin/entr…"   6 days ago     Up 3 minutes   127.0.0.1:54354->22/tcp, 127.0.0.1:54353->2376/tcp, 127.0.0.1:54356->5000/tcp, 127.0.0.1:54357->8443/tcp, 127.0.0.1:54355->32443/tcp   minikube
e5e034a8a18e   postgres:18              "docker-entrypoint.s…"   6 days ago     Up 23 hours    5432/tcp                                                                                                                               stage3a-db-1
➜  TP2 git:(main) ✗ kubectl kill
error: unknown command "kill" for "kubectl"
➜  TP2 git:(main) ✗ minikube stops
Error: unknown command "stops" for "minikube"

Did you mean this?
        stop

Run 'minikube --help' for usage.
➜  TP2 git:(main) ✗ minikube stop
✋  Stopping node "minikube"  ...
🛑  Powering off "minikube" via SSH ...
🛑  1 node stopped.
➜  TP2 git:(main) ✗ docker images
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B    U   
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B    U   
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B    U   
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B    U   
postgres:18                     dfee641c8b67        479MB             0B    U   
stage3a-app:latest              7e919badfc71       1.28GB             0B    U   
tp1-exo1:latest                 e72b69b21b61        173MB             0B    U   
tp1-exo2:latest                 80c921fdf3ac        331MB             0B    U   
➜  TP2 git:(main) ✗ cd ..
➜  Introduction_Kubernetes git:(main) ✗ git add .
➜  Introduction_Kubernetes git:(main) ✗ git commit -m"On repasse sur onyxia"
[main c0c10d7] On repasse sur onyxia
 1 file changed, 6 insertions(+), 13 deletions(-)
➜  Introduction_Kubernetes git:(main) git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 434 bytes | 434.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Mimo53/Introduction_Kubernetes.git
   237a285..c0c10d7  main -> main
➜  Introduction_Kubernetes git:(main) cd TP1
➜  TP1 git:(main) cd Exo1 
➜  Exo1 git:(main) docker run -p 8081:8081 tp1-exo1 
docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint elated_thompson (c544ae206696c2cfaca1057c1db77709938f0c23eab49b90ad749490a2471da7): Bind for 0.0.0.0:8081 failed: port is already allocated

Run 'docker run --help' for more information
➜  Exo1 git:(main) docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS        PORTS                                         NAMES
dc1720130576   tp1-exo2      "java -jar app.jar"      12 hours ago   Up 12 hours   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1      "uvicorn python-api.…"   18 hours ago   Up 18 hours   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago     Up 24 hours   5432/tcp                                      stage3a-db-1
➜  Exo1 git:(main) docker run -p 8081:8081 44891350518b
Unable to find image '44891350518b:latest' locally
docker: Error response from daemon: pull access denied for 44891350518b, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
➜  Exo1 git:(main) docker pull tp1-exo1
Using default tag: latest
Error response from daemon: pull access denied for tp1-exo1, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
➜  Exo1 git:(main) docker pull moonshayne tp1-exo1
docker: 'docker pull' requires 1 argument

Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Run 'docker pull --help' for more information
➜  Exo1 git:(main) docker pull moonshayne tp1-exo1:latest
docker: 'docker pull' requires 1 argument

Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Run 'docker pull --help' for more information
➜  Exo1 git:(main) docker pull moonshayne/tp1-exo1:latest
latest: Pulling from moonshayne/tp1-exo1
Digest: sha256:673d83f3fb6baafb898b31aa132789803caac110c33d922873dd6402be3d1d70
Status: Image is up to date for moonshayne/tp1-exo1:latest
docker.io/moonshayne/tp1-exo1:latest
➜  Exo1 git:(main) docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS        PORTS                                         NAMES
dc1720130576   tp1-exo2      "java -jar app.jar"      12 hours ago   Up 12 hours   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1      "uvicorn python-api.…"   18 hours ago   Up 18 hours   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago     Up 24 hours   5432/tcp                                      stage3a-db-1
➜  Exo1 git:(main) docker images
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B    U   
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B    U   
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B    U   
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B    U   
postgres:18                     dfee641c8b67        479MB             0B    U   
stage3a-app:latest              7e919badfc71       1.28GB             0B    U   
tp1-exo1:latest                 e72b69b21b61        173MB             0B    U   
tp1-exo2:latest                 80c921fdf3ac        331MB             0B    U   
➜  Exo1 git:(main) docker run -p 8081:8001 1a4b8bb2ba97
docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint nervous_satoshi (e95ea99ac1866961a2f56ad25b85612cff8c2be34d018184a1675f5bd871f393): Bind for 0.0.0.0:8081 failed: port is already allocated

Run 'docker run --help' for more information
➜  Exo1 git:(main) docker run -p 8001:8081 1a4b8bb2ba97
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
➜  Exo1 git:(main) cd ..
➜  TP1 git:(main) cd ..
➜  Introduction_Kubernetes git:(main) docker images
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B    U   
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B    U   
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B    U   
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B    U   
postgres:18                     dfee641c8b67        479MB             0B    U   
stage3a-app:latest              7e919badfc71       1.28GB             0B    U   
tp1-exo1:latest                 e72b69b21b61        173MB             0B    U   
tp1-exo2:latest                 80c921fdf3ac        331MB             0B    U   
➜  Introduction_Kubernetes git:(main) docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS        PORTS                                         NAMES
dc1720130576   tp1-exo2      "java -jar app.jar"      12 hours ago   Up 12 hours   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1      "uvicorn python-api.…"   19 hours ago   Up 19 hours   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago     Up 24 hours   5432/tcp                                      stage3a-db-1
➜  Introduction_Kubernetes git:(main) docker pods
docker: unknown command: docker pods

Run 'docker --help' for more information
➜  Introduction_Kubernetes git:(main) git add .
➜  Introduction_Kubernetes git:(main) ✗ git commit -m"Début du compte rendu et problème d'archi"
[main f8a7027] Début du compte rendu et problème d'archi
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 TP2/CR.md
➜  Introduction_Kubernetes git:(main) git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 402 bytes | 402.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Mimo53/Introduction_Kubernetes.git
   c0c10d7..f8a7027  main -> main
➜  Introduction_Kubernetes git:(main) cd TP1 
➜  TP1 git:(main) cd Exo1 
➜  Exo1 git:(main) # 1. Créer un builder multi-arch (une seule fois)
docker buildx create --use

# 2. Builder et pousser directement sur Docker Hub pour amd64
docker buildx build \
  --platform linux/amd64 \
  -t moonshayne/tp1-exo1:latest \
  --push \
  .
busy_williamson
[+] Building 65.4s (12/12) FINISHED                                                                                                                                                          docker-container:busy_williamson
 => [internal] booting buildkit                                                                                                                                                                                         32.8s
 => => pulling image moby/buildkit:buildx-stable-1                                                                                                                                                                      31.0s
 => => creating container buildx_buildkit_busy_williamson0                                                                                                                                                               1.8s
 => [internal] load build definition from Dockerfile                                                                                                                                                                     0.1s
 => => transferring dockerfile: 876B                                                                                                                                                                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                                                                                      1.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                                                        0.0s
 => => transferring context: 2B                                                                                                                                                                                          0.0s
 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:d168b8d9eb761f4d3fe305ebd04aeb7e7f2de0297cec5fb2f8f6403244621664                                                                                               11.1s
 => => resolve docker.io/library/python:3.13-slim@sha256:d168b8d9eb761f4d3fe305ebd04aeb7e7f2de0297cec5fb2f8f6403244621664                                                                                                0.0s
 => => sha256:baa1df1a3ce66ddf69aaa907923f01541b3d2da10e8072fd11b284d75cad027d 250B / 250B                                                                                                                               0.7s
 => => sha256:c841cd3d90201032366c4f50f468dce928a1f9b8f43552c3890091c01a9ce0dc 4.26MB / 4.26MB                                                                                                                           1.7s
 => => sha256:7e1c7541cbddd706165f108a82e8a53bfc4819367c8a5b34265f74cf81274412 11.82MB / 11.82MB                                                                                                                         5.5s
 => => sha256:5435b2dcdf5cb7faa0d5b1d4d54be2c72a776fab9a605336f5067d6e9ecb5976 29.78MB / 29.78MB                                                                                                                         9.1s
 => => extracting sha256:5435b2dcdf5cb7faa0d5b1d4d54be2c72a776fab9a605336f5067d6e9ecb5976                                                                                                                                1.2s
 => => extracting sha256:c841cd3d90201032366c4f50f468dce928a1f9b8f43552c3890091c01a9ce0dc                                                                                                                                0.1s
 => => extracting sha256:7e1c7541cbddd706165f108a82e8a53bfc4819367c8a5b34265f74cf81274412                                                                                                                                0.4s
 => => extracting sha256:baa1df1a3ce66ddf69aaa907923f01541b3d2da10e8072fd11b284d75cad027d                                                                                                                                0.0s
 => [internal] load build context                                                                                                                                                                                        0.1s
 => => transferring context: 11.47kB                                                                                                                                                                                     0.0s
 => [2/4] WORKDIR /app                                                                                                                                                                                                   0.3s
 => [3/4] COPY . .                                                                                                                                                                                                       0.0s
 => [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                                                                                                  7.2s
 => exporting to image                                                                                                                                                                                                  11.4s 
 => => exporting layers                                                                                                                                                                                                  0.7s 
 => => exporting manifest sha256:a91d80bee2771b0fb046416fdd8b8baad9da1109b36bcaa391c4aaba7ffc3bca                                                                                                                        0.0s 
 => => exporting config sha256:6c2ff289c16bdaa3f6b0938f5c4d13043a29a27ea2954396a77ed66d46a1beef                                                                                                                          0.0s 
 => => exporting attestation manifest sha256:82775782c5d31cb4af31a2a07207c1aa28fc37852f9c3e2b528d9b6dfd0d00b1                                                                                                            0.0s 
 => => exporting manifest list sha256:54370a2d60a343e7d67caddefaf8873e3c84ef0c4c20a5fcb845eb2cef1b862d                                                                                                                   0.0s 
 => => pushing layers                                                                                                                                                                                                    7.7s
 => => pushing manifest for docker.io/moonshayne/tp1-exo1:latest@sha256:54370a2d60a343e7d67caddefaf8873e3c84ef0c4c20a5fcb845eb2cef1b862d                                                                                 3.1s
 => [auth] moonshayne/tp1-exo1:pull,push token for registry-1.docker.io                                                                                                                                                  0.0s
➜  Exo1 git:(main) # 1. Créer un builder multi-arch (une seule fois)
docker buildx create --use

# 2. Builder et pousser directement sur Docker Hub pour amd64
docker buildx build \
  --platform linux/amd64 \
  -t moonshayne/tp1-exo2:latest \
  --push \
  .
romantic_blackwell
[+] Building 45.8s (12/12) FINISHED                                                                                                                                                       docker-container:romantic_blackwell
 => [internal] booting buildkit                                                                                                                                                                                          2.4s
 => => pulling image moby/buildkit:buildx-stable-1                                                                                                                                                                       1.1s
 => => creating container buildx_buildkit_romantic_blackwell0                                                                                                                                                            1.2s
 => [internal] load build definition from Dockerfile                                                                                                                                                                     0.1s
 => => transferring dockerfile: 876B                                                                                                                                                                                     0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                                                                                                      3.1s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                                                        0.0s
 => => transferring context: 2B                                                                                                                                                                                          0.0s
 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:d168b8d9eb761f4d3fe305ebd04aeb7e7f2de0297cec5fb2f8f6403244621664                                                                                               19.3s
 => => resolve docker.io/library/python:3.13-slim@sha256:d168b8d9eb761f4d3fe305ebd04aeb7e7f2de0297cec5fb2f8f6403244621664                                                                                                0.0s
 => => sha256:baa1df1a3ce66ddf69aaa907923f01541b3d2da10e8072fd11b284d75cad027d 250B / 250B                                                                                                                               0.5s
 => => sha256:c841cd3d90201032366c4f50f468dce928a1f9b8f43552c3890091c01a9ce0dc 4.26MB / 4.26MB                                                                                                                           5.8s
 => => sha256:5435b2dcdf5cb7faa0d5b1d4d54be2c72a776fab9a605336f5067d6e9ecb5976 29.78MB / 29.78MB                                                                                                                        17.2s
 => => sha256:7e1c7541cbddd706165f108a82e8a53bfc4819367c8a5b34265f74cf81274412 11.82MB / 11.82MB                                                                                                                        13.4s
 => => extracting sha256:5435b2dcdf5cb7faa0d5b1d4d54be2c72a776fab9a605336f5067d6e9ecb5976                                                                                                                                1.1s
 => => extracting sha256:c841cd3d90201032366c4f50f468dce928a1f9b8f43552c3890091c01a9ce0dc                                                                                                                                0.3s
 => => extracting sha256:7e1c7541cbddd706165f108a82e8a53bfc4819367c8a5b34265f74cf81274412                                                                                                                                0.7s
 => => extracting sha256:baa1df1a3ce66ddf69aaa907923f01541b3d2da10e8072fd11b284d75cad027d                                                                                                                                0.0s
 => [internal] load build context                                                                                                                                                                                        0.0s
 => => transferring context: 11.47kB                                                                                                                                                                                     0.0s
 => [2/4] WORKDIR /app                                                                                                                                                                                                   0.1s
 => [3/4] COPY . .                                                                                                                                                                                                       0.0s
 => [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                                                                                                  6.7s
 => exporting to image                                                                                                                                                                                                  12.9s 
 => => exporting layers                                                                                                                                                                                                  0.7s 
 => => exporting manifest sha256:eb1521e65cffc940baddb51316650148456475ef00e19629e7e4fdfc6f9e39b3                                                                                                                        0.0s 
 => => exporting config sha256:e3e0245f31d727c8401775381eaa34ec3f9dda184227a659bd5cc5ed7d342e3b                                                                                                                          0.0s 
 => => exporting attestation manifest sha256:7da5c8a6fa70a492909745bce7fd72b432afdca4a18d0e4a20e28a8a61a4e471                                                                                                            0.0s 
 => => exporting manifest list sha256:24eba2db4979401f13a55c7503e85b215d36134363dc2d341821672239bfd2e3                                                                                                                   0.0s 
 => => pushing layers                                                                                                                                                                                                    8.9s
 => => pushing manifest for docker.io/moonshayne/tp1-exo2:latest@sha256:24eba2db4979401f13a55c7503e85b215d36134363dc2d341821672239bfd2e3                                                                                 3.3s
 => [auth] moonshayne/tp1-exo2:pull,push token for registry-1.docker.io                                                                                                                                                  0.0s
➜  Exo1 git:(main) cd ..
cd%                                                                                                                                                                                                                           
➜  TP1 git:(main) cd Exo2 
➜  Exo2 git:(main) tree
.
├── CR_TP1_exo2.md
├── Dockerfile
└── java-api
    ├── pom.xml
    ├── src
    │   └── main
    │       └── java
    │           └── com
    │               └── example
    │                   ├── Application.java
    │                   └── HelloController.java
    └── target
        ├── classes
        │   └── com
        │       └── example
        │           ├── Application.class
        │           └── HelloController.class
        └── test-classes

12 directories, 7 files
➜  Exo2 git:(main) docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED        STATUS        PORTS                                         NAMES
5e4754f4a3a2   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   3 hours ago    Up 3 hours                                                  buildx_buildkit_romantic_blackwell0
0c24930765f0   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   3 hours ago    Up 3 hours                                                  buildx_buildkit_busy_williamson0
dc1720130576   tp1-exo2                        "java -jar app.jar"      17 hours ago   Up 17 hours   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1                        "uvicorn python-api.…"   23 hours ago   Up 23 hours   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18                     "docker-entrypoint.s…"   7 days ago     Up 28 hours   5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) docker run -p 8082:8082 dc1720130576
Unable to find image 'dc1720130576:latest' locally
docker: Error response from daemon: pull access denied for dc1720130576, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
➜  Exo2 git:(main) docker login
Authenticating with existing credentials... [Username: moonshayne]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
➜  Exo2 git:(main) docker run -p 8082:8082 dc1720130576
Unable to find image 'dc1720130576:latest' locally
docker: Error response from daemon: pull access denied for dc1720130576, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
➜  Exo2 git:(main) docker logout
Removing login credentials for https://index.docker.io/v1/
➜  Exo2 git:(main) docker login
Authenticating with existing credentials... [Username: moonshayne]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
➜  Exo2 git:(main) docker run -p 8082:8082 dc1720130576
Unable to find image 'dc1720130576:latest' locally
docker: Error response from daemon: pull access denied for dc1720130576, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
➜  Exo2 git:(main) docker images                       
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B    U   
moby/buildkit:buildx-stable-1   192ca72e69e8        240MB             0B    U   
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B    U   
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B    U   
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B    U   
postgres:18                     dfee641c8b67        479MB             0B    U   
stage3a-app:latest              7e919badfc71       1.28GB             0B    U   
tp1-exo1:latest                 e72b69b21b61        173MB             0B    U   
tp1-exo2:latest                 80c921fdf3ac        331MB             0B    U   
➜  Exo2 git:(main) docker run -p 8082:8082 80c921fdf3ac
docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint condescending_wu (550179a3f81edf65222558943d5a9c7f27d3de3e45f3daf8ed051eca42afa12e): Bind for 0.0.0.0:8082 failed: port is already allocated

Run 'docker run --help' for more information
➜  Exo2 git:(main) docker run -p 8003:8082 80c921fdf3ac 

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

2026-04-14T13:04:32.224Z  INFO 1 --- [           main] com.example.Application                  : Starting Application v1.0.0 using Java 21.0.10 with PID 1 (/app/app.jar started by root in /app)
2026-04-14T13:04:32.227Z  INFO 1 --- [           main] com.example.Application                  : No active profile set, falling back to 1 default profile: "default"
2026-04-14T13:04:33.265Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2026-04-14T13:04:33.275Z  INFO 1 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2026-04-14T13:04:33.275Z  INFO 1 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.16]
2026-04-14T13:04:33.323Z  INFO 1 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2026-04-14T13:04:33.325Z  INFO 1 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 953 ms
2026-04-14T13:04:33.775Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path ''
2026-04-14T13:04:33.803Z  INFO 1 --- [           main] com.example.Application                  : Started Application in 2.039 seconds (process running for 3.078)
^C%                                                                                                                                                                                                                           
➜  Exo2 git:(main) docker run -d -p 8003:8082 80c921fdf3ac
0e8f23d298832eb2748550bba0a27508c18ff7d8eb391ecbfa9c6f5efc4d0fc5
➜  Exo2 git:(main) docker ps                   
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS          PORTS                                         NAMES
0e8f23d29883   80c921fdf3ac                    "java -jar app.jar"      40 seconds ago   Up 39 seconds   0.0.0.0:8003->8082/tcp, [::]:8003->8082/tcp   hopeful_kilby
5e4754f4a3a2   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   3 hours ago      Up 3 hours                                                    buildx_buildkit_romantic_blackwell0
0c24930765f0   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   4 hours ago      Up 4 hours                                                    buildx_buildkit_busy_williamson0
dc1720130576   tp1-exo2                        "java -jar app.jar"      17 hours ago     Up 17 hours     0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1                        "uvicorn python-api.…"   23 hours ago     Up 23 hours     0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18                     "docker-entrypoint.s…"   7 days ago       Up 28 hours     5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) docker exec -it 0e8f23d29883
docker: 'docker exec' requires at least 2 arguments

Usage:  docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

See 'docker exec --help' for more information
➜  Exo2 git:(main) docker exec -it 0e8f23d29883 bash
root@0e8f23d29883:/app# ls
app.jar
root@0e8f23d29883:/app# cd ..
root@0e8f23d29883:/# ls
app  bin  boot  __cacert_entrypoint.sh  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@0e8f23d29883:/# cd ..
root@0e8f23d29883:/# ls
app  bin  boot  __cacert_entrypoint.sh  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@0e8f23d29883:/# cd app/
root@0e8f23d29883:/app# ls
app.jar
root@0e8f23d29883:/app# ls -alh
total 19M
drwxr-xr-x 1 root root 4.0K Apr 13 19:57 .
drwxr-xr-x 1 root root 4.0K Apr 14 13:04 ..
-rw-r--r-- 1 root root  19M Apr 13 19:57 app.jar
root@0e8f23d29883:/app# ^C
root@0e8f23d29883:/app# exit
exit
➜  Exo2 git:(main) docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS          PORTS                                         NAMES
0e8f23d29883   80c921fdf3ac                    "java -jar app.jar"      21 minutes ago   Up 21 minutes   0.0.0.0:8003->8082/tcp, [::]:8003->8082/tcp   hopeful_kilby
5e4754f4a3a2   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   4 hours ago      Up 4 hours                                                    buildx_buildkit_romantic_blackwell0
0c24930765f0   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   4 hours ago      Up 4 hours                                                    buildx_buildkit_busy_williamson0
dc1720130576   tp1-exo2                        "java -jar app.jar"      17 hours ago     Up 17 hours     0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1                        "uvicorn python-api.…"   23 hours ago     Up 23 hours     0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18                     "docker-entrypoint.s…"   7 days ago       Up 28 hours     5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) docker images
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B    U   
moby/buildkit:buildx-stable-1   192ca72e69e8        240MB             0B    U   
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B    U   
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B    U   
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B    U   
postgres:18                     dfee641c8b67        479MB             0B    U   
stage3a-app:latest              7e919badfc71       1.28GB             0B    U   
tp1-exo1:latest                 e72b69b21b61        173MB             0B    U   
tp1-exo2:latest                 80c921fdf3ac        331MB             0B    U   
➜  Exo2 git:(main) docker kill 0e8f23d29883
0e8f23d29883
➜  Exo2 git:(main) docker kill 5e4754f4a3a2
5e4754f4a3a2
➜  Exo2 git:(main) docker kill 0c24930765f0 
0c24930765f0
➜  Exo2 git:(main) dc1720130576
zsh: command not found: dc1720130576
➜  Exo2 git:(main) docker kill dc1720130576
dc1720130576
➜  Exo2 git:(main) docker kill 44891350518b
44891350518b
➜  Exo2 git:(main) docker kill e5e034a8a18e
e5e034a8a18e
➜  Exo2 git:(main) docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
➜  Exo2 git:(main) docker images
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B    U   
moby/buildkit:buildx-stable-1   192ca72e69e8        240MB             0B    U   
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B    U   
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B    U   
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B    U   
postgres:18                     dfee641c8b67        479MB             0B    U   
stage3a-app:latest              7e919badfc71       1.28GB             0B    U   
tp1-exo1:latest                 e72b69b21b61        173MB             0B    U   
tp1-exo2:latest                 80c921fdf3ac        331MB             0B    U   
➜  Exo2 git:(main) docker rmi f3db27eba481
Error response from daemon: conflict: unable to delete f3db27eba481 (must be forced) - image is being used by stopped container d492cf4ac56d
➜  Exo2 git:(main) docker stop f3db27eba481
Error response from daemon: No such container: f3db27eba481
➜  Exo2 git:(main) docker ps --all
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                            PORTS     NAMES
0e8f23d29883   80c921fdf3ac                    "java -jar app.jar"      23 minutes ago   Exited (137) 2 minutes ago                  hopeful_kilby
4151efc6f63a   80c921fdf3ac                    "java -jar app.jar"      24 minutes ago   Exited (130) 23 minutes ago                 sleepy_brahmagupta
b0f3eb92b542   80c921fdf3ac                    "java -jar app.jar"      24 minutes ago   Created                                     condescending_wu
5e4754f4a3a2   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   4 hours ago      Exited (137) 2 minutes ago                  buildx_buildkit_romantic_blackwell0
0c24930765f0   moby/buildkit:buildx-stable-1   "/usr/bin/buildkitd-…"   4 hours ago      Exited (137) 2 minutes ago                  buildx_buildkit_busy_williamson0
6fe10af874b5   1a4b8bb2ba97                    "uvicorn python-api.…"   5 hours ago      Exited (0) 5 hours ago                      sad_yonath
31ce0442506c   1a4b8bb2ba97                    "uvicorn python-api.…"   5 hours ago      Created                                     nervous_satoshi
6acc1d6b1928   tp1-exo1                        "uvicorn python-api.…"   5 hours ago      Created                                     elated_thompson
dc1720130576   tp1-exo2                        "java -jar app.jar"      17 hours ago     Exited (137) About a minute ago             lucid_yalow
b446c0db5883   tp1-exo2                        "java -jar app.jar"      17 hours ago     Exited (137) 17 hours ago                   distracted_morse
f43f4fb4d34f   tp1-exo2                        "java -jar app.jar"      17 hours ago     Created                                     eloquent_swanson
fe6b3550975e   tp1-exo2                        "java -jar app.jar"      17 hours ago     Exited (130) 17 hours ago                   gifted_williams
44891350518b   tp1-exo1                        "uvicorn python-api.…"   23 hours ago     Exited (137) About a minute ago             peaceful_herschel
7025f828e2a5   tp1-exo1                        "uvicorn python-api.…"   23 hours ago     Exited (0) 23 hours ago                     lucid_darwin
6e9f748b0d5a   tp1-exo1                        "uvicorn python-api.…"   23 hours ago     Exited (137) 23 hours ago                   loving_lichterman
0c59ec27c1c9   tp1-exo1                        "uvicorn python-api.…"   23 hours ago     Created                                     objective_tu
bf62e062229f   1a4b8bb2ba97                    "uvicorn python-api.…"   28 hours ago     Exited (137) 23 hours ago                   jolly_pike
2e7b0d8413e3   d5f29126dba1                    "uvicorn python-api.…"   28 hours ago     Exited (137) 28 hours ago                   youthful_brattain
e178c4d541e2   d5f29126dba1                    "uvicorn python-api.…"   28 hours ago     Exited (0) 28 hours ago                     amazing_roentgen
97cb98271cf5   859bfcd041eb                    "uvicorn python-api.…"   28 hours ago     Exited (0) 28 hours ago                     adoring_northcutt
40cf3c07937f   859bfcd041eb                    "uvicorn python-api.…"   28 hours ago     Exited (0) 28 hours ago                     reverent_ptolemy
dd530c2c46a3   58d8cc593194                    "uvicorn python-api.…"   28 hours ago     Exited (0) 28 hours ago                     vibrant_bohr
e434f7f44706   c208c86ee691                    "python main.py"         28 hours ago     Exited (0) 28 hours ago                     nifty_jones
61ca76942469   c208c86ee691                    "python main.py"         28 hours ago     Exited (0) 28 hours ago                     sweet_mestorf
3d3ff6b4042e   e1720bdf4315                    "python main.py /bin…"   28 hours ago     Exited (0) 28 hours ago                     goofy_volhard
3bd4a4af32aa   e1720bdf4315                    "python main.py"         28 hours ago     Exited (0) 28 hours ago                     sharp_hugle
345cd9d5a467   e1720bdf4315                    "python main.py"         28 hours ago     Exited (0) 28 hours ago                     elegant_kapitsa
fa61da15a5c9   47feaf1a850d                    "python python-api/s…"   28 hours ago     Exited (0) 28 hours ago                     cranky_williams
184bb0cb0d9c   47feaf1a850d                    "python python-api/s…"   28 hours ago     Exited (0) 28 hours ago                     trusting_tesla
fd2f2773243a   87a95002c02b                    "python /python-api/…"   28 hours ago     Exited (2) 28 hours ago                     kind_hugle
572defff5296   2be4410b3f9e                    "pyhton /python-api/…"   28 hours ago     Created                                     gracious_meitner
86cfcf85edc4   2be4410b3f9e                    "pyhton /python-api/…"   28 hours ago     Created                                     distracted_fermi
bf021551c322   2be4410b3f9e                    "pyhton /python-api/…"   28 hours ago     Created                                     strange_matsumoto
d492cf4ac56d   kicbase/stable:v0.0.50          "/usr/local/bin/entr…"   7 days ago       Exited (130) 5 hours ago                    minikube
ed1ded0ecc47   moonshayne/stage3a-app:latest   "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       stage3a-app-1
e5e034a8a18e   postgres:18                     "docker-entrypoint.s…"   7 days ago       Exited (137) About a minute ago             stage3a-db-1
a514f1281e89   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       funny_taussig
324b454bc1e3   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       compassionate_nash
eaeb897d31f9   postgres:18                     "docker-entrypoint.s…"   7 days ago       Exited (137) 7 days ago                     db
d5c74f37d606   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       reverent_yonath
583b41cfe86a   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       thirsty_meninsky
9632a8aa24a6   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       epic_yonath
2e3f3f73ac3e   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       sad_ellis
4bbf6756da68   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       affectionate_napier
fdd90ec5c89e   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       elastic_chandrasekhar
4723220573cd   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       pensive_nobel
60c94f633f74   45533a288967                    "./entrypoint.sh"        7 days ago       Created                                     objective_feistel
2952f277871b   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       nifty_hamilton
87546c3624a5   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       wizardly_dewdney
17fa7020fbdb   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       relaxed_swanson
43ba16ec67f2   45533a288967                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       brave_borg
96bf0d206c81   835ac51b37e9                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       serene_khorana
e35d1dca7cf4   835ac51b37e9                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       agitated_carver
93c12e94de9f   ce509c783483                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       gifted_dijkstra
34e3ace0ffa4   ce509c783483                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       peaceful_feynman
fc0f98cc00da   ce509c783483                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       happy_germain
1c2ce1cb7b61   ce509c783483                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       modest_satoshi
3389fbca44b5   62a874c0bf89                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       exciting_boyd
00164a6c0dca   62a874c0bf89                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       epic_shirley
6d4dec3bed69   62a874c0bf89                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       vigilant_euler
0964ca399518   62a874c0bf89                    "./entrypoint.sh"        7 days ago       Exited (0) 7 days ago                       gracious_wu
858c2cb3acc8   7e919badfc71                    "streamlit run app.py"   7 days ago       Exited (0) 7 days ago                       upbeat_keller
b1412e7d6315   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      dazzling_hopper
a0d786db72e0   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      upbeat_thompson
78f0663eeb16   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      blissful_diffie
d13cc0653f81   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      relaxed_hamilton
af78fceb4f7f   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      suspicious_pike
2ab8a10fe26a   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      beautiful_roentgen
11c4899fb114   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      flamboyant_khayyam
79c86f10b677   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      nostalgic_tesla
80c88e532e68   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      gracious_satoshi
7f0c6fbb63aa   7e919badfc71                    "streamlit run app.py"   10 days ago      Exited (0) 10 days ago                      cool_cerf
39d64c06024a   7e919badfc71                    "streamlit run app.py"   10 days ago      Created                                     pensive_almeida
d9a94a7d70c2   d9fe86493f28                    "./entrypoint.sh"        11 days ago      Exited (0) 11 days ago                      sleepy_nobel
ae9daad6c108   d9fe86493f28                    "./entrypoint.sh"        11 days ago      Exited (0) 11 days ago                      infallible_torvalds
e6f29846c2dd   734680c9ac1e                    "streamlit run app.py"   11 days ago      Exited (0) 11 days ago                      vibrant_pasteur
4b13f56b6be1   734680c9ac1e                    "streamlit run app.py"   11 days ago      Exited (0) 11 days ago                      jolly_rhodes
4fb334622085   7e919badfc71                    "streamlit run app.py"   11 days ago      Exited (0) 11 days ago                      hungry_lumiere
dc6aabcc7514   d5963c7f0849                    "streamlit run app.py"   11 days ago      Exited (0) 11 days ago                      fervent_pike
3bd98d7fd2b4   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (137) 11 days ago                    musing_bhaskara
3b6386a2ff1f   7e919badfc71                    "streamlit run app.py"   11 days ago      Exited (0) 11 days ago                      blissful_boyd
5424bab0ad3b   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (0) 11 days ago                      pedantic_mestorf
961dd49d43a7   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (0) 11 days ago                      zealous_leakey
6c5caffe5e83   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (0) 11 days ago                      clever_ptolemy
897f04526b0e   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (1) 11 days ago                      loving_swanson
a48a269fe58c   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (1) 11 days ago                      heuristic_leavitt
15102035f990   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (1) 11 days ago                      confident_grothendieck
ae798154dbf1   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (1) 11 days ago                      gifted_volhard
9a9c48b5cd91   dfee641c8b67                    "docker-entrypoint.s…"   11 days ago      Exited (1) 11 days ago                      priceless_almeida
➜  Exo2 git:(main) docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
0e8f23d298832eb2748550bba0a27508c18ff7d8eb391ecbfa9c6f5efc4d0fc5
4151efc6f63ace99cd92b4572682701ec54fcc861b4a3b1a3855e43e770546b6
b0f3eb92b542d321c4ae6e6b487afad1201242527feebfa6a4d469524adb7472
5e4754f4a3a20c4fa18f431ff9422f1e8f1e9cd7a20ce870fd58d6c5d71923a7
0c24930765f047b850fa5bc316121b1f8860c89bcb230870339b2a3465a71388
6fe10af874b5cb41d8ae664a3b31da8815e382848fc2d903334b5f488be02dd2
31ce0442506c88073d6cb37d73d50fd220c6d2d97b267820ff5465476aa6af2e
6acc1d6b1928d66ca665e27339dcd0eba4a89f9cf4281680edd91bc5ade62f20
dc1720130576cd748db60bb65f1857591501b4926739787242d07acce6ee4a4e
b446c0db58834f8d57ce3a1e8fc7fd52f0fcd3bd1c54b230272448ca7930981c
f43f4fb4d34f0eddabd2b8a0d078948c1016cf3c5c2396e6cd2944341847f905
fe6b3550975ed8094d938b8a923f99704b9d64c7724ac05f5dbb412486d903df
44891350518b34d4014dacacc1153a6499f5fe73e4ba1365eb6c734bb8cc9625
7025f828e2a565705a47255b603eeb2f2785fc19bd4d3dba7619e41c7ccd23b5
6e9f748b0d5a034b015a3ad2a60c1bb4ab53f9fec72760d4717492e19752e7dc
0c59ec27c1c9a98afbdb398a9087f9f1878b16126be76fa2a2094edd494c998b
bf62e062229f3e6de2cb099b2dc1a6661cc04a207e610b083ceddf8c07e322c2
2e7b0d8413e33e1d1d98afc417bc047adedeff7bccbbf56f4a1054c600b17a0d
e178c4d541e203f20c334d4aef87ea344579de8f6b859c3f0fb51c872b5068e2
97cb98271cf5ba136cac69712c894c8aab56358cc788994e0ea1f451942c0e6a
40cf3c07937ffd0e627b05507caf35279750b904ab6d801a0a3d7f580ba39315
dd530c2c46a38e78af7b33c8e54ad25f2ccee1e594b851c0d45ddc792ea8215c
e434f7f4470672673fb0c8a5124297a4ca7250532221389acfae4457371ca671
61ca769424691d3e4e85b984d1bc678cf9869219a77b6f25e7dafcf92aa0d119
3d3ff6b4042e84660ad9ad952bd75277cb6bd2c5a047b54bdc1e08051c3273e6
3bd4a4af32aaed6c1711c6b2c1623bce71d86d93fcbf8c907f9079e8e632f140
345cd9d5a46749004d8ee50d6fdc03e25990352fc7a7f73fee95d6465411605b
fa61da15a5c95e2673cb08cd441871dcf484bad800c6d1532343b21830c1107b
184bb0cb0d9c4b6b6bfec747d251d7a1d94a571b083e28e4efcf4734adaa054b
fd2f2773243a42fa318a52edb00ef955450a8636b823bc9ffad59a358a159c0d
572defff5296add055c7671441858821b4064c9c6ecf9b3db2dfdb6db5d91422
86cfcf85edc48ff9f3de164483abe77cf3fa3fe0c193ff35b43a31d379f95d15
bf021551c322d8270cba6b8a3fc55c321c049c84b34ebfaaa9d4ee2cf4ca13e3
d492cf4ac56da6547a1115379caa3020adc65ed60c2eceb1bc4de7ba0e3198ee
ed1ded0ecc47a9e87465f270019aff6de4d788f0cf65a604fb0ae20bc5c9b408
e5e034a8a18eb17dd51549741ab5530c843579adde47cb317cf04209c4c62661
a514f1281e899801dbb2fb75e67f798a594db61812880bcbc42b0f9428799fda
324b454bc1e32ab815af5fa966d7824aa5c3554e290e7ac9682ba8b2c05c2093
eaeb897d31f91c28b804bcc631426f12088eaa79df56a698f9f989eb4c9611c2
d5c74f37d6065e2549b40300ac15f026df3cfac0421e83e3bc8c799d9afbf927
583b41cfe86a7567408463066034c74aa36be34247a279b2e4675b0dcd92cdfe
9632a8aa24a61b6eee2e7348e3773dbf4ee06738a465cfc81912acc1c1b3129a
2e3f3f73ac3e44ddd75705a0930df128053b57304a1801c1f990ca36764d49f9
4bbf6756da68b50d384efc26a00c3431b73c99217b764c16b3da5423524ef2a6
fdd90ec5c89e268a1d207d0404fbe56ac2239e9c23dca1c31448589932a17b3a
4723220573cda0af318566124a3a27e452c641e2cbee214b5809956def9fcbc4
60c94f633f74c5229f691c3a7528c0e3fad8d20aa2d9c339795c8509440e1e7a
2952f277871bdbd3e6b0bcd5281a00c0dc043876d722c5ed9a56f64a41aecb24
87546c3624a54b02f2e01ccb29d35d9066126e6985b689112aeccb2773871f8a
17fa7020fbdb30c4f7313d1e1cd049ddf52884912d2e71ad70de515c216f60f8
43ba16ec67f20e3cd2c8f7bc93ee37400d37e56dbbab44f616a65d4c63f193d2
96bf0d206c817d24ade149c5591d8fc7be23b76e32d24ca75c5afeff839e66ba
e35d1dca7cf485ee883c3494e4c5db5b973ac87bc0df8ed1380c74a081a016b9
93c12e94de9ffafb8c77dceab2c3df5a08d40ea3b752f95a3a6b8fa9c3d63d04
34e3ace0ffa4be7ffa7e53a088e5eda5331ece059c95e416b08c8d06ffb315f1
fc0f98cc00dabc4a2655db98a3ff2d1fc16d6b854886a42289e41f1f795c7870
1c2ce1cb7b61064acf40df9b4d57acf338d547a9bcd20578dc74ceb3f573078d
3389fbca44b557bbc5d3926aaa2beb9c497d8823b42e62613a39e58c69c5a9ea
00164a6c0dca2f78d4abda26e8531ea219a54b32142cecd176c858fda27affb4
6d4dec3bed693c57c09096f8d615f739a4020c5a4b01d61592b42bb203f03ff1
0964ca3995184ef65871c34ce4ccd00bf9a4e58b9105025334544039ae227cc0
858c2cb3acc81167699e2e0a32b9486c74e07255838592d3f83f098f13d37b2f
b1412e7d6315e556d26e8a479b9d3ddf9091e4176abfccde88a0b7646219ffbc
a0d786db72e097d75a06c8f28395c509d66fe27fbf27efcbce3b38338518e959
78f0663eeb168103d69bb4713280e0f80e697295fd829e6628e382226ea34ee2
d13cc0653f811231c1efb787a2e9cf788c9b734e3f54b00e00469bdf328096d0
af78fceb4f7f3f9f4352ba968e8012b49cdcc5fbfd81a8f53c0fb1153ef1c70b
2ab8a10fe26abf14077ef338248f6a15e65576bd613a202a8ba6c3ecf41baddf
11c4899fb11427d9ac5856cccfaf770938b31df5ae7ef5c302eebb866508ccc3
79c86f10b67775cc808e833662292421510dc866707250ea707525859160e72a
80c88e532e6834f6ed164c0e841592cacd9c8fc3ea1a0643ada4404b313d711a
7f0c6fbb63aa6a649fb4c933fb3c700e98f02ef38d4aee1773ff6f51628720c2
39d64c06024a4771a80a472b630ded6adef9e01889ec2f6ac15884fb5fa69c99
d9a94a7d70c2943f706c78ff6a139edc8bb2cb8ac622e57bb76025349bcc240e
ae9daad6c108f48f5e3c694c754c13abfc796c3693980ae0e6b3fc36522e7cd2
e6f29846c2ddf4d997b345a0349e7fca6e7f848f0810227f4deef67cc672c09f
4b13f56b6be107db052dce432014625debc8ca9c48520e499c7068fb463e2240
4fb334622085dd47152770a70b3bfad1d7367a1d18a0f96a4f0b308a4ba43f87
dc6aabcc75143a697bf56bb0ba4a3084a6f67d269188d3d9ae2eff35e74f13ac
3bd98d7fd2b4cfea991df18531d6f80392cf3c652a6c33fb76de30238d4bd8a8
3b6386a2ff1f15e32970b57931d1cbaa8910a8180ecae63762aca6ace21bfa42
5424bab0ad3b915690718faebedea2ae60a531523fa21f7c4c690439b8422c50
961dd49d43a7950e4051d026283db7d396b7b3773814c56250a8f82748651826
6c5caffe5e83734c38e531b8800ac701ff1c023cfbb2a4ee2962fb84cb32f458
897f04526b0ea4700290249f0d39abbf835c79c38026f1493f91254c7617ca69
a48a269fe58c88f3aa1dfe3819be0c23ca79ac30309c1b35d4f552a35c1abcbc
15102035f990cfbc81d4769bc6adfaca2c0ef5fa633eed45a04dc31f248fa286
ae798154dbf161d00bf79adf7d40f2c193d0378c46f4b195b2ecc8b47b2358a4
9a9c48b5cd91c1939562f45053b2963037d2a5874649eee08fd79c6ba6257aed

Deleted Networks:
stage3a_default
mon_reseau_perso
minikube

Deleted Images:
untagged: moonshayne/stage3a-app@sha256:5375b29d752f30ba38979020bf5e939e2ed1cbf8573b1ede8742c9d5f060b296
deleted: sha256:d9fe86493f280320c730caa9b685450289a5be5e828a85020f6ec6b7d81cd590
deleted: sha256:9dde48369e0eaf3865e826ea2db253fdf14648285fad159f44347c0ebd974071
deleted: sha256:d1828221760f9a84bf2cf42c706c0b763e2c91e10da65cd88c8bc96c9f7e93e3
deleted: sha256:271c582e9fac421f66315f7fdb9175a26f54afbb9e413e14b64e3cf862e75269
deleted: sha256:b648e3b38b43b76d029e7f148380b92815b8768d75af817856030a16fef6fe37
deleted: sha256:b4d07a89839880b28c68df0296760acd84a8291ee35c3afba867153da6bba736
deleted: sha256:a8b3def6a28b282d960a45b25cd3fc5b706f520c6205421eb8dc9d219d8005aa
deleted: sha256:45533a28896778e09b91607f67b9298977f17d6b29a8257a0558b4e46e75d005
deleted: sha256:47feaf1a850d819955b5e485d30caa3fd69fff7ae0f260ab975f23bee195a23f
untagged: moonshayne/stage3a-app@sha256:994405587e6cab0dcf05506289770b57915a62e22adaa62953e54d5aba83535f
deleted: sha256:742db57527cb96bf5e20d6aea5fff7104cf6de98db8718d819d601caf90ed867
deleted: sha256:646be6b8cb5bb7b4e61144b7a6399b7c644dcbae4ffcc2b1700519c221854270
deleted: sha256:8793351af12a0c3448807077c9f2f3ed33803628c9cafa6dbfde997dd4346fb7
deleted: sha256:6f1743a5b4eebc2afd7e4af65ed183c761db0979eae03f173527daef5fb3edca
deleted: sha256:d460c03c909113fb47f3427a16cc8331a346e6177f75654007a44bc3499d3077
deleted: sha256:b9df8026844a593f36930074b34aa20b9d26c0f47b8c34ebf9d9e719ec5578e6
deleted: sha256:2ff79e4ef5ec5ffa1e78df4466f68d45969379099b759b9dd3ea7788a0cebe38
deleted: sha256:58d8cc593194fc6c61cb22adb1ec1c0168cf0d89ca615b6e8803aa8a88e2ce61
deleted: sha256:d5963c7f0849ad46f1d97063f811a3b5587aad12d1d15c6602a2947919e06ffd
deleted: sha256:8381a60b9a60498467989569a4c4a685f9a9d446824958d84e4f171bb37746c7
deleted: sha256:d5f29126dba176e1477157df6072a569c73cc4b78ed20b9d9e6c9945b9af999c
deleted: sha256:c208c86ee6914afc403902b441e5789962e383cdb982c9c1a181ac6578d998c0
deleted: sha256:e0ba948f4a6a1fe99a7ccc519ac7ccdb019b65010175d1c48c0b13786f4f6a11
deleted: sha256:e1720bdf43150fb43400dcd026e9a823cf254813ca8ecab0b69050bbc4e75af8
deleted: sha256:70bd3c493d31bdce5ceec6cdb685d16b5bed277842be25c51b5cc7be3f60fb2e
untagged: moonshayne/stage3a-app@sha256:f7b132a94b0b2a7863720c1acf081309ae0f49256b5ee1af62dfc3fbcf4ddeb9
deleted: sha256:6af8bebbfba12c299943788d69dccb4c0fc29560530592817ca1ec71c785fdb0
deleted: sha256:39ea9d9fd919291346d6d9874b1f94a62f834eb384ae04c9f82a812b086dab45
deleted: sha256:5840940f611082281eea779efced721d0e4daff6a8a8bfe82a55e33e401ca8ac
deleted: sha256:6f7036465aac1d0999b7b2c44bf1eabfe7b1f47117eb2731d285efe05b5c6d6a
deleted: sha256:66cfe0c065e0380f97782253e07cd6c8f7cf58739a3fc30b9d0cce1c27b51589
deleted: sha256:b531b01ea7ea537e51d793d948106f917614dea9923c63f117bb26f803f279ad
deleted: sha256:94fa8f5d4a19def884f8368614776d0a6d782e6d6b75ffec9df39e94ecc9c596
deleted: sha256:859bfcd041eb6f6fa1d1aeb99cc579f42e60ee01a8c9af65f39a0a314d64adbb
deleted: sha256:e272c0fc552ec62160d1bd3577b927a8c978cfa03e82935424203322f4e69f9f
untagged: moonshayne/stage3a-app@sha256:044ed4e7b80df70b4e20d7e364d0255398c19302a2fbca9163909cbdb84fa3a8
deleted: sha256:95e7d9bf15f43ce2126294e1139625a120a39db615ffaab0c41ee0fb84c87c23
deleted: sha256:4ce865dcf5295b7b26efca8a609d9654a067232f194345401be962f39d15c91c
deleted: sha256:74046968719b24ae30118e48d2def88a8ffb7fb94215c00458d93c01447bb243
deleted: sha256:65a7be3b632d589ed7e8d4e85218bc7c8b57fc6509ca3dbd8b5a5bcd7fb43f5d
deleted: sha256:4e7390cc75e6aed42c73b88d9cb5eb51137ac819d8d2670e93d8b118e31a9c9e
deleted: sha256:f21dc8330b07282aed7fd82f3e29caee35be8b79d68208ca035d88b237271060
deleted: sha256:25ca551cf6ab8f33eba35736aeee201dc2974fe3acf7f7024a4e14612c4de06f
deleted: sha256:62a874c0bf89ee691364d825e4012cee59cbde7021a3842236b0826c4d444685
deleted: sha256:1d4ebf7c1a395e044ce94e6bd7a45f7cbb0c26680fb5efaa708803a462ec06fd
deleted: sha256:2be4410b3f9e885662317f3377e2469092f9490bf6ec1dc9fd16c7d8c8fbb4f4
deleted: sha256:87a95002c02b3185b97057132dc8807d9db985e3628324eb0f18862ab5107595
untagged: moonshayne/stage3a-app@sha256:91e8a57fbcf05957d00b0a9530ceecd7cba287ce8ff59326ff72be1fb1f04083
deleted: sha256:734680c9ac1ef4f1285d3d3005f74ade53530744618f04e282cfa6cc39cf513b
deleted: sha256:e77ad3d78570fdcd76a3f32b28219b0101aab17eadaf28f6909ffecb0e499b37
deleted: sha256:e3c533b6e3035b21994b7a4d2c75b5e10d39b3fea707a329fe9aae6feeb35e70
deleted: sha256:9be92801cc59ff139f5c69fbb23bd290420b0521e5a973b78e06577c414c5a05
deleted: sha256:7f1fcd53cdc872c5377a3d819cf1961cc61e3f015484124120ab86b7e0f983e3
deleted: sha256:246c1c0ec419fcacf47bdfeea9f43fdf73b2f74a13a23b404bd0e16fba278477
deleted: sha256:0b7384932f021f3d979bb7bb2ca9f7968896a887b4697f58430cea27a082b2fd
deleted: sha256:a3a43bb2556ec7f977473bc7398bf8815553e6085e7a39cdb9e7f069c2f0e68d
deleted: sha256:70337aad7db388323fec47ff8d2cf2e21e5f11369fd5884867a33961658afe21
deleted: sha256:1e0588de697a91a82bf341f82eb33c0580a4667a2feb858317ac5a0cc1a2b8d6
deleted: sha256:d7c97cb6f1fe7cae982649e9f55efe201212e8acaa64bd668c083b204e4efd4c
untagged: moonshayne/stage3a-app@sha256:2ab5dd46f506db160db078f3b5cae451e8b4f8de5e51c288105470ce842c2ac1
deleted: sha256:835ac51b37e9206acb1fd0cb2be24a2a0f8161c14164254b7fff7af66ce5f012
deleted: sha256:53962e7c0e6ca99ff80aa3f3ab94fed7784f7541a9fd4383648b3850779f57e1
deleted: sha256:1dc0204bd035d6444ff0d812bf8f4f4c952efd8cc66ddeb8ce15283e225d1eb8
deleted: sha256:901c50408f57f54cc74b37633e40be46073a048fecc69fddd5873f0d8e03e272
deleted: sha256:e90066e35801347b13275ac7ea3e2f6f508f1fcbcec5b0f0cd72a23f1c90d112
deleted: sha256:8596b82547922d4ab2053aeed256d9f0607ecc927f33db9075a3be4242db6ffd
deleted: sha256:3b3543fc767dd0f3a02f73654fe65481615a3cd21a7eb4bd894b7e868632a986
deleted: sha256:97991f1056465a9d33a32475bd725036ce793078e1f502bd8fd9e9dd7752819d
deleted: sha256:bea3125a05a6cb0cadb5a70e6b9b5a7b96c604319179e66ee01f79fbcee43419
deleted: sha256:141e6d6ad5f43278e785a03f94c0b56270953c3333e2731d176b0aaef56d53ed
deleted: sha256:60e70dddd9ea3b1c77c62fe78be1d9f485706b6fe6052c3d88612bd8f56acd67
deleted: sha256:3a40f90b77e8362f12aba1a18706613e5f254cd155d18bc6f464b67634eec891
deleted: sha256:ce509c7834831565a8750a5624724f20d897b73ce52571c568c86f1376765e8a
deleted: sha256:6aec3647634dfff78964c52d709e59eb664b47ae0cd2a5227dbc857d0ee5b690
deleted: sha256:20da32e29b6a6db13e6779f03568ca319f32c5a3443d8d85d1746f87875a00ff
deleted: sha256:46d79c9a957fc803f2efb21a791952249eec74d481bc201abd950209ed7523a8

Deleted build cache objects:
9b9i6x9y0hq5n1lcae5tzmyiv
y608siei72r5czw471lpjogzp
v20mjqub6q54fb9o9rntcof7k
q4370ni1kcjtutunsqwniu8ni
nmsirny0669qf2nkcwevtjfes
w1tdkz1adh9hph4zxkj0rchdz
1mxysgz2fz6rhw0j8fig9pvm4
zeqnnt77q5snrdfqms6qpnhn5
jo6fmux5tj5ni0vai3ujhlz0m
2u5f406fgnctgc04xli0s81c8
sgfv2qc6cwx2erhfrduxpt5kv
d4iia9wzr0tub7du59aprxzwf
jkmz4a73jtrjqrpdayqpdmym1
osiff0orefql12wvkvy2k36fg
v49oixns9qxr72qkpzakoml9e
vcmwpkeke0vv81nzfhkhuk0u3
w12n1qpqjnihy0usk9lmou5p6
jia5yq38s88exnrq6txeeu6m0
x5ebv5qcdc7fbhz3ofqbfxisq
77t2ke4lygpawai6i8jin3nar
mget36xr99u7szm97w5bqplx2
1e1yf8w757xbdam2hdwm86opx
pgpadjk18aa0hz5etrczb9l7f
wglhsdtyb0mkj8ym238pr7h5l
3ys6hzdrf9zxo2cyp0c9j5q39
mys5n9h3wzuuqoj79ikqft884
b88khwrqvrs30xlf6g7m8039k
dycv62qxr8apriehpdgfwnxo2
uo720arydnh9x5ppp2vrza3jr
juvwhlz67rdd8yolxa14sti0s
jxotxtmn7bpmba1a3nrjqzpka
ypyyun09uphxmpg4pkcfkzx0x
ikqt5bcc6ntdur6jbcnn30d7i
s1y7xqdcaszhl84hz8zvpyrnk
svc068fr0ot9lpfrz5bzfnfeo
0h4lmesu2mfefsdw8c76gxle9
cqhtev024v6c99fqpsk8svsy7
ayen6tqegy8tddlf0gtmaaed0
dlduj1q0hn5zctn2l36caxz0r
vytpr9057qkeslxf2r6w9ddy8
scoejzzsghgaoj98zbj2lbsgt
0khrcvmk43dgwbt2vvt14lx0z
rn5wqio3kp8hkg91d7kk7nkba
owqxvc2uqpp8lvugujr16pjnc
vq6tjlm5hxezezol15l0zi1ss
vrn43iddafjyaur08qtxo1coq
i8rjgwoh25vvvto3agoxxp31t
wupfyjn0a9otgo2phdi2xsko5
89r08jxbnjt3h1066qfnoau3t
zceo1w9bhtws65pp1zvmas9r5
o9u56nglmh10ox41zmgywvmqd
p7yrdbowghi2yu6noc5cpk58e
ja6z1znr1oq60o69fzzcn9qr6
zo1xx7afddhhin4ms61mjfv84
o49v38yfy4unixsfnk16bc9l8
okq67hq0xbx71hs97ew2u26ll
3kvwnoc6crlza9b4kfn3b3hq1
sdm2lm6wq20wnyrcpineeo12o
qaj0t8vo6zq4l2hotbsvfevae
z9v1nda1uf2we5s46a4usivbp
x1cv7qnt4t9qa2l2c3vjgg1fv
72acb7j7uwoq1g1gry7e2hc5s
mvnliiwdlu0t18dg28k3jpqs4
r2wqlknkkkltckbwb5nvfq051
s03brwj2xwkia942stqx97fyj
y38q8cposofjxqb0yx3m7cabl
q53hozco6bubj599e5vvz98af
lb4tcc6kjlsi0dmmu1lm9up1m
vh82bpgu8g5kf3cvikws4fs72
yem4fov46rphm23jzwdzmj0c0
87cl3dkch82v1lellnmio1cna
mmr0k42dm3kdzbifao0wq4pio
70yff14pxhpmetfjjxaqhwlcs
ikbs1f5kw1e8x2fh3zkn5uc6u
m036vqgw1snhmtl5aqq9o91bz
6li5uaq8ta6li4spaj4s06mtw
cpdizdpji6snh4moj173tvy62
s2mpj2wl7718f36zpcguj0ujz
pcsnd1s08kjnvtyx4r68ex3qs
qsynuseg5dqr7jwit4aiexhxb
0ezknqt0co4af3l7wsowrmeuv

Total reclaimed space: 6.506GB
➜  Exo2 git:(main) docker ps --all
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
➜  Exo2 git:(main) docker images --all
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                           ID             DISK USAGE   CONTENT SIZE   EXTRA
kicbase/stable:v0.0.50          f3db27eba481       1.35GB             0B        
moby/buildkit:buildx-stable-1   192ca72e69e8        240MB             0B        
moonshayne/stage3a-app:latest   46bfcdee27ae        760MB             0B        
moonshayne/tp1-exo1:latest      1a4b8bb2ba97        173MB             0B        
moonshayne/tp1-exo2:latest      80c921fdf3ac        331MB             0B        
postgres:18                     dfee641c8b67        479MB             0B        
stage3a-app:latest              7e919badfc71       1.28GB             0B        
tp1-exo1:latest                 e72b69b21b61        173MB             0B        
tp1-exo2:latest                 80c921fdf3ac        331MB             0B        
➜  Exo2 git:(main) docker rmi f3db27eba481
Untagged: kicbase/stable:v0.0.50
Untagged: kicbase/stable@sha256:eb4fec00e8ad70adf8e6436f195cc429825ffb85f95afcdb5d8d9deb576f3e93
Deleted: sha256:f3db27eba4816f2db25b544cf584151da4c765d875f9146f7649cb467909411b
Deleted: sha256:4624ac991636b3dc1de1b0251eac639f39ce17a98154e33a7abd85612c4c7a7a
➜  Exo2 git:(main) docker rmi 192ca72e69e8
Untagged: moby/buildkit:buildx-stable-1
Untagged: moby/buildkit@sha256:0039c1d47e8748b5afea56f4e85f14febaf34452bd99d9552d2daa82262b5cc5
Deleted: sha256:192ca72e69e8c1d69a72ea56007007c6aba99d3f3bc86ead7951207b8f71ec3d
Deleted: sha256:b1f66c565da2150204ad5a2270cad71f3b897ca01270a0e973104f6e64dd33e9
Deleted: sha256:5acd1ca932d3e3544271d6f29a5dbc77830d259ba3d12b7870331b13566c54b6
Deleted: sha256:8388aeac1fa505c6e7d9ea9010606f727701f50f403f4c174cb2edb55987c944
Deleted: sha256:1770961e8017f6078443a469f651895077ee75582da9513975b0a9dcbf4d47d1
Deleted: sha256:6b4befc5f7a7ee5508b466f21aebb47e8103942265d1113229cb7a260e07c1d9
Deleted: sha256:960807336d2f4f45befabc887ed65ef690e2154d7f93006c66f41c76617590d2
Deleted: sha256:45f3ea5848e8a25ca27718b640a21ffd8c8745d342a24e1d4ddfc8c449b0a724
➜  Exo2 git:(main) docker rmi 46bfcdee27ae
Untagged: moonshayne/stage3a-app:latest
Deleted: sha256:46bfcdee27ae3480a266af45a9cc4d4e0cdbbd62e7157aa6f5c18978104af3d2
➜  Exo2 git:(main) docker rmi 1a4b8bb2ba97
Untagged: moonshayne/tp1-exo1:latest
Untagged: moonshayne/tp1-exo1@sha256:673d83f3fb6baafb898b31aa132789803caac110c33d922873dd6402be3d1d70
Deleted: sha256:1a4b8bb2ba9712462d5c70cea4be148608043ba20f8c2e7a97accf5a7caab738
➜  Exo2 git:(main) docker rmi 80c921fdf3ac
Error response from daemon: conflict: unable to delete 80c921fdf3ac (must be forced) - image is referenced in multiple repositories
➜  Exo2 git:(main) docker rmi dfee641c8b67
Untagged: postgres:18
Untagged: postgres@sha256:a9abf4275f9e99bff8e6aed712b3b7dfec9cac1341bba01c1ffdfce9ff9fc34a
Deleted: sha256:dfee641c8b6719541e843300d13ce6de986ef764f012a59db21260fc09f77b69
Deleted: sha256:e1de1ed3bc126117920b70d73f2b4b87633482ebc7f8355aefa2216c52d3a445
Deleted: sha256:d8f5d86aa453f06cb6e71331cd33c25ef3fe99a449d10c17cec25e83a841a939
Deleted: sha256:011816b24b49dba260e23b6a168025584bee2bdb6afc688d7a669f5b0c0a1a1e
Deleted: sha256:3a836cf972564ab088756146bc829313080076a092119465a648f7eef5cbe8ea
Deleted: sha256:4376a6083b4d5d440dedd5ff5755c82d9df37b0f442c3396a7ca6d4517ddd039
Deleted: sha256:9a057251a5cee823de08e9dbecb30bb8b173aa6eaf375eb0a366de6c48f48469
Deleted: sha256:adaa47485084b1b8ea7e4034c6655f0f75c802eb18fb669a46b6e96cc207d0be
Deleted: sha256:708bca2166a90a755a57e0b8c14ae15f0001d1b4fbde1f37c5323cf2fa345179
Deleted: sha256:3a51b63e3e33ff82d3339e6654487a4b118d8756d86b1855e1ad32f40094522f
Deleted: sha256:2aed339fd36aa4df0211f5f0c3e2f2995c7c484105b59b87c12188bb0873cf62
Deleted: sha256:d195166ba968e70e60fc8dc14e02af1da924410c781b0cf583de034f4be80e5e
Deleted: sha256:076bd72dcda33c24548947f217cab7d82761d1ec00640bca6922513c191e4f8e
➜  Exo2 git:(main) docker rmi 7e919badfc71
Untagged: stage3a-app:latest
Deleted: sha256:7e919badfc716a7f13bafcf2691720298d64665f5ac05198ae53b23aaf9cd3d6
➜  Exo2 git:(main) docker rmi e72b69b21b61
Untagged: tp1-exo1:latest
Deleted: sha256:e72b69b21b6188f4dbec8b38a3533382f21365efdd3ee5a823db611d87563637
➜  Exo2 git:(main) docker rmi 80c921fdf3ac 
Error response from daemon: conflict: unable to delete 80c921fdf3ac (must be forced) - image is referenced in multiple repositories
➜  Exo2 git:(main) docker images 
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE                        ID             DISK USAGE   CONTENT SIZE   EXTRA
moonshayne/tp1-exo2:latest   80c921fdf3ac        331MB             0B        
tp1-exo2:latest              80c921fdf3ac        331MB             0B        
➜  Exo2 git:(main) # Supprimer les deux tags un par un
docker rmi tp1-exo2:latest
docker rmi moonshayne/tp1-exo2:latest
Untagged: tp1-exo2:latest
Untagged: moonshayne/tp1-exo2:latest
Untagged: moonshayne/tp1-exo2@sha256:5ec612dbf111d256cea2a0fcd8052840411d8edba3a35767e2e5e277528972ad
Deleted: sha256:80c921fdf3ac6e3e1901c76ebf6d58235de53988563e30da0e071c1f4b9e027b
➜  Exo2 git:(main) docker images
                                                                                                                                                                                                          i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
➜  Exo2 git:(main) docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
➜  Exo2 git:(main) 





