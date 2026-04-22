Sortie de mon terminal pour savoir les erreurs rencontrés (à modifier)

onyxia@vscode-python-166697-0:~/work$ cd Introduction_Kubernetes/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes$ cd TP3/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd 3.Expo_3_tiers/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs backend-app-67698fbd68-8vj4b
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.115.195:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs backend-app-67698fbd68-8vj4b | grep "Running on"
 * Running on all addresses.
 * Running on http://10.233.115.195:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f backend.yaml 
deployment.apps/backend-app configured
service/backend configured
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs backend-app-67698fbd68-8vj4b | grep "Running on"
error: error from server (NotFound): pods "backend-app-67698fbd68-8vj4b" not found in namespace "user-mohamederrafii"
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs backend-app-67698fbd68-8vj4b
error: error from server (NotFound): pods "backend-app-67698fbd68-8vj4b" not found in namespace "user-mohamederrafii"
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-86cf5dd779-96d9t      1/1     Running   0          103s
frontend-app-f9767664-cxw4p       1/1     Running   0          5m27s
helloworld-app-56988bb556-76r25   1/1     Running   0          16m
helloworld-app-56988bb556-7hjdt   1/1     Running   0          16m
helloworld-app-56988bb556-8jv7l   1/1     Running   0          16m
postgres-db-7f6c48dc7f-vltsh      1/1     Running   0          11m
vscode-python-166697-0            1/1     Running   0          28m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get logs backend-app-86cf5dd779-96d9t
error: the server doesn't have a resource type "logs"
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get log backend-app-86cf5dd779-96d9t
error: the server doesn't have a resource type "log"
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs backend-app-86cf5dd779-96d9t
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.115.215:5000/ (Press CTRL+C to quit)
10.233.115.155 - - [18/Apr/2026 09:13:30] "POST /reviews/add HTTP/1.1" 200 -
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 5000:5000
Unable to listen on port 5000: Listeners failed to create with the following errors: [unable to create listener: Error listen tcp4 127.0.0.1:5000: bind: address already in use unable to create listener: Error listen tcp6 [::1]:5000: bind: address already in use]
error: unable to listen on any of the requested ports: [{5000 5000}]
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs frontend-app-f9767664-cxw4p  
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
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get service backend
kubectl logs backend-app-86cf5dd779-96d9t | grep "Running on"
NAME      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend   ClusterIP   10.233.51.125   <none>        5000/TCP   33m
 * Running on all addresses.
 * Running on http://10.233.115.215:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs frontend-app-f9767664-cxw4p  
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
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ 


onyxia@vscode-python-166697-0:~/work$ kubectl get pods
NAME                                   READY   STATUS    RESTARTS        AGE
backend-app-67698fbd68-9bwcw           1/1     Running   1 (44h ago)     44h
database-d55d8545f-98pzp               1/1     Running   1 (7d17h ago)   12d
frontend-app-f9767664-2q8mm            1/1     Running   0               42h
helloworld-app-5b9599f4f7-67zzp        1/1     Running   0               3d23h
helloworld-app-5b9599f4f7-c7plk        1/1     Running   0               3d23h
helloworld-app-5b9599f4f7-jw828        1/1     Running   0               3d23h
postgres-db-7f6c48dc7f-mb65g           1/1     Running   0               44h
python-api-deployment-f59ff958-lmw28   1/1     Running   1 (7d17h ago)   45d
python-api-deployment-f59ff958-lx9cr   1/1     Running   1 (7d17h ago)   12d
python-api-deployment-f59ff958-v6sfn   1/1     Running   1 (7d17h ago)   24d
vscode-python-166697-0                 1/1     Running   0               80s
onyxia@vscode-python-166697-0:~/work$ kubectl get services
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend                ClusterIP   10.233.43.61    <none>        8000/TCP   44h
database               ClusterIP   10.233.54.207   <none>        5432/TCP   66d
db                     ClusterIP   10.233.48.202   <none>        5432/TCP   44h
frontend-service       ClusterIP   10.233.13.199   <none>        5000/TCP   44h
helloworld-service     ClusterIP   10.233.24.176   <none>        8081/TCP   2d18h
python-api-service     ClusterIP   10.233.29.18    <none>        80/TCP     66d
vscode-python-166697   ClusterIP   None            <none>        8080/TCP   96s
onyxia@vscode-python-166697-0:~/work$ # TP2 - helloworld
kubectl delete deployment helloworld-app
kubectl delete service helloworld-service

kubectl delete deployment frontend-app backend-app postgres-db
kubectl delete service frontend-service backend db

kubectl delete deployment database
kubectl delete service database python-api-service
kubectl delete deployment python-api-deployment
deployment.apps "helloworld-app" deleted from user-mohamederrafii namespace
service "helloworld-service" deleted from user-mohamederrafii namespace
deployment.apps "frontend-app" deleted from user-mohamederrafii namespace
deployment.apps "backend-app" deleted from user-mohamederrafii namespace
deployment.apps "postgres-db" deleted from user-mohamederrafii namespace
service "frontend-service" deleted from user-mohamederrafii namespace
service "backend" deleted from user-mohamederrafii namespace
service "db" deleted from user-mohamederrafii namespace
deployment.apps "database" deleted from user-mohamederrafii namespace
service "database" deleted from user-mohamederrafii namespace
service "python-api-service" deleted from user-mohamederrafii namespace
deployment.apps "python-api-deployment" deleted from user-mohamederrafii namespace
onyxia@vscode-python-166697-0:~/work$ kubectl gets service
error: unknown command "gets" for "kubectl"

Did you mean this?
        set
        get
onyxia@vscode-python-166697-0:~/work$ kubectl get services
NAME                   TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
vscode-python-166697   ClusterIP   None         <none>        8080/TCP   6m46s
onyxia@vscode-python-166697-0:~/work$ kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
vscode-python-166697-0   1/1     Running   0          6m55s
onyxia@vscode-python-166697-0:~/work$ cd Introduction_Kubernetes/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes$ cd TP3/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd 1.Expo_Cluster/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ kubectl apply -f app.yaml
deployment.apps/helloworld-app created
service/helloworld-service created
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ kubectl get service
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
helloworld-service     ClusterIP   10.233.32.219   <none>        8081/TCP   76s
vscode-python-166697   ClusterIP   None            <none>        8080/TCP   9m9s
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ # TP2 - helloworld
kubectl delete deployment helloworld-app
kubectl delete service helloworld-service

# TP3 - app 3-tiers (si TP terminé)
kubectl delete deployment frontend-app backend-app postgres-db
kubectl delete service frontend-service backend db

# Anciennes ressources Onyxia orphelines
kubectl delete deployment database
kubectl delete service database python-api-service
kubectl delete deployment python-api-deployment
deployment.apps "helloworld-app" deleted from user-mohamederrafii namespace
service "helloworld-service" deleted from user-mohamederrafii namespace
Error from server (NotFound): deployments.apps "frontend-app" not found
Error from server (NotFound): deployments.apps "backend-app" not found
Error from server (NotFound): deployments.apps "postgres-db" not found
Error from server (NotFound): services "frontend-service" not found
Error from server (NotFound): services "backend" not found
Error from server (NotFound): services "db" not found
Error from server (NotFound): deployments.apps "database" not found
Error from server (NotFound): services "database" not found
Error from server (NotFound): services "python-api-service" not found
Error from server (NotFound): deployments.apps "python-api-deployment" not found
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ cd ..
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd ..
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes$ cd TP2/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP2$ kubectl apply -f app.yaml
deployment.apps/helloworld-app created
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP2$ cd ..
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes$ cd TP3/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd 1.Expo_Cluster/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ kubectl apply -f app.yaml
deployment.apps/helloworld-app unchanged
service/helloworld-service created
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ kubectl get services
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
helloworld-service     ClusterIP   10.233.38.163   <none>        8081/TCP   12s
vscode-python-166697   ClusterIP   None            <none>        8080/TCP   13m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ kubectl run test-curl --image=curlimages/curl --rm -it --restart=Never \
  -- curl http://helloworld-service:8081/hello
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/test-curl, falling back to streaming logs: Internal error occurred: Internal error occurred: error attaching to container: failed to load task: no running task found: task 922c85b22bfdaec4aca550fda225ce535120faf611c394d33ecb7e5fff88c64e not found
"world"pod "test-curl" deleted from user-mohamederrafii namespace
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/1.Expo_Cluster$ cd ..
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd é
bash: cd: é: No such file or directory
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd 2.Expo_Internet/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/2.Expo_Internet$ kubectl apply -f app.yaml
ingress.networking.k8s.io/helloworld-ingress unchanged
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/2.Expo_Internet$ kubectl get ingress
NAME                      CLASS    HOSTS                                               ADDRESS       PORTS     AGE
frontend-ingress          nginx    moonshayne-app.lab.sspcloud.fr                      10.233.1.91   80        66d
helloworld-ingress        <none>   helloworld.lab.sspcloud.fr                                        80        2d18h
python-api-ingress        <none>   moonshayne-api.lab.sspcloud.fr                      10.233.1.91   80        66d
vscode-python-166697-ui   onyxia   user-mohamederrafii-166697-0.user.lab.sspcloud.fr                 80, 443   15m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/2.Expo_Internet$ curl https://helloworld.lab.sspcloud.fr/hello
"world"onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/2.Expo_Internet$ cd ..
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3$ cd 3.Expo_3_tiers/
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f postgres.yaml
deployment.apps/postgres-db created
service/db created
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f backend.yaml
deployment.apps/backend-app created
service/backend created
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f frontend.yaml
deployment.apps/frontend-app created
service/frontend-service created
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl get pods
kubectl get services
NAME                              READY   STATUS    RESTARTS   AGE
backend-app-67698fbd68-8vj4b      1/1     Running   0          23s
frontend-app-8488c7694f-lthnb     1/1     Running   0          12s
helloworld-app-56988bb556-76r25   1/1     Running   0          5m39s
helloworld-app-56988bb556-7hjdt   1/1     Running   0          5m39s
helloworld-app-56988bb556-8jv7l   1/1     Running   0          5m39s
postgres-db-7f6c48dc7f-vltsh      1/1     Running   0          38s
vscode-python-166697-0            1/1     Running   0          18m
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend                ClusterIP   10.233.51.125   <none>        8000/TCP   23s
db                     ClusterIP   10.233.9.248    <none>        5432/TCP   38s
frontend-service       ClusterIP   10.233.34.156   <none>        8501/TCP   12s
helloworld-service     ClusterIP   10.233.38.163   <none>        8081/TCP   5m13s
vscode-python-166697   ClusterIP   None            <none>        8080/TCP   18m
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 8501:8501
Forwarding from 127.0.0.1:8501 -> 8501
Forwarding from [::1]:8501 -> 8501
Handling connection for 8501
E0418 09:04:47.361828    5825 portforward.go:424] "Unhandled Error" err="an error occurred forwarding 8501 -> 8501: error forwarding port 8501 to pod 5cd147a9002dc7cf0589c618524ce0b0e8859b134c4d1cedb385a24e2a94e8e0, uid : failed to execute portforward in network namespace \"/var/run/netns/cni-3220a1c6-a609-c933-298a-787a6dc799d9\": failed to connect to localhost:8501 inside namespace \"5cd147a9002dc7cf0589c618524ce0b0e8859b134c4d1cedb385a24e2a94e8e0\", IPv4: dial tcp4 127.0.0.1:8501: connect: connection refused IPv6 dial tcp6: address localhost: no suitable address found "
error: lost connection to pod
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 8501:8501
Forwarding from 127.0.0.1:8501 -> 8501
Forwarding from [::1]:8501 -> 8501
Handling connection for 8501
E0418 09:07:00.372307    6175 portforward.go:424] "Unhandled Error" err="an error occurred forwarding 8501 -> 8501: error forwarding port 8501 to pod 5cd147a9002dc7cf0589c618524ce0b0e8859b134c4d1cedb385a24e2a94e8e0, uid : failed to execute portforward in network namespace \"/var/run/netns/cni-3220a1c6-a609-c933-298a-787a6dc799d9\": failed to connect to localhost:8501 inside namespace \"5cd147a9002dc7cf0589c618524ce0b0e8859b134c4d1cedb385a24e2a94e8e0\", IPv4: dial tcp4 127.0.0.1:8501: connect: connection refused IPv6 dial tcp6: address localhost: no suitable address found "
error: lost connection to pod
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs frontend-app-8488c7694f-lthnb
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.115.83:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl apply -f frontend.yaml
deployment.apps/frontend-app configured
service/frontend-service configured
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 5000:5000
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
Handling connection for 5000
^Conyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl logs backend-app-67698fbd68-8vj4b
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.233.115.195:5000/ (Press CTRL+C to quit)
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ 
onyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 5000:5000
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
Handling connection for 5000
Handling connection for 5000
^Conyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 5000:5000
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
Handling connection for 5000
^Conyxia@vscode-python-166697-0:~/work/Introduction_Kubernetes/TP3/3.Expo_3_tiers$ kubectl port-forward service/frontend-service 5000:5000
Forwarding from 127.0.0.1:5000 -> 5000
Forwarding from [::1]:5000 -> 5000
Handling connection for 5000
Handling connection for 5000



