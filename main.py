from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    nome: str
    idade: int

@app.post("/processar")
def processar(data: InputData):
    return {
        "mensagem": f"{data.nome} tem {data.idade} anos.",
        "ok": True
    }