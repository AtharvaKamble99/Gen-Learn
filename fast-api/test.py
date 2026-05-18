from fastapi import FastAPI,Body
from ollama import Client

client = Client(
    host = "http://localhost:11434",

)

app = FastAPI()

@app.get("/")
def homepage():
    return{"Hello Jew :🪙"}


@app.post("/chat")
def chat(
    message: str = Body(...,description="The Message")
):
    response= client.chat(model="phi3:3.8b",messages=[
        {"role":"user","content":message}
    ])

    return {"response" : response.message.content}