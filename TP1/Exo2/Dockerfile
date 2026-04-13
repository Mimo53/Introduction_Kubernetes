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