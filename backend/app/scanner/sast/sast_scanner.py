import re
from app.scanner.models import Finding, Severity
from app.scanner.utils import get_all_files


DANGEROUS_PATTERNS = [
    (r"eval\(", "Use of eval()", Severity.CRITICAL),
    (r"exec\(", "Use of exec()", Severity.CRITICAL),
    (r"os\.system\(", "Command injection risk", Severity.HIGH),
]


def run_sast_scan(target_dir):
    findings = []

    files = get_all_files(target_dir, [".py"])

    for file in files:
        try:
            with open(file, "r", errors="ignore") as f:
                for i, line in enumerate(f, start=1):
                    for pattern, issue, severity in DANGEROUS_PATTERNS:
                        if re.search(pattern, line):
                            findings.append(
                                Finding(
                                    scanner="SAST",
                                    file=file,
                                    line=i,
                                    issue=issue,
                                    severity=severity
                                )
                            )
        except Exception:
            continue

    return findings