# TP 4 Gestion de la persistance 

## Objectifs du TP

- Comprendre les mécanismes de persistance dans Kubernetes
- Ajouter de la persistance à une application 
- Déployer une application stateful 


Livrable : 
- Manifest kubernetes pour déployer les applications 
- Un compte rendu avec les difficultés rencontrées, et les résultats de chaque exercice. 

## Prérequis

- Avoir un compte SSPCloud 

## Activer la persistance sur notre application

Comme vous avez pu le voir lors du précédent TP, notre base de données n'a aucune persistance. Dès lors que l'on supprime la base de données, les données sont perdues. 

Votre objectif est donc de passer d'un Deployment pour la base de données à un StatefulSet et ainsi vérifier la persistance des données. 

Dans le compte rendu, il est attendu une démonstration de l'intérêt de la mise en place du StatefulSet par rapport au Deployment dans notre cas d'usage. 



