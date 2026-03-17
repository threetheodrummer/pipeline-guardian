import re
from app.scanner.models import Finding, Severity
from app.scanner.utils import get_all_files


SECRET_PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS Key", Severity.CRITICAL),
    (r"(?i)password\s*=\s*['\"].+['\"]", "Hardcoded password", Severity.HIGH),
]


def run_secrets_scan(target_dir):
    findings = []

    files = get_all_files(target_dir)

    for file in files:
        try:
            with open(file, "r", errors="ignore") as f:
                for i, line in enumerate(f, start=1):
                    for pattern, issue, severity in SECRET_PATTERNS:
                        if re.search(pattern, line):
                            findings.append(
                                Finding(
                                    scanner="Secrets",
                                    file=file,
                                    line=i,
                                    issue=issue,
                                    severity=severity
                                )
                            )
        except Exception:
            continue

    return findings