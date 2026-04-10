# Amélioration de notre application 3 tiers 

L'idée de ce TP est de reprendre notre application 3 tiers afin de l'améliorer en ajoutant des objets Kubernetes en plus. 

Voici des axes d'amélioration que vous pouvez explorer : 
- Création d'objet secret pour stocker les informations sensibles (username/password),
- Mise en place d'un init container pour alimenter la base de données de l'application,
- Mise en place de probes pour assurer la disponibilité de notre application, 
- Mise en place de ressources afin d'implémenter une QoS : Guaranteed. 
- Mise en place d'un headless service pour la base de données. 

Pour les plus motivés : 
- Mise en place de clustering sur les bases de données postgresql : Cette partie peut être assez longue à réaliser mais peut être un petit projet annexe pour découvrir le monde des bases de données et leur déploiement dans le cloud. 

Comme pour les autres TP, un compte rendu explicitant la démarche sera attendu.
