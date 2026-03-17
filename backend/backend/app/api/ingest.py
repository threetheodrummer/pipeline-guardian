from fastapi import APIRouter
from backend.app.core.models import Finding
from backend.app.core.scoring import score_finding

router = APIRouter()

@router.post("/")
def ingest_finding(finding: Finding):
    score = score_finding(finding)
    return {
        "id": finding.id,
        "severity": finding.severity,
        "score": score
    }
