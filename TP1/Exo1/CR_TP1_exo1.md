(Pour ce TP, je l'ai réalisé sur mon ordinateur personnel qui est un macOS)
# Exo 1 

## Le docker file a pour code : 

```dockerfile
# On part d'une image de base de python qui contient toute les dépendances nécessaire pour le reste de notre projet

FROM python:3.13-slim

/# on se palce dans le dossier app pour les prochaines commandes du dockerfile

WORKDIR /app

# On copie tout, ce n'est pas optimale (si il y a un changement dnas le code mais pas dans les dépendances on re-charge toute l'image mais on verra l'optimisation plus tard)

COPY . .

# On installe les requirements mais on vide le cache car d'une part ce n'est pas utile d'autres part ça prends de la place en stockage

RUN pip install --no-cache-dir -r python-api/requirements.txt

# Port choisi totalement au hasard

EXPOSE 8081

# Comme on utilise FastApi, on se met d'abord sur Uvicorn, pour pourvoir l'utiliser. 

ENTRYPOINT ["uvicorn", "python-api.src.main:app","--host", "0.0.0.0", "--port", "8081"]

```

Puis on fait dans notre terminal : 

```bash
 TP1 git:(main) ✗ ls

1_docker.md Exo1        java-api

➜  TP1 git:(main) ✗ cd Exo1 

➜  Exo1 git:(main) ✗ ls

CR.md      Dockerfile python-api

➜  Exo1 git:(main) ✗ tree   
.
├── CR.md
├── Dockerfile
└── python-api
    ├── requirements.txt
    └── src
        └── main.py

3 directories, 4 files

➜  Exo1 git:(main) ✗ docker build -t tp1-exo1 .   

[+] Building 9.8s (9/9) 
FINISHED                                                                                                                                                                      docker:desktop-linux

 => [internal] load build definition from Dockerfile                                                                                   0.0s

 => => transferring dockerfile: 876B                                                                                                   0.0s

 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                    0.6s

 => [internal] load .dockerignore                                                                                                      0.0s

 => => transferring context: 2B                                                                                                        0.0s

 => [1/4] FROM docker.io/library/python:3.13-slim@sha256:d168b8d9eb761f4d3fe305ebd04aeb7e7f2de0297cec5fb2f8f6403244621664              0.0s

 => [internal] load build context                                                                                                      0.0s

 => => transferring context: 1.13kB                                                                                                    0.0s

 => CACHED [2/4] WORKDIR /app                                                                                                          0.0s

 => [3/4] COPY . .                                                                                                                     0.0s

 => [4/4] RUN pip install --no-cache-dir -r python-api/requirements.txt                                                                9.1s

 => exporting to image                                                                                                                 0.1s

 => => exporting layers                                                                                                                0.1s

 => => writing image sha256:1a4b8bb2ba9712462d5c70cea4be148608043ba20f8c2e7a97accf5a7caab738                                           0.0s 

 => => naming to docker.io/library/tp1-exo1                                                                                            0.0s 

➜  Exo1 git:(main) ✗ docker run -d -p 8081:8081 tp1-exo1

bf62e062229f3e6de2cb099b2dc1a6661cc04a207e610b083ceddf8c07e322c2

➜  Exo1 git:(main) ✗ docker ps      

CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                                         NAMES
bf62e062229f   tp1-exo1      "uvicorn python-api.…"   21 seconds ago   Up 20 seconds   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   jolly_pike

➜  Exo1 git:(main) ✗ docker logs bf62e062229f

INFO:     Started server process [1]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)

➜  Exo1 git:(main) ✗ docker logs bf62e062229f

INFO:     Started server process [1]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)

INFO:     192.168.65.1:36298 - "GET /hello HTTP/1.1" 200 OK

INFO:     192.168.65.1:28219 - "GET /favicon.ico HTTP/1.1" 404 Not Found

➜  Exo1 git:(main) ✗ docker tag tp1-exo1 moonshayne/tp1-exo1

➜  Exo1 git:(main) ✗ docker push moonshayne/tp1-exo1

Using default tag: latest

The push refers to repository [docker.io/moonshayne/tp1-exo1]

79effefc456a: Pushed 

05ad96d70f99: Pushed 

69936bbb496d: Pushed 

678cc16ba548: Mounted from library/python 

b9e6b8887d35: Mounted from library/python 

ec833b93e52e: Mounted from library/python 

f38e00a1a324: Mounted from library/python 

latest: digest: sha256:673d83f3fb6baafb898b31aa132789803caac110c33d922873dd6402be3d1d70 size: 1784

➜  Exo1 git:(main) ✗

```

### Commentaire : 

Quand on regarde les logs de notre image docker, on remarque le message :
 ```text
 INFO: 192.168.65.1:28219 - "GET /favicon.ico HTTP/1.1" 404 Not Found
 ``` 

Cette erreur vient du fait que notre image n'a pas d'icon d'après le forum : https://discuss.python.org/t/get-http-1-1-404-get-favicon-ico-http-1-1-404/34577



## Difficulté rencontrer :

Au début, il y avait plusieurs problèmes, notamment des erreurs de syntaxes comme :
```bash
docker build -t <Exo1>/Dockerfile
```

au lieu de : 
```bash
docker build -t tp1-exo1
```

Aussi il y avait des fautes d'orthographes qui se cachait dans mon Dockerfile (pyhton au lieu de python, requirement au lieu de requirements,...)

Quand je lancais : 

```bash
Exo1 git:(main) ✗ docker run dockerfile
```
Aussi j'avais l'erreur :  
```text
failed to connect to the docker API at unix:///Users/zaslaoui/.docker/run/docker.sock; check if the path is correct and if the daemon is running: dial unix /Users/zaslaoui/.docker/run/docker sock: connect: no such file or directory
```

car je n'avais pas lancer Docker desktop sur mon mac

Par ailleurs, j'oubliais les espaces entre les points dnas mon dockerfile

Aussi l'ENTRYPOINT était mauvais, je mettais le chemin absolu depuis mon mac alors qu'il fallait mettre depuis le chemin relatif au WORDIR

Et pour l'ENTRYPOINT, je ne lancais pas python avant ni je rajoutais à main.py un shebang du style '#!/usr/bin/env python3'

Ensuite dans mon terminal je mettais seulement 'docker build -t tp1-exo1' ce qui m'a causé des erreurs je n'avais pas mis de contexte de build : 

ERROR: docker: 'docker buildx build' requires 1 argument

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Run 'docker buildx build --help' for more information 

Donc je devais changer ma commande pour mettre 'docker build -t tp1-exo1 .' pour lui dire de lancer la commande à partir de là où j'étais 

Après une fois que j'arrivais bien à build, j'avais des erreurs dans mon dockerfile, notamment avec le 'COPY python-api/requirements.txt .' (que j'ai remplacé par COPY .. que j'ai lui même remplacé par COPY . .) et des fautes d'orthographes (encore une fois)

avec notamment "--no-cache-dire" au lieu de "--no-cache-dir"

Aussi j'avais l'erreur : 
'''
 Exo1 git:(main) ✗ docker run -p 8080:8080 tp1-exo1
python: can't open file '/python-api/src/main.py': [Errno 2] No such file or directory

malgré le fait que ma structure de code était : 

➜  Exo1 git:(main) ✗ tree
.
├── CR.md
├── Dockerfile
└── python-api
    ├── requirements.txt
    └── src
        └── main.py

3 directories, 4 files
'''

J'avias cette erreur car je cherchais mon main.py dans le conteneur et non en local et donc le chemin n'était plus "/python-api/src/main.py" mais étais devenu "python-api/src/main.py" sans le slash au début car 


Dans mon `Dockerfile`, je défini `WORKDIR /app`. Quand je fais `COPY . .`, la structure à l'intérieur de mon conteneur devient :
* `/app/CR.md`
* `/app/Dockerfile`
* `/app/python-api/src/main.py`


Donc j'enlève le slash ou alors j'aurais pu mettre : 
```
WORKDIR /app/python-api/src

EXPOSE 8080

ENTRYPOINT ["python", "main.py"]
```
Pour me déplacer au bon endroit

Mais cette erreur m'a appris à apprendre la commande `docker run -it tp1-exo1 ls -R /app`

Pour comprendre ce  qu'il y a "vraiment" dans mon conteneur pour comprendre pourquoi un chemin échoue. 

Puis la connexion à la page ne se faisait pas 

car mon application crashait tout de suite après s'être lancé et j'ai eu du mal à trouver les messages d'erreur (messages que je n'ai au final jamais trouvé)

le problème était que main.py faisait appel à FastAPI et que FastAPI ne se alncait pas avec directement avec python et j'avais besoin d'un serveur ASGI et j'avais besoin de uvicorn donc 
mon entrypoint était incorrect donc j'ai remplacé 

'''
ENTRYPOINT ["python", "main.py"]
'''

par 
'''
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
'''

Enfin j'avais les messages : " 

INFO:     192.168.65.1:37012 - "GET / HTTP/1.1" 404 Not Found
INFO:     192.168.65.1:43436 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     192.168.65.1:37012 - "GET /index.php/apps/files/preview-service-worker.js HTTP/1.1" 404 Not Found

ce qui faisait que quand j'allais sur la page page localhost:8080 je ne voyais rien mais c'était parce que mon API n'avait qu'une seule route défénie `/hello` 

et enfin le message : " INFO:     192.168.65.1:43436 - "GET /favicon.ico HTTP/1.1" 404 Not Found " n'est pas une erreur mais juste le signalement du manque d'icon. 
