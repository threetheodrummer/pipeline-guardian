from fastapi import APIRouter
from backend.app.core.scoring import calculate_risk

router = APIRouter()

@router.get("/")
def risk_summary():
    return calculate_risk()
