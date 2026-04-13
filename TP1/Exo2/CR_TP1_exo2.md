 TP1 git:(main) cd Exo2 
➜  Exo2 git:(main) docker build -t tp1-exo2 .                                 
[+] Building 2.4s (5/5) FINISHED                                                                                                    docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                0.0s
 => => transferring dockerfile: 718B                                                                                                                0.0s
 => ERROR [internal] load metadata for docker.io/library/eclipse-temurin:17-jre-alpine                                                              2.3s
 => CANCELED [internal] load metadata for docker.io/library/maven:3.9-eclipse-temurin-17                                                            2.3s
 => [auth] library/eclipse-temurin:pull token for registry-1.docker.io                                                                              0.0s
 => [auth] library/maven:pull token for registry-1.docker.io                                                                                        0.0s
------
 > [internal] load metadata for docker.io/library/eclipse-temurin:17-jre-alpine:
------
Dockerfile:19
--------------------
  17 |     
  18 |     # Et là, on utilise notre JRE : "run de l'application avec un JRE"
  19 | >>> FROM eclipse-temurin:17-jre-alpine
  20 |     
  21 |     WORKDIR /app
--------------------
ERROR: failed to build: failed to solve: eclipse-temurin:17-jre-alpine: failed to resolve source metadata for docker.io/library/eclipse-temurin:17-jre-alpine: no match for platform in manifest: not found
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
➜  Exo2 git:(main) eclipse-temurin:21-jre
➜  Exo2 git:(main) docker build -t tp1-exo2 .
[+] Building 3.2s (12/15)                                                                                                           docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                0.0s
 => => transferring dockerfile: 830B                                                                                                                0.0s
 => [internal] load metadata for docker.io/library/maven:3.9-eclipse-temurin-17                                                                     3.0s
 => [internal] load metadata for docker.io/library/eclipse-temurin:21-jre                                                                           3.0s
 => [auth] library/maven:pull token for registry-1.docker.io                                                                                        0.0s
 => [auth] library/eclipse-temurin:pull token for registry-1.docker.io                                                                              0.0s
 => [internal] load .dockerignore                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                     0.0s
 => CANCELED [stage-1 1/3] FROM docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec    0.1s
 => => resolve docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec                     0.0s
 => => sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec 7.18kB / 7.18kB                                                      0.0s
 => => sha256:e0cc35f29e9b1b293cc87f003e6f5a84ab9dc47ffc4a79e48081a3e2b3ccc01c 1.94kB / 1.94kB                                                      0.0s
 => => sha256:4376b56bc34d9b39b408241f74cc7f5992b46292e2c6938a84e82b1af3bf7b0c 5.64kB / 5.64kB                                                      0.0s
 => CANCELED [builder 1/5] FROM docker.io/library/maven:3.9-eclipse-temurin-17@sha256:69cbc8e5054547a094d8190abc62ea0b1f4f1d0f16e03cda26fe0cfb16f3  0.1s
 => => resolve docker.io/library/maven:3.9-eclipse-temurin-17@sha256:69cbc8e5054547a094d8190abc62ea0b1f4f1d0f16e03cda26fe0cfb16f3edab               0.0s
 => => sha256:cb3feaf1b61588cc9fc9160566bcc3b98428e53b9057e38431d204c7e69d9cb3 2.91kB / 2.91kB                                                      0.0s
 => => sha256:69cbc8e5054547a094d8190abc62ea0b1f4f1d0f16e03cda26fe0cfb16f3edab 7.94kB / 7.94kB                                                      0.0s
 => => sha256:7fabb8caa28761bd73a7b5adbd47000ebd156e3ad13c8b0bb84b325ba0833414 9.73kB / 9.73kB                                                      0.0s
 => [internal] load build context                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                     0.0s
 => CACHED [builder 2/5] WORKDIR /app                                                                                                               0.0s
 => ERROR [builder 3/5] COPY pom.xml .                                                                                                              0.0s
 => ERROR [builder 4/5] COPY src ./src                                                                                                              0.0s
------
 > [builder 3/5] COPY pom.xml .:
------
------
 > [builder 4/5] COPY src ./src:
------
Dockerfile:13
--------------------
  11 |     
  12 |     # On copie les sources
  13 | >>> COPY src ./src 
  14 |     
  15 |     # Build de l'application
--------------------
ERROR: failed to build: failed to solve: failed to compute cache key: failed to calculate checksum of ref 853468fa-6247-4aaa-929b-544716e137e2::ucpsrrduw0meq94tasoragn5w: "/src": not found
➜  Exo2 git:(main) ✗ docker build -t tp1-exo2 .
[+] Building 3.5s (12/15)                                                                                                           docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                0.0s
 => => transferring dockerfile: 830B                                                                                                                0.0s
 => [internal] load metadata for docker.io/library/eclipse-temurin:21-jre                                                                           3.1s
 => [internal] load metadata for docker.io/library/maven:3.9-eclipse-temurin-17                                                                     3.4s
 => [auth] library/eclipse-temurin:pull token for registry-1.docker.io                                                                              0.0s
 => [auth] library/maven:pull token for registry-1.docker.io                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                     0.0s
 => CANCELED [builder 1/5] FROM docker.io/library/maven:3.9-eclipse-temurin-17@sha256:69cbc8e5054547a094d8190abc62ea0b1f4f1d0f16e03cda26fe0cfb16f3  0.1s
 => => resolve docker.io/library/maven:3.9-eclipse-temurin-17@sha256:69cbc8e5054547a094d8190abc62ea0b1f4f1d0f16e03cda26fe0cfb16f3edab               0.0s
 => => sha256:7fabb8caa28761bd73a7b5adbd47000ebd156e3ad13c8b0bb84b325ba0833414 9.73kB / 9.73kB                                                      0.0s
 => => sha256:69cbc8e5054547a094d8190abc62ea0b1f4f1d0f16e03cda26fe0cfb16f3edab 7.94kB / 7.94kB                                                      0.0s
 => => sha256:cb3feaf1b61588cc9fc9160566bcc3b98428e53b9057e38431d204c7e69d9cb3 2.91kB / 2.91kB                                                      0.0s
 => [internal] load build context                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                     0.0s
 => CANCELED [stage-1 1/3] FROM docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec    0.1s
 => => resolve docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec                     0.0s
 => => sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec 7.18kB / 7.18kB                                                      0.0s
 => => sha256:e0cc35f29e9b1b293cc87f003e6f5a84ab9dc47ffc4a79e48081a3e2b3ccc01c 1.94kB / 1.94kB                                                      0.0s
 => => sha256:4376b56bc34d9b39b408241f74cc7f5992b46292e2c6938a84e82b1af3bf7b0c 5.64kB / 5.64kB                                                      0.0s
 => CACHED [builder 2/5] WORKDIR /app                                                                                                               0.0s
 => ERROR [builder 3/5] COPY pom.xml .                                                                                                              0.0s
 => ERROR [builder 4/5] COPY src ./src                                                                                                              0.0s
------
 > [builder 3/5] COPY pom.xml .:
------
------
 > [builder 4/5] COPY src ./src:
------
Dockerfile:13
--------------------
  11 |     
  12 |     # On copie les sources
  13 | >>> COPY src ./src 
  14 |     
  15 |     # Build de l'application
--------------------
ERROR: failed to build: failed to solve: failed to compute cache key: failed to calculate checksum of ref 853468fa-6247-4aaa-929b-544716e137e2::59khnywafiuyllh8vjceakhw2: "/src": not found
➜  Exo2 git:(main) ✗ docker build -t tp1-exo2 .
[+] Building 386.0s (15/15) FINISHED                                                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                0.0s
 => => transferring dockerfile: 1.04kB                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/maven:3.9-eclipse-temurin-21                                                                     2.2s
 => [internal] load metadata for docker.io/library/eclipse-temurin:21-jre                                                                           0.9s
 => [internal] load .dockerignore                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                     0.0s
 => [builder 1/5] FROM docker.io/library/maven:3.9-eclipse-temurin-21@sha256:481aad0b7042ad7a924ebd49ea5b307a049bd33d758f8613d68dcbd2904f3c8e     282.3s
 => => resolve docker.io/library/maven:3.9-eclipse-temurin-21@sha256:481aad0b7042ad7a924ebd49ea5b307a049bd33d758f8613d68dcbd2904f3c8e               0.0s
 => => sha256:76fd055477b6edf8004a5a962edad02a820d4c8b2f02682410edfbe376b418c5 28.87MB / 28.87MB                                                   47.9s
 => => sha256:481aad0b7042ad7a924ebd49ea5b307a049bd33d758f8613d68dcbd2904f3c8e 6.65kB / 6.65kB                                                      0.0s
 => => sha256:91db5c02b513db5c1faff0c9eb310e01595ec27c58bcd2797e986a60e835a41f 9.66kB / 9.66kB                                                      0.0s
 => => sha256:571cc6f4fe80027a65fbaead9a4c234c3f2078738acb8bebc1646533dfbdfb0b 2.92kB / 2.92kB                                                      0.0s
 => => sha256:21c7d1b1c79c5ecc5fccf686d3358ce1ce67645041767f3b414cf69acfa63f91 24.17MB / 24.17MB                                                   94.7s
 => => sha256:80ff0baa3d4d98b333e10ac5a29849712241a6e7241a71aac16f5e3cbf06d88a 156.14MB / 156.14MB                                                277.2s
 => => extracting sha256:76fd055477b6edf8004a5a962edad02a820d4c8b2f02682410edfbe376b418c5                                                         335.5s
 => => sha256:270f33f32bad8041e2f3bccef67345ec2c76c01a1d45b76d51a19cb2d52d14b6 159B / 159B                                                         96.4s
 => => extracting sha256:21c7d1b1c79c5ecc5fccf686d3358ce1ce67645041767f3b414cf69acfa63f91                                                           1.5s
 => => sha256:2d6ceb247738b23fbed80439fa7e1cf66042b6767e2c0e0f2057a251f8e1c404 2.28kB / 2.28kB                                                     96.7s
 => => sha256:84698d45be067bc0907994117b8f027e3c484706cd4eb2419b11295996d3512b 22.61MB / 22.61MB                                                  236.5s
 => => sha256:1b7045829dea4f0c1a15b15cd94770be0c970281b0866f0e6369979506aac69b 9.31MB / 9.31MB                                                    203.5s
 => => sha256:0c663e33530b7abe39f302afe580fb97f888bf4fc79d3c6a17208ae53896ec06 850B / 850B                                                        204.0s
 => => sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B                                                          204.6s
 => => sha256:ef26ee0d1708c0e73c005976ab892d40d47a536f4915fe52a4243ac12ca815d4 155B / 155B                                                        205.0s
 => => extracting sha256:80ff0baa3d4d98b333e10ac5a29849712241a6e7241a71aac16f5e3cbf06d88a                                                           2.4s
 => => extracting sha256:270f33f32bad8041e2f3bccef67345ec2c76c01a1d45b76d51a19cb2d52d14b6                                                           0.0s
 => => extracting sha256:2d6ceb247738b23fbed80439fa7e1cf66042b6767e2c0e0f2057a251f8e1c404                                                           0.0s
 => => extracting sha256:84698d45be067bc0907994117b8f027e3c484706cd4eb2419b11295996d3512b                                                           1.9s
 => => extracting sha256:1b7045829dea4f0c1a15b15cd94770be0c970281b0866f0e6369979506aac69b                                                           0.1s
 => => extracting sha256:0c663e33530b7abe39f302afe580fb97f888bf4fc79d3c6a17208ae53896ec06                                                           0.0s
 => => extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1                                                           0.0s
 => => extracting sha256:ef26ee0d1708c0e73c005976ab892d40d47a536f4915fe52a4243ac12ca815d4                                                           0.0s
 => [stage-1 1/3] FROM docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec           189.2s
 => => resolve docker.io/library/eclipse-temurin:21-jre@sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec                     0.0s
 => => sha256:67f35487ed2661ef1a9abe9e1463176946610327c6610d40bfa71dde6f5d7cec 7.18kB / 7.18kB                                                      0.0s
 => => sha256:e0cc35f29e9b1b293cc87f003e6f5a84ab9dc47ffc4a79e48081a3e2b3ccc01c 1.94kB / 1.94kB                                                      0.0s
 => => sha256:4376b56bc34d9b39b408241f74cc7f5992b46292e2c6938a84e82b1af3bf7b0c 5.64kB / 5.64kB                                                      0.0s
 => => sha256:76fd055477b6edf8004a5a962edad02a820d4c8b2f02682410edfbe376b418c5 28.87MB / 28.87MB                                                  383.6s
 => => sha256:bfc1fe49c2f79e04d9e562ce4ee017e874bf7e23feea81b6df6f351ab993d9b5 17.00MB / 17.00MB                                                   35.1s
 => => sha256:538e758f95d8493adbf608ecfa760b05bb49d3ceee0f1e637ca69598f3434ea6 52.16MB / 52.16MB                                                  187.2s
 => => sha256:80e0252f321812c22ad7139fe93995a4ab816f331d23ab15579dedbc1027f1ca 158B / 158B                                                         36.1s
 => => sha256:3f199c35f5162fea3c8f07eef1e388cab02e2e3f619c9b2842b8bcd77a768e1e 2.28kB / 2.28kB                                                     36.7s
 => => extracting sha256:76fd055477b6edf8004a5a962edad02a820d4c8b2f02682410edfbe376b418c5                                                           1.8s
 => => extracting sha256:bfc1fe49c2f79e04d9e562ce4ee017e874bf7e23feea81b6df6f351ab993d9b5                                                           0.7s
 => => extracting sha256:538e758f95d8493adbf608ecfa760b05bb49d3ceee0f1e637ca69598f3434ea6                                                           1.3s
 => => extracting sha256:80e0252f321812c22ad7139fe93995a4ab816f331d23ab15579dedbc1027f1ca                                                           0.0s
 => => extracting sha256:3f199c35f5162fea3c8f07eef1e388cab02e2e3f619c9b2842b8bcd77a768e1e                                                           0.0s
 => [internal] load build context                                                                                                                   0.0s
 => => transferring context: 2.23kB                                                                                                                 0.0s
 => [auth] library/maven:pull token for registry-1.docker.io                                                                                        0.0s
 => [stage-1 2/3] WORKDIR /app                                                                                                                      0.3s
 => [builder 2/5] WORKDIR /app                                                                                                                      0.5s
 => [builder 3/5] COPY java-api/pom.xml .                                                                                                           0.0s
 => [builder 4/5] COPY java-api/src ./src                                                                                                           0.0s
 => [builder 5/5] RUN mvn clean package -DskipTests                                                                                                97.9s
 => [stage-1 3/3] COPY --from=builder /app/target/*.jar app.jar                                                                                     0.1s
 => exporting to image                                                                                                                              0.3s
 => => exporting layers                                                                                                                             0.1s
 => => writing image sha256:80c921fdf3ac6e3e1901c76ebf6d58235de53988563e30da0e071c1f4b9e027b                                                        0.0s
 => => naming to docker.io/library/tp1-exo2                                                                                                         0.1s
➜  Exo2 git:(main) ✗ docker run -p 8082:8082 tp1-exo2

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

2026-04-13T20:00:12.610Z  INFO 1 --- [           main] com.example.Application                  : Starting Application v1.0.0 using Java 21.0.10 with PID 1 (/app/app.jar started by root in /app)
2026-04-13T20:00:12.621Z  INFO 1 --- [           main] com.example.Application                  : No active profile set, falling back to 1 default profile: "default"
2026-04-13T20:00:15.212Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2026-04-13T20:00:15.239Z  INFO 1 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2026-04-13T20:00:15.239Z  INFO 1 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.16]
2026-04-13T20:00:15.388Z  INFO 1 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2026-04-13T20:00:15.392Z  INFO 1 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 2528 ms
2026-04-13T20:00:16.074Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path ''
2026-04-13T20:00:16.120Z  INFO 1 --- [           main] com.example.Application                  : Started Application in 5.299 seconds (process running for 6.869)
^C%                                                                                                                                                      
➜  Exo2 git:(main) ✗ docker run -d -p 8081:8081 tp1-exo2
f43f4fb4d34f0eddabd2b8a0d078948c1016cf3c5c2396e6cd2944341847f905
docker: Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint eloquent_swanson (63a05bea18baca041ed1cc41be63e5199584b9cd62533dc6730002f1565fb28a): Bind for 0.0.0.0:8081 failed: port is already allocated

Run 'docker run --help' for more information
➜  Exo2 git:(main) ✗ docker run -d -p 8082:8082 tp1-exo2
2148024222e4094298c933d88b7615588fb676c1572c1309811f3e8cbf67b862
➜  Exo2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS              PORTS                                         NAMES
2148024222e4   tp1-exo2      "java -jar app.jar"      About a minute ago   Up About a minute   0.0.0.0:8082->8082/tcp, [::]:8082->8082/tcp   crazy_panini
44891350518b   tp1-exo1      "uvicorn python-api.…"   6 hours ago          Up 6 hours          0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago           Up 11 hours         5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) ✗ docker logs 2148024222e4

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

2026-04-13T20:03:57.513Z  INFO 1 --- [           main] com.example.Application                  : Starting Application v1.0.0 using Java 21.0.10 with PID 1 (/app/app.jar started by root in /app)
2026-04-13T20:03:57.517Z  INFO 1 --- [           main] com.example.Application                  : No active profile set, falling back to 1 default profile: "default"
2026-04-13T20:03:59.673Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2026-04-13T20:03:59.695Z  INFO 1 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2026-04-13T20:03:59.696Z  INFO 1 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.16]
2026-04-13T20:03:59.822Z  INFO 1 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2026-04-13T20:03:59.830Z  INFO 1 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 2120 ms
2026-04-13T20:04:02.187Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path ''
2026-04-13T20:04:02.235Z  INFO 1 --- [           main] com.example.Application                  : Started Application in 5.507 seconds (process running for 7.057)
➜  Exo2 git:(main) ✗ # Stopper et supprimer le conteneur actuel
docker stop crazy_panini && docker rm crazy_panini

# Relancer avec le bon mapping 8082 (host) -> 8080 (conteneur)
docker run -d -p 8082:8080 tp1-exo2
crazy_panini
crazy_panini
b446c0db58834f8d57ce3a1e8fc7fd52f0fcd3bd1c54b230272448ca7930981c
➜  Exo2 git:(main) ✗ docker logs 2148024222e4                  
Error response from daemon: No such container: 2148024222e4
➜  Exo2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS              PORTS                                         NAMES
b446c0db5883   tp1-exo2      "java -jar app.jar"      About a minute ago   Up About a minute   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   distracted_morse
44891350518b   tp1-exo1      "uvicorn python-api.…"   6 hours ago          Up 6 hours          0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago           Up 11 hours         5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) ✗ docker logs b446c0db5883

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

2026-04-13T20:11:19.141Z  INFO 1 --- [           main] com.example.Application                  : Starting Application v1.0.0 using Java 21.0.10 with PID 1 (/app/app.jar started by root in /app)
2026-04-13T20:11:19.145Z  INFO 1 --- [           main] com.example.Application                  : No active profile set, falling back to 1 default profile: "default"
2026-04-13T20:11:21.407Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 8080 (http)
2026-04-13T20:11:21.428Z  INFO 1 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2026-04-13T20:11:21.428Z  INFO 1 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.16]
2026-04-13T20:11:21.521Z  INFO 1 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2026-04-13T20:11:21.532Z  INFO 1 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 2256 ms
2026-04-13T20:11:22.380Z  INFO 1 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8080 (http) with context path ''
2026-04-13T20:11:22.395Z  INFO 1 --- [           main] com.example.Application                  : Started Application in 3.833 seconds (process running for 6.072)
2026-04-13T20:11:27.478Z  INFO 1 --- [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2026-04-13T20:11:27.479Z  INFO 1 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2026-04-13T20:11:27.482Z  INFO 1 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 3 ms
➜  Exo2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS              PORTS                                         NAMES
b446c0db5883   tp1-exo2      "java -jar app.jar"      About a minute ago   Up About a minute   0.0.0.0:8082->8080/tcp, [::]:8082->8080/tcp   distracted_morse
44891350518b   tp1-exo1      "uvicorn python-api.…"   6 hours ago          Up 6 hours          0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago           Up 11 hours         5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) ✗ docker kill b446c0db5883
b446c0db5883
➜  Exo2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS        PORTS                                         NAMES
44891350518b   tp1-exo1      "uvicorn python-api.…"   6 hours ago   Up 6 hours    0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago    Up 11 hours   5432/tcp                                      stage3a-db-1
➜  Exo2 git:(main) ✗ cd ..
➜  TP1 git:(main) ✗ cd Exo2 
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
➜  Exo2 git:(main) ✗ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS        PORTS                                         NAMES
44891350518b   tp1-exo1      "uvicorn python-api.…"   6 hours ago   Up 6 hours    0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp   peaceful_herschel
e5e034a8a18e   postgres:18   "docker-entrypoint.s…"   6 days ago    Up 11 hours   5432/tcp                                      stage3a-db-1
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
➜  Exo2 git:(main) ✗ docker push moonshayne/tp1-exo2
Using default tag: latest
The push refers to repository [docker.io/moonshayne/tp1-exo2]
An image does not exist locally with the tag: moonshayne/tp1-exo2
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
➜  Exo2 git:(main) ✗ 


et modification : 

eclipse-temurin:21-jre

maven:3.9-eclipse-temurin-21


