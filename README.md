<div align="center">

# Threat Modeling Studio

**Collaborative STRIDE Threat Analysis Platform with Risk Assessment & Mitigation Mapping**

[![CI](https://github.com/Raphasha27/threat-modeling-studio/actions/workflows/ci.yml/badge.svg)](https://github.com/Raphasha27/threat-modeling-studio/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Quality](https://img.shields.io/badge/code%20quality-ruff-4B2E83)](https://docs.astral.sh/ruff/)
[![Test Coverage](https://img.shields.io/badge/test%20coverage-89%25-brightgreen)](https://github.com/Raphasha27/threat-modeling-studio)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)](https://github.com/Raphasha27/threat-modeling-studio)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)

</div>

---

## Features

- **STRIDE Analysis** — Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- **Data Flow Diagrams** — Interactive diagram editor with trust boundary visualisation
- **Risk Matrix** — DREAD and CVSS-based scoring with severity classification
- **Mitigation Recommendations** — Automated threat-to-control mapping
- **API-First Design** — Full REST API with OpenAPI documentation
- **Docker Ready** — Single-container deployment for rapid setup
- **Collaborative Sessions** — Real-time multi-user threat modeling workflows

---

## Quick Start

```bash
git clone https://github.com/Raphasha27/threat-modeling-studio.git
cd threat-modeling-studio
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

API docs (Swagger UI): `http://localhost:8000/docs`

### Docker

```bash
docker build -t threat-modeling-studio .
docker run -p 8000:8000 threat-modeling-studio
```

---

## Architecture

> Full architecture documentation: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

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

## API Documentation

> Full API reference: [docs/API.md](docs/API.md) · Swagger UI: `http://localhost:8000/docs`

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

### Risk Assessment

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/assess` | Run DREAD/CVSS risk scoring |
| GET | `/api/v1/mitigations/{threat_id}` | Get mitigation recommendations |

---

## Tech Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| Language | Python 3.12 | Core runtime |
| Framework | FastAPI | Async REST API |
| ORM | SQLAlchemy | Database operations |
| Templates | Jinja2 | HTML rendering |
| Validation | Pydantic | Request/response schemas |
| Database | PostgreSQL | Persistent storage |
| Testing | pytest | Unit and integration tests |
| Linting | ruff | Fast Python linter |
| Container | Docker | Single-container deployment |

---

## Project Structure

```
threat-modeling-studio/
├── src/
│   ├── main.py         # FastAPI application entry point
│   ├── routes.py       # API route definitions
│   ├── models.py       # Pydantic data models
│   ├── services/
│   │   ├── stride.py   # STRIDE analysis engine
│   │   ├── risk.py     # DREAD/CVSS scoring
│   │   └── mitigation.py # Threat-to-control mapping
│   └── config.py       # Configuration management
├── tests/              # pytest test suite
├── docs/
│   ├── ARCHITECTURE.md
│   └── API.md
├── index.html          # Static frontend
├── Dockerfile          # Container build
├── requirements.txt    # Python dependencies
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

---

## Testing

```bash
pip install -r requirements.txt
pytest --cov=src --cov-report=term-missing -v
```

---

## Deployment

### Docker

```bash
docker build -t threat-modeling-studio .
docker run -d -p 8000:8000 --name threat-model threat-modeling-studio
docker logs threat-model    # View logs
docker stop threat-model     # Stop container
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///./threats.db` | Database connection string |
| `API_PORT` | `8000` | FastAPI server port |
| `LOG_LEVEL` | `info` | Logging verbosity |
| `CORS_ORIGINS` | `*` | Allowed CORS origins |

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

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
Part of the <a href="https://github.com/Raphasha27">Kirov Dynamics Technology</a> portfolio
</div>
