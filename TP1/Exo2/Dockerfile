# On reprend la structure des diapos (celle nommée Multi-Stage build)

# Le JDK (Java Development Kit) est inclus par défaut dans Maven.
# On l'utilise ici pour respecter les consignes et l'énoncé : "build de l'application avec un JDK"
FROM maven:3.9-eclipse-temurin-17 AS builder

WORKDIR /app

# On copie le fichier de configuration Maven
COPY pom.xml . 

# On copie les sources
COPY src ./src 

# Build de l'application
RUN mvn clean package -DskipTests

# Et là, on utilise notre JRE : "run de l'application avec un JRE"
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8082 

ENTRYPOINT ["java", "-jar", "app.jar"]