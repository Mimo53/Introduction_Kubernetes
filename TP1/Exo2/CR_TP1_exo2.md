(Pour ce TP, je l'ai réalisé sur mon ordinateur personnel qui est un macOS)
# Exo2
Pour ce TP, on a repris le dockerfile du cours et on l'a adpaté à notre besoin.

## Dockerfile et commande bash

```dockerfile
# On reprend la structure des diapos (celle nommée Multi-Stage build)

# Le JDK (Java Development Kit) est inclus par défaut dans Maven.
# On l'utilise ici pour respecter les consignes et l'énoncé : "build de l'application avec un JDK" (on change la version à 21 pour être en correspondance avec le reste)
FROM maven:3.9-eclipse-temurin-21 AS builder

WORKDIR /app

COPY java-api/pom.xml .
COPY java-api/src ./src


# Build de l'application
RUN mvn clean package -DskipTests

# Et là, on utilise notre JRE : "run de l'application avec un JRE" (j'ai changé "eclipse-temurin:17-jre-alpine" par "eclipse-temurin:21-jre" pour les raisons suivantes
# je travaille sur mac et la version antérieure précédente n'a pas d'image pour l'architecture ARM par ailleurs dans le fichier pom.xml on utilise la version 21 de java 
# qui peut causer des problèmes)
FROM eclipse-temurin:21-jre

WORKDIR /app

COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8082 

ENTRYPOINT ["java", "-jar", "app.jar"]
```

Ensuite on fait dans notre terminal : 
```bash
TP1 git:(main) cd Exo2 
➜  Exo2 git:(main) ✗ docker build -t tp1-exo2 .      
[+] Building 3.9s (16/16) FINISHED                                                                                                  docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                0.0s
 => => transferring dockerfile: 1.04kB                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/maven:3.9-eclipse-temurin-21                                                                     3.7s
 => [internal] load metadata for docker.io/library/eclipse-temurin:21-jre                                                                           3.7s
 => [auth] library/eclipse-temurin:pull token for registry-1.docker.io                                                                              0.0s
 => [auth] library/maven:pull token for registry-1.docker.io                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                     0.0s
 => [builder 1/5] FROM docker.io/library/maven:3.9-eclipse-temurin-21@sha256:481aad0b7042ad7a924ebd49ea5b307a049bd33d758f8613d68dcbd2904f3c8e       0.0s
 => [internal] load build context                                                                                                                   0.0s
 => => transferring context: 423B                                                                                                                   0.0s
 => [stage-1 1/3] FROM docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec             0.0s
 => CACHED [stage-1 2/3] WORKDIR /app                                                                                                               0.0s
 => CACHED [builder 2/5] WORKDIR /app                                                                                                               0.0s
 => CACHED [builder 3/5] COPY java-api/pom.xml .                                                                                                    0.0s
 => CACHED [builder 4/5] COPY java-api/src ./src                                                                                                    0.0s
 => CACHED [builder 5/5] RUN mvn clean package -DskipTests                                                                                          0.0s
 => CACHED [stage-1 3/3] COPY --from=builder /app/target/*.jar app.jar                                                                              0.0s
 => exporting to image                                                                                                                              0.0s
 => => exporting layers                                                                                                                             0.0s
 => => writing image sha256:80c921fdf3ac6e3e1901c76ebf6d58235de53988563e30da0e071c1f4b9e027b                                                        0.0s
 => => naming to docker.io/library/tp1-exo2                                                                                                         0.0s

➜  Exo2 git:(main) ✗ docker run -d -p 8082:8080 tp1-exo2       
dc1720130576cd748db60bb65f1857591501b4926739787242d07acce6ee4a4e
➜  Exo2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                         NAMES
dc1720130576   tp1-exo2      "java -jar app.jar"      7 seconds ago   Up 6 seconds   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   lucid_yalow
44891350518b   tp1-exo1      "uvicorn python-api.…"   6 hours ago     Up 6 hours     0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago      Up 11 hours    5432/tcp                                      stage3a-db-1

➜  Exo2 git:(main) ✗ docker logs dc1720130576

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

2026-04-13T20:15:04.015Z  INFO 1 --- [           main] com.example.Application                  : Starting Application v1.0.0 using Java 21.0.10 with PID 1 (/app/app.jar started by root in /app)
2026-04-13T20:15:04.019Z  INFO 1 --- [           main] com.example.Application                  : No active profile set, falling back to 1 default profile: "default"
2026-04-13T20:15:05.113Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2026-04-13T20:15:05.129Z  INFO 1 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2026-04-13T20:15:05.130Z  INFO 1 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.16]
2026-04-13T20:15:05.176Z  INFO 1 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2026-04-13T20:15:05.177Z  INFO 1 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1070 ms
2026-04-13T20:15:05.489Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path ''
2026-04-13T20:15:05.501Z  INFO 1 --- [           main] com.example.Application                  : Started Application in 1.994 seconds (process running for 3.061)
```
```bash
➜  Exo2 git:(main) ✗ docker tag tp1-exo2 moonshayne/tp1-exo2
➜  Exo2 git:(main) ✗ docker push moonshayne/tp1-exo2
Using default tag: latest
The push refers to repository [docker.io/moonshayne/tp1-exo2]
96f8f8f9b6a3: Pushed 
c98cd0b88a61: Pushed 
6beb9de35608: Mounted from library/eclipse-temurin 
3e30637c8aa8: Mounted from library/eclipse-temurin 
29736819a753: Mounted from library/eclipse-temurin 
1548b43f0990: Mounted from library/eclipse-temurin 
e17beae36f94: Mounted from library/eclipse-temurin 
latest: digest: sha256:5ec612dbf111d256cea2a0fcd8052840411d8edba3a35767e2e5e277528972ad size: 1786
```

## Difficultés rencontrées : 
Tout d'abors comme je travaille sur mac personnel j'ai remarqué que l'image "eclipse-temurin:17-jre-alpine" n'était pas adapté pour l'architecture sur laquelle je travaillais (à savoir ARM64) donc j'ai dû cherhcer une autre version compatibles avec mon ordinateur et par ailleurs en regardant le pom.xml j'ai remarqué quue l'on utilisais la version 21 de Java et que la version 21 de eclipse-temurin était compatibles avec les ARM64. Donc c'est celle que j'ai prise. Je me suis aussi permit de changer la version de maven utilisé pour garder une cohérence entre les outils utilisés. 

Ensuite j'ai encore eu des problèmes pour comprendre le placement des fichiers, dnas mon dockerfile je faisais 

```dockerfile
COPY pom.xml .
```
au lieu 
```dockerfile
COPY java-api/pom.xml .
```

et de même, je mettais 

```dockerfile
COPY src ./src
```
 au lieu de 

```dockerfile
COPY java-api/src ./src
```


Après j'ai eu des erreurs de ports, quand je faisais 
```bash
➜  Exo2 git:(main) ✗ docker run -p 8082:8082 tp1-exo2
```
j'avais :
```text
docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint eloquent_swanson (63a05bea18baca041ed1cc41be63e5199584b9cd62533dc6730002f1565fb28a): Bind for 0.0.0.0:8081 failed: port is already allocated

Run 'docker run --help' for more information
```

J'ai eu des problèmes de mapping de port (car pour une raison que j'ignore, le conteneur était mappé au port 8080 (je me pencherais sur la question plus tard je pense que ça doit être le port par défaut d'un service qui utilisé par l'application)) et j'ai du faire du nettoyage puis ça a marché. 



