from enum import Enum
from dataclasses import dataclass, asdict
from typing import List


class Severity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


@dataclass
class Finding:
    scanner: str
    file: str
    line: int
    issue: str
    severity: Severity

    def to_dict(self):
        data = asdict(self)
        data["severity"] = self.severity.value
        return data


@dataclass
class ScanReport:
    findings: List[Finding]

    def to_dict(self):
        return {
            "total_findings": len(self.findings),
            "findings": [f.to_dict() for f in self.findings]
        }