from app.scanner.sast.sast_scanner import run_sast_scan
from app.scanner.dependency.dependency_scanner import run_dependency_scan
from app.scanner.secrets.secrets_scanner import run_secrets_scan
from app.scanner.models import ScanReport


def run_full_scan(target_dir):
    findings = []

    findings.extend(run_sast_scan(target_dir))
    findings.extend(run_dependency_scan(target_dir))
    findings.extend(run_secrets_scan(target_dir))

    return ScanReport(findings=findings)