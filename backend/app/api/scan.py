from fastapi import APIRouter
from app.scanner.engine import run_full_scan

router = APIRouter(prefix="/scan", tags=["Scan"])


@router.post("/")
def run_scan():
    target = "test_repo"
    report = run_full_scan(target)
    return report.to_dict()