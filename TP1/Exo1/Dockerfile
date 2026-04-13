# On part d'une image de base de python qui contient toute les dépendances nécessaire pour le reste de notre projet
FROM python:3.13-slim

# on se palce dans le dossier app pour les prochaines commandes du dockerfile
WORKDIR /app

# On copie tout, ce n'est pas optimale (si il y a un changement dnas le code mais pas dans les dépendances on re-charge toute l'image mais on verra l'optimisation plus tard)
COPY . .

# On installe les requirements mais on vide le cache car d'une part ce n'est pas utile d'autres part ça prends de la place en stockage
RUN pip install --no-cache-dir -r python-api/requirements.txt

#Port choisi totalement au hasard
EXPOSE 8081

# Comme on utilise FastApi, on se met d'abord sur Uvicorn, pour pourvoir l'utiliser. 
ENTRYPOINT ["uvicorn", "python-api.src.main:app","--host", "0.0.0.0", "--port", "8081"]