# Contributing to Threat Modeling Studio

Welcome and thank you for your interest in contributing to **Threat Modeling Studio**! Every contribution helps make security threat analysis better for everyone.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Architecture Reference](#architecture-reference)
- [Release Process](#release-process)

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code. Please report unacceptable behavior to **raphasha27@github.com**.

---

## Development Setup

### Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12+ | Backend runtime |
| Node.js | 18+ | Frontend (if applicable) |
| Docker | 24.x+ | Containerized development |

### Step-by-Step Setup

1. **Fork and clone** the repository:
   ```bash
   git clone https://github.com/<your-username>/threat-modeling-studio.git
   cd threat-modeling-studio
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server**:
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

5. **Verify the API**:
   - Swagger UI: `http://localhost:8000/docs`

6. **Run linter locally** (optional):
   ```bash
   ruff check .
   ruff format .
   ```

---

## Code Style Guidelines

### Python (FastAPI)

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide.
- Use **Ruff** for linting and formatting — CI enforces this.
- Maximum line length: **88 characters**.
- Use type hints on all function signatures.
- Prefer async/await for I/O-bound operations.

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Functions | `snake_case` | `analyze_threat` |
| Classes | `PascalCase` | `STRIDEAnalyzer` |
| Constants | `UPPER_SNAKE_CASE` | `THREAT_CATEGORIES` |
| API routes | `kebab-case` | `/api/v1/threats` |
| Database columns | `snake_case` | `created_at` |

### Security-Specific Guidelines

- Use STRIDE methodology consistently for threat classification.
- Document threat rationale — why severity scores are assigned.
- Follow DREAD/CVSS scoring standards.
- Ensure data flow diagrams accurately represent trust boundaries.

### General

- Write meaningful variable and function names.
- Add docstrings for all public functions and classes.
- Keep functions focused and under 40 lines.
- No hardcoded secrets — use environment variables.

---

## Testing Requirements

| Type | Framework | Coverage Target |
|------|-----------|-----------------|
| Unit tests | pytest | 85%+ |
| Threat analysis tests | pytest | All STRIDE categories |
| API tests | FastAPI TestClient | All endpoints |

- Every new feature **must** include tests.
- Bug fixes **must** include a regression test.
- Run the full test suite before pushing:
  ```bash
  pytest tests/ -v --cov=src --cov-report=term-missing
  ```
- Test threat analysis accuracy against known threat models.

---

## Pull Request Process

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines above.

3. **Write or update tests** to cover your changes.

4. **Commit with a conventional message**:
   ```
   feat: add STRIDE threat categorization
   fix: correct DREAD scoring calculation
   docs: update threat modeling methodology documentation
   test: add tests for mitigation mapping
   chore: update FastAPI dependencies
   ```

5. **Push and open a PR** against `main`.

6. **PR checklist** (all must pass before merge):
   - [ ] CI pipeline passes (linting, tests, Docker build)
   - [ ] Code reviewed by at least one maintainer
   - [ ] No merge conflicts with `main`
   - [ ] Documentation updated (if applicable)
   - [ ] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)

---

## Issue Guidelines

### Bug Reports

- Check [existing issues](../../issues) first to avoid duplicates.
- Include a clear, descriptive title.
- Provide steps to reproduce, expected vs. actual behavior.
- Include environment details: Python version, OS.
- Attach error logs if relevant.

### Feature Requests

- Describe the feature and its motivation.
- Explain the use case for threat modeling workflows.
- Propose an implementation approach if possible.

### Labels

| Label | Description |
|-------|-------------|
| `bug` | Something is broken |
| `enhancement` | New feature or improvement |
| `good-first-issue` | Ideal for first-time contributors |
| `security` | Security-related concern |
| `help-wanted` | Community help appreciated |

---

## Architecture Reference

For detailed system design, data flow diagrams, and component interactions, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

Key components to understand:
- **STRIDE Analyzer** — Spoofing, Tampering, Repudiation, Info Disclosure, DoS, EoP
- **Risk Matrix** — DREAD and CVSS-based scoring
- **Mitigation Engine** — Automated threat-to-control mapping
- **FastAPI Server** — REST API with OpenAPI documentation

---

## Release Process

1. All changes merge to `main` via PR with passing CI.
2. Semantic versioning is used: `MAJOR.MINOR.PATCH`.
3. Tags are created for each release: `git tag v1.x.x`.
4. Docker images are built and published automatically via CI.
5. Release notes are generated from conventional commit messages.

---

## Questions?

Open a [discussion](../../discussions) or reach out to **raphasha27@github.com**.

Thank you for contributing to Threat Modeling Studio!
