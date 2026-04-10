# TP 3 Exposons notre application sur Internet

## Objectifs du TP

- Exposer notre application sur le réseau du cluster
- Exposer notre application sur internet 

Livrables : 
- Manifest kubernetes pour déployer les applications 
- Un compte rendu avec les difficultés rencontrées, et les résultats de chaque exercice. 


## Prérequis

- Avoir un compte SSPCloud 
- Avoir déployé l'application du TP2

## Exposition sur le réseau du cluster

Votre objectif est maintenant d'exposer votre application sur le réseau interne au cluster.

Au précédent TP, il était impératif de rentrer à l'intérieur du pod pour tester notre application. Ici, nous voulons que notre application soit accessible depuis notre namespace. 

Dans le compte rendu de cet exercice, il faudra inclure les captures d'écran des commandes permettant :
- d'afficher l'adresse réseau de notre application 
- de montrer un test fonctionnel de notre application 

## Exposition sur internet

Dans cet exercice, nous allons plus loin. Vous voulez désormais offrir les services de votre magnifique application au monde entier en l'exposant sur internet. 

Dans le compte rendu de cet exercice, il faudra inclure les captures d'écran des commandes permettant :
- de lister les objets ingress,
- de montrer un test fonctionnel de notre application depuis votre poste de travail. 

PS : Les URL doivent toujours finir par `.lab.sspcloud.fr`

## Déploiement d'une application 3 tiers 

L'idée de ce TP est de déployer une application complète avec un frontend, un backend et une base de données.

Il faut donc refaire les différentes étapes du TP 2 et 3 afin d'exposer notre application. 

Les images à utiliser :
- hugosmn5/backend-3-tier:1.1
- hugosmn5/frontend-3-tier:1.1
- postgres:13

Les variables d'environnement à définir dans le backend : 
- name: DB_USER
value: "admin"
- name: DB_PASS
value: "password"
- name: DB
value: "reviews"
- name: DB_HOST
value: `Nom du service postgresql`

Et pour la base postgresql : 
- name: POSTGRES_USER
value: "admin"
- name: POSTGRES_PASSWORD
value: "password"
- name: POSTGRES_DB
    value: "reviews"


NB : L'application frontend se base entièrement sur le nom de service : `backend`.