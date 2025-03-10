from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import obtener_respuesta


app = FastAPI()

# Modelo para recibir la solicitud
class MessageRequest(BaseModel):
    message: str

# Endpoint para recibir mensajes y devolver respuestas
@app.post("/chatbot/")
async def chat(request: MessageRequest):
    respuesta = obtener_respuesta(request.message)
    return {"response": respuesta}