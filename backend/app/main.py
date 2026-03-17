from fastapi import FastAPI
from app.api import health
from app.api import scan

app = FastAPI(
    title="Pipeline Guardian",
    version="1.0.0"
)

# Register routes
app.include_router(health.router)
app.include_router(scan.router)


@app.get("/")
def root():
    return {"message": "Pipeline Guardian API is running"}