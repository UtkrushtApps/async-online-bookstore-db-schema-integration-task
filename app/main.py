from fastapi import FastAPI
from app.routes import api

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

app.include_router(api.router)
