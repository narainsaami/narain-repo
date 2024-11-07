# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/data")
async def hello():
    return {"message": "Hello! This is something."}
