# Threat Modeling Studio

### Collaborative STRIDE Threat Analysis Platform

<div align="center">

[![CI](https://github.com/koketseraphasha/threat-modeling-studio/actions/workflows/ci.yml/badge.svg)](https://github.com/koketseraphasha/threat-modeling-studio/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-a78bfa?style=flat-square)

</div>

---

## Overview

Threat Modeling Studio is a **collaborative security analysis platform** built for teams to perform structured STRIDE threat analysis, visualise data flow diagrams, assess risk ratings, and generate actionable mitigation recommendations. It provides a clean API-first design with an interactive UI for real-time threat modelling sessions.

> Built for defensive cybersecurity — educational and authorised use only.

---

## Features

- [x] STRIDE Analysis — Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- [x] Data Flow Diagrams — Interactive diagram editor with trust boundary visualisation
- [x] Risk Matrix — DREAD and CVSS-based scoring with severity classification
- [x] Mitigation Recommendations — Automated threat-to-control mapping
- [x] API-First Design — Full REST API with OpenAPI documentation
- [x] Docker Ready — Single-container deployment

---

## Architecture

```
┌─────────────────┐
│   React UI      │
│ (Static/SPA)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│   FastAPI       │────▶│  SQLAlchemy      │
│   :8000         │     │  ORM Layer       │
└────────┬────────┘     └────────┬────────┘
         │                       │
         │                ┌──────▼──────┐
         │                │  PostgreSQL  │
         │                │  (persistent)│
         │                └─────────────┘
         │
    ┌────▼────────────┐
    │  Jinja2 Templates│
    │  (HTML Rendering)│
    └─────────────────┘
```

---

## Quick Start

### Using pip + uvicorn

```bash
git clone https://github.com/koketseraphasha/threat-modeling-studio.git
cd threat-modeling-studio
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

### Using Docker

```bash
docker build -t threat-modeling-studio .
docker run -p 8000:8000 threat-modeling-studio
```

API docs available at `http://localhost:8000/docs`

---

## API Endpoints

### System

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Service status |
| GET | `/health` | Health check |

### Threat Models

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/models` | List all threat models |
| GET | `/api/v1/models/{id}/stride` | Get STRIDE analysis for a model |
| GET | `/api/v1/models/{id}/flows` | Get data flow diagrams for a model |

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Templates | Jinja2 |
| Validation | Pydantic |
| Testing | pytest |
| Linting | ruff |
| Container | Docker |

---

## Project Structure

```
threat-modeling-studio/
├── src/
│   ├── main.py         # FastAPI application entry point
│   ├── routes.py       # API route definitions
│   ├── models.py       # Pydantic data models
│   └── config.py       # Configuration management
├── tests/              # pytest test suite
├── docs/               # Documentation
├── index.html          # Static frontend
├── Dockerfile          # Container build
├── requirements.txt    # Python dependencies
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

---

## Security

This is a defensive security tool. See [SECURITY.md](SECURITY.md) for responsible disclosure guidelines.

---

## Ethical Use Notice

This tool is built strictly for **educational and defensive cybersecurity purposes**.

It must only be used in:
- Controlled lab environments
- Authorised systems
- Security research contexts

**Unauthorised use is strictly prohibited.**

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) and open an issue before submitting a PR.

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
Part of the <a href="https://github.com/Raphasha27">Kirov Dynamics Technology</a> portfolio
</div>
