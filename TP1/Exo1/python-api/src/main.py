# Fichier de base que je n'ai pas touché mais que je vais un peu commenter : 
# On utilise fastapi pour faire appel à l'API python pour faire un HelloWorld
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return "world"
