from fastapi import FastAPI
from backend.app.api import ingest, risk

app = FastAPI(title="Pipeline Guardian Backend")

app.include_router(ingest.router)
app.include_router(risk.router)

@app.get("/health")
def health():
    return {"status": "ok"}
