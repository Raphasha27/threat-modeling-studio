from fastapi import FastAPI
from src.routes import router

app = FastAPI(title="Threat Modeling Studio", version="0.1.0")
app.include_router(router)


@app.get("/")
async def root():
    return {"service": "threat-modeling-studio", "status": "running", "version": "0.1.0"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
