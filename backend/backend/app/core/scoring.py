from backend.app.core.models import Finding

def score_finding(finding: Finding) -> int:
    mapping = {
        "low": 10,
        "medium": 40,
        "high": 70,
        "critical": 100
    }
    return mapping.get(finding.severity.lower(), 0)

def calculate_risk():
    return {
        "risk_level": "medium",
        "score": 42
    }
