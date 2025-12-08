from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "FastAPI Async Microservices Starter Running 🚀"}
