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

# difficulté rencotré : 

Sortie de mon terminal (à retravailler)


cd onyxia@vscode-python-166697-0:~/work$ cd Introduction_Kubernetes/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes$ cd TP4/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
ERROR:  relation "reviews" does not exist
LINE 1: SELECT * FROM reviews;
                      ^
command terminated with exit code 1
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectrl get services
bash: kubectrl: command not found
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get serviced
error: the server doesn't have a resource type "serviced"
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get services
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend                ClusterIP   10.233.51.125   <none>        5000/TCP   48m
db                     ClusterIP   10.233.9.248    <none>        5432/TCP   49m
frontend-service       ClusterIP   10.233.34.156   <none>        5000/TCP   48m
helloworld-service     ClusterIP   10.233.38.163   <none>        8081/TCP   53m
vscode-python-166697   ClusterIP   None            <none>        8080/TCP   66m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-86cf5dd779-96d9t      1/1     Running   0          40m
frontend-app-f9767664-cxw4p       1/1     Running   0          43m
helloworld-app-56988bb556-76r25   1/1     Running   0          54m
helloworld-app-56988bb556-7hjdt   1/1     Running   0          54m
helloworld-app-56988bb556-8jv7l   1/1     Running   0          54m
postgres-db-0                     1/1     Running   0          3m35s
vscode-python-166697-0            1/1     Running   0          66m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl logs frontend-app-f9767664-cxw4p
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.115.155:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [18/Apr/2026 09:09:41] "GET / HTTP/1.1" 200 -
[2026-04-18 09:09:59,761] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 175, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/connection.py", line 95, in create_connection
    raise err
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 723, in urlopen
    chunked=chunked,
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 416, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 244, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/usr/local/lib/python3.6/http/client.py", line 1291, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1337, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1286, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1046, in _send_output
    self.send(msg)
  File "/usr/local/lib/python3.6/http/client.py", line 984, in send
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 205, in connect
    conn = self._new_conn()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 187, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7fd47e23d128>: Failed to establish a new connection: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/requests/adapters.py", line 450, in send
    timeout=timeout
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 803, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/retry.py", line 594, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='backend', port=5000): Max retries exceeded with url: /reviews/add (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fd47e23d128>: Failed to establish a new connection: [Errno 111] Connection refused',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 2073, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1518, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1516, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1502, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
  File "app.py", line 19, in index
    res = requests.post("http://backend:5000/reviews/add",data={"name":name,"review":review})
  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 117, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 645, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='backend', port=5000): Max retries exceeded with url: /reviews/add (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fd47e23d128>: Failed to establish a new connection: [Errno 111] Connection refused',))
127.0.0.1 - - [18/Apr/2026 09:09:59] "POST / HTTP/1.1" 500 -
[2026-04-18 09:10:54,385] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 175, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/connection.py", line 95, in create_connection
    raise err
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 723, in urlopen
    chunked=chunked,
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 416, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 244, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/usr/local/lib/python3.6/http/client.py", line 1291, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1337, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1286, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1046, in _send_output
    self.send(msg)
  File "/usr/local/lib/python3.6/http/client.py", line 984, in send
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 205, in connect
    conn = self._new_conn()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 187, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7fd47e134470>: Failed to establish a new connection: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/requests/adapters.py", line 450, in send
    timeout=timeout
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 803, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/retry.py", line 594, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='backend', port=5000): Max retries exceeded with url: /reviews/add (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fd47e134470>: Failed to establish a new connection: [Errno 111] Connection refused',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 2073, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1518, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1516, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1502, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
  File "app.py", line 19, in index
    res = requests.post("http://backend:5000/reviews/add",data={"name":name,"review":review})
  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 117, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 645, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='backend', port=5000): Max retries exceeded with url: /reviews/add (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fd47e134470>: Failed to establish a new connection: [Errno 111] Connection refused',))
127.0.0.1 - - [18/Apr/2026 09:10:54] "POST / HTTP/1.1" 500 -
127.0.0.1 - - [18/Apr/2026 09:10:58] "GET / HTTP/1.1" 200 -
[2026-04-18 09:11:10,481] ERROR in app: Exception on / [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 175, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/connection.py", line 95, in create_connection
    raise err
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 723, in urlopen
    chunked=chunked,
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 416, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 244, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/usr/local/lib/python3.6/http/client.py", line 1291, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1337, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1286, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.6/http/client.py", line 1046, in _send_output
    self.send(msg)
  File "/usr/local/lib/python3.6/http/client.py", line 984, in send
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 205, in connect
    conn = self._new_conn()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 187, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7fd47e13bcf8>: Failed to establish a new connection: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/requests/adapters.py", line 450, in send
    timeout=timeout
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 803, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/retry.py", line 594, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='backend', port=5000): Max retries exceeded with url: /reviews/add (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fd47e13bcf8>: Failed to establish a new connection: [Errno 111] Connection refused',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 2073, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1518, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1516, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1502, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
  File "app.py", line 19, in index
    res = requests.post("http://backend:5000/reviews/add",data={"name":name,"review":review})
  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 117, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/sessions.py", line 645, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/requests/adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='backend', port=5000): Max retries exceeded with url: /reviews/add (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fd47e13bcf8>: Failed to establish a new connection: [Errno 111] Connection refused',))
127.0.0.1 - - [18/Apr/2026 09:11:10] "POST / HTTP/1.1" 500 -
127.0.0.1 - - [18/Apr/2026 09:13:23] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Apr/2026 09:13:30] "POST / HTTP/1.1" 302 -
127.0.0.1 - - [18/Apr/2026 09:35:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Apr/2026 09:38:50] "POST / HTTP/1.1" 302 -
127.0.0.1 - - [18/Apr/2026 09:51:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [18/Apr/2026 09:51:45] "POST / HTTP/1.1" 200 -
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
ERROR:  relation "reviews" does not exist
LINE 1: SELECT * FROM reviews;
                      ^
command terminated with exit code 1
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl logs backend-app-86cf5dd779-96d9t | tail -20
10.233.115.155 - - [18/Apr/2026 09:38:50] "POST /reviews/add HTTP/1.1" 200 -
[2026-04-18 09:51:45,887] ERROR in app: Exception on /reviews/add [POST]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 2073, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1518, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1516, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1502, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
  File "app.py", line 57, in addreview
    add_review(name,review)
  File "app.py", line 28, in add_review
    cursor.execute(ADD_REVIEW,(name,review))
psycopg2.errors.UndefinedTable: relation "reviews" does not exist
LINE 1: INSERT INTO REVIEWS (name,review) VALUES ('Chef','étoile')
                    ^

10.233.115.155 - - [18/Apr/2026 09:51:45] "POST /reviews/add HTTP/1.1" 500 -
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "
CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  review TEXT
);"
CREATE TABLE
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
 id | name | review 
----+------+--------
  1 | Chef | étoile
(1 row)

onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl rollout restart deployment backend-app
deployment.apps/backend-app restarted
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
 id | name | review 
----+------+--------
  1 | Chef | étoile
(1 row)

onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl delete pod postgres-db-0
pod "postgres-db-0" deleted from user-mohamederrafii namespace
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get pods -w
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-85f948fd95-tl8hq      1/1     Running   0          64s
frontend-app-f9767664-cxw4p       1/1     Running   0          47m
helloworld-app-56988bb556-76r25   1/1     Running   0          58m
helloworld-app-56988bb556-7hjdt   1/1     Running   0          58m
helloworld-app-56988bb556-8jv7l   1/1     Running   0          58m
postgres-db-0                     1/1     Running   0          15s
vscode-python-166697-0            1/1     Running   0          71m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;";"
 id | name | review 
----+------+--------
  1 | Chef | étoile
(1 row)

onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ 

onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes$ cd TP4/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ # 1. Supprimer l'ancien Deployment postgres
kubectl delete deployment postgres-db

# 2. Appliquer le StatefulSet
kubectl get podse le PVC est créélset.yaml
deployment.apps "postgres-db" deleted from user-mohamederrafii namespace
statefulset.apps/postgres-db created
service/db unchanged
NAME                          STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS      VOLUMEATTRIBUTESCLASS   AGE
data-postgresql-439617-0      Bound     pvc-5f3dd795-a5b5-4d98-96ee-1f1ed86bf1eb   10Gi       RWO            rook-ceph-block   <unset>                 375d
data-postgresql-777147-0      Bound     pvc-872aac8f-3d25-4c8d-b54c-52e31e9a69e9   10Gi       RWO            rook-ceph-block   <unset>                 100d
postgres-data-postgres-db-0   Pending                                                                        rook-ceph-block   <unset>                 0s
vscode-python-166697          Bound     pvc-2c126214-c08b-4dbe-bf52-79d510b9b38b   10Gi       RWO            rook-ceph-block   <unset>                 47h
NAME                              READY   STATUS        RESTARTS   AGE
backend-app-86cf5dd779-96d9t      1/1     Running       0          30m
frontend-app-f9767664-cxw4p       1/1     Running       0          34m
helloworld-app-56988bb556-76r25   1/1     Running       0          44m
helloworld-app-56988bb556-7hjdt   1/1     Running       0          44m
helloworld-app-56988bb556-8jv7l   1/1     Running       0          44m
postgres-db-0                     0/1     Pending       0          0s
postgres-db-7f6c48dc7f-vltsh      1/1     Terminating   0          39m
vscode-python-166697-0            1/1     Running       0          57m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
error: Internal error occurred: unable to upgrade connection: container not found ("postgres")
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl describe pod postgres-db-0 | grep "Container ID" -A1
# ou plus simple
kubectl get pod postgres-db-0 -o jsonpath='{.spec.containers[*].name}'
    Container ID:   containerd://d177ba818703f6e2a135d9c3ff1ad4af3c7dd8e457cd8059f8d699448beb1d60
    Image:          postgres:13
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"eviews;"
error: Internal error occurred: unable to upgrade connection: container not found ("postgres")
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get pod postgres-db-0
# STATUS doit être Running et READY 1/1

kubectl exec -it postgres-db-0 -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
NAME            READY   STATUS             RESTARTS      AGE
postgres-db-0   0/1     CrashLoopBackOff   4 (55s ago)   2m31s
error: Internal error occurred: unable to upgrade connection: container not found ("postgres")
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl logs postgres-db-0
kubectl logs postgres-db-0 --previous
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
It contains a lost+found directory, perhaps due to it being a mount point.
Using a mount point directly as the data directory is not recommended.
Create a subdirectory under the mount point.
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
It contains a lost+found directory, perhaps due to it being a mount point.
Using a mount point directly as the data directory is not recommended.
Create a subdirectory under the mount point.
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ # Supprimer et repartir proprement
kubectl delete statefulset postgres-db
kubectl delete pvc postgres-data-postgres-db-0

# Réappliquer
kubectl apply -f postgres-statefulset.yaml

# Vérifier
kubectl get pods -w
statefulset.apps "postgres-db" deleted from user-mohamederrafii namespace
persistentvolumeclaim "postgres-data-postgres-db-0" deleted from user-mohamederrafii namespace
statefulset.apps/postgres-db created
service/db unchanged
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-86cf5dd779-96d9t      1/1     Running   0          36m
frontend-app-f9767664-cxw4p       1/1     Running   0          40m
helloworld-app-56988bb556-76r25   1/1     Running   0          50m
helloworld-app-56988bb556-7hjdt   1/1     Running   0          50m
helloworld-app-56988bb556-8jv7l   1/1     Running   0          50m
postgres-db-0                     0/1     Pending   0          0s
vscode-python-166697-0            1/1     Running   0          63m
postgres-db-0                     0/1     Pending   0          0s
postgres-db-0                     0/1     ContainerCreating   0          0s
postgres-db-0                     1/1     Running             0          10s
^Conyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-86cf5dd779-96d9t      1/1     Running   0          37m
frontend-app-f9767664-cxw4p       1/1     Running   0          40m
helloworld-app-56988bb556-76r25   1/1     Running   0          51m
helloworld-app-56988bb556-7hjdt   1/1     Running   0          51m
helloworld-app-56988bb556-8jv7l   1/1     Running   0          51m
postgres-db-0                     1/1     Running   0          48s
vscode-python-166697-0            1/1     Running   0          64m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl exec -it postgres-db-0 -c postgres -- psql -U admin -d reviews -c "SELECT * FROM reviews;"
ERROR:  relation "reviews" does not exist
LINE 1: SELECT * FROM reviews;
                      ^
command terminated with exit code 1
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP4$ kubectl get pods
kubectl port-forward service/frontend-service 5000:5000
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-86cf5dd779-96d9t      1/1     Running   0          38m
frontend-app-f9767664-cxw4p       1/1     Running   0          42m
helloworld-app-56988bb556-76r25   1/1     Running   0          52m
helloworld-app-56988bb556-7hjdt   1/1     Running   0          52m
helloworld-app-56988bb556-8jv7l   1/1     Running   0          52m
postgres-db-0                     1/1     Running   0          117s
vscode-python-166697-0            1/1     Running   0          65m
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
Handling connection for 5000
Handling connection for 5000


