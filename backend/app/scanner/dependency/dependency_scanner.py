import os
from app.scanner.models import Finding, Severity


VULNERABLE_PACKAGES = {
    "django==1.2": ("Outdated Django", Severity.CRITICAL),
    "flask==0.12": ("Old Flask", Severity.HIGH),
}


def run_dependency_scan(target_dir):
    findings = []

    req_file = os.path.join(target_dir, "requirements.txt")

    if not os.path.exists(req_file):
        return findings

    with open(req_file, "r") as f:
        for i, line in enumerate(f, start=1):
            pkg = line.strip()

            if pkg in VULNERABLE_PACKAGES:
                issue, severity = VULNERABLE_PACKAGES[pkg]

                findings.append(
                    Finding(
                        scanner="Dependency",
                        file="requirements.txt",
                        line=i,
                        issue=issue,
                        severity=severity
                    )
                )

    return findings