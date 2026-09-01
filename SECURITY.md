# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | :white_check_mark: Active |
| < Latest | :x: No |

Always use the latest version to receive security patches and improvements.

---

## Reporting a Vulnerability

The Threat Modeling Studio team takes security seriously. We appreciate your efforts to responsibly disclose any security concerns.

**Please do NOT report security vulnerabilities through public GitHub issues.**

### Step-by-Step Reporting Process

1. **Identify the vulnerability** — Document the issue with clear reproduction steps.
2. **Email the security team** at **raphasha27@github.com** with the following:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
   - Suggested fix (if any)
3. **Wait for acknowledgment** — You will receive a response within **48 hours**.
4. **Collaborate on the fix** — We may reach out for additional details.
5. **Disclosure** — We will coordinate a public disclosure timeline with you.

### What to Include

- Type of vulnerability (e.g., data leakage, API abuse, input validation)
- Affected component and version
- Attack vector and prerequisites
- Proof of concept (if available)
- Your suggested remediation

---

## Security Response Timeline

| Phase | Timeframe |
|-------|-----------|
| Initial acknowledgment | 48 hours |
| Severity assessment | 5 business days |
| Patch development | 10–15 business days |
| Coordinated disclosure | 30 days after fix |

---

## Intended Use

This project is designed for:

- **Education** — Learning threat modeling methodologies
- **Research** — Academic and industry security research
- **Defensive Security** — Identifying and mitigating threats
- **Security Awareness** — Training teams on threat analysis
- **Penetration Testing** — Only in authorized environments

## Prohibited Use

- **Unauthorized Access** — Accessing systems without permission
- **Credential Theft** — Stealing or harvesting credentials
- **Malware Distribution** — Creating or spreading malicious software
- **Denial of Service** — Intentionally disrupting services
- **Surveillance** — Monitoring unsuspecting users
- **Any illegal activity** — Any use violating applicable laws

---

## Security Design

This project implements the following security measures:

- **Environment Variables** — No hardcoded secrets or API keys
- **Input Validation** — Pydantic models validate all API inputs
- **CORS Configuration** — Restricted to trusted origins
- **Dependency Scanning** — Automated vulnerability checks in CI
- **No Persistent Storage** — Analysis data is ephemeral by default

---

## Security Best Practices for Users

When deploying or developing with Threat Modeling Studio:

### Configuration
- Always use **environment variables** for API keys
- Never commit `.env` files or secrets to version control
- Restrict API access to trusted networks
- Use Docker for isolated deployments

### Data Protection
- Threat models may contain sensitive system information — ensure proper access controls
- Use encrypted storage for threat analysis data in production
- Audit access to threat models regularly
- Consider classifying threat models by sensitivity level

### Network
- Deploy behind a reverse proxy with TLS termination
- Enable CORS only for trusted frontend origins
- Use HTTPS for all API communications

### Dependencies
- Run `pip audit` for Python dependency vulnerabilities
- Enable Dependabot alerts for automatic vulnerability notifications
- Review dependency updates before merging

---

## Dependency Management

### Python Dependencies

```bash
# Check for known vulnerabilities
pip install pip-audit
pip-audit

# Update dependencies
pip install --upgrade -r requirements.txt
```

### Automated Scanning

- **Dependabot** is enabled for automatic dependency update PRs.
- **CI pipeline** runs `pip-audit` on every PR.
- Review and merge Dependabot PRs promptly.

---

## Responsible Disclosure

We follow [coordinated disclosure](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) principles:

- Report vulnerabilities privately before public disclosure.
- We will credit reporters in release notes (unless anonymity is preferred).
- We ask that you do not exploit the vulnerability beyond what is necessary to demonstrate it.
- We will not pursue legal action against researchers who follow this policy.

---

## Compliance

This project complies with responsible disclosure standards. Use only in isolated, authorized environments.

---

## Contact

- **Security Email**: raphasha27@github.com
- **General Issues**: [GitHub Issues](../../issues)

Thank you for helping keep Threat Modeling Studio and its users safe.
