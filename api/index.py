# api/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API online"}

@app.get("/produtos")
def get_produtos():
    return {"produto": "Produto Exemplo", "id": 1}