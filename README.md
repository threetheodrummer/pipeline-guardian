# Pipeline Guardian

Pipeline Guardian is an enterprise-grade DevSecOps pipeline that enforces
security controls directly inside CI/CD.

## Phase 1 – CI, Secrets & SAST

### Security Controls Implemented
- GitHub Actions CI
- Secrets detection using Gitleaks
- SAST using Semgrep
- Hard-fail enforcement
- Audit artifacts via GitHub Actions

### Failure Conditions
- Secrets committed to the repository
- High/Critical SAST findings

This project mirrors real-world DevSecOps practices used in
regulated and security-first organizations.
