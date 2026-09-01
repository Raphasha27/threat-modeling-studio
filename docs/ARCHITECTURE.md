# Threat Modeling Studio — Architecture

## System Overview

Threat Modeling Studio is a collaborative security analysis platform built for teams to perform structured STRIDE threat analysis, visualise data flow diagrams, assess risk ratings, and generate actionable mitigation recommendations. It provides an API-first design with an interactive UI for real-time threat modelling sessions.

## Architecture Diagram

```
┌─────────────────┐
│   React UI      │
│ (Static/SPA)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│   FastAPI       │────►│  SQLAlchemy      │
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

## Technology Stack

| Component      | Technology        | Version |
|----------------|-------------------|---------|
| Language       | Python            | 3.12    |
| Framework      | FastAPI           | —       |
| ORM            | SQLAlchemy        | —       |
| Templates      | Jinja2            | —       |
| Validation     | Pydantic          | —       |
| Testing        | pytest            | —       |
| Linting        | ruff              | —       |
| Container      | Docker            | —       |

## Directory Structure

```
threat-modeling-studio/
├── src/
│   ├── main.py          # FastAPI application entry point
│   ├── routes.py        # API route definitions
│   ├── models.py        # Pydantic data models (Threat, STRIDE, DREAD)
│   └── config.py        # Configuration management
├── tests/               # pytest test suite
├── docs/                # Documentation
├── index.html           # Static frontend (SPA)
├── Dockerfile           # Container build
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project metadata
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

## Data Flow

### STRIDE Analysis
1. User creates a threat model via API or UI.
2. System generates STRIDE categories (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege).
3. Each threat is classified, scored using DREAD/CVSS, and assigned severity.
4. Mitigation recommendations auto-generated from threat-to-control mapping.

### Data Flow Diagrams
1. User defines components, data stores, processes, and trust boundaries.
2. System renders interactive DFD with trust boundary visualization.
3. Threats associated with each data flow element.

### Risk Assessment
1. DREAD scoring: Damage, Reproducibility, Exploitability, Affected Users, Discoverability.
2. CVSS vector scoring for technical severity.
3. Risk matrix maps scores to severity levels (Critical/High/Medium/Low).

## Security

- **Defensive tool only**: Designed for authorized security assessments.
- **No live exploitation**: No network scanning, exploitation, or unauthorized access.
- **Input validation**: Pydantic models validate all threat data.
- **Environment variables**: Configuration loaded from env, not hardcoded.

## Deployment

### Docker

```bash
docker build -t threat-modeling-studio .
docker run -p 8000:8000 threat-modeling-studio
```

### Local Development

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

### API Endpoints

| Method | Path                          | Description                     |
|--------|-------------------------------|---------------------------------|
| GET    | `/`                           | Service status                  |
| GET    | `/health`                     | Health check                    |
| GET    | `/api/v1/models`              | List all threat models          |
| GET    | `/api/v1/models/{id}/stride`  | Get STRIDE analysis             |
| GET    | `/api/v1/models/{id}/flows`   | Get data flow diagrams          |

## Scaling Considerations

- **Database**: SQLite for single-user; PostgreSQL for team collaboration.
- **Real-time collaboration**: Add WebSocket for live multi-user threat modeling sessions.
- **Export**: PDF/Markdown export for compliance reports.
- **Integration**: Webhook support for SIEM/ticketing systems (Jira, ServiceNow).
- **Multi-tenancy**: Add workspace isolation for enterprise teams.
- **Caching**: Cache frequently accessed threat models and mitigation databases.

## Decision Records

| Decision | Rationale |
|----------|-----------|
| STRIDE over PASTA | STRIDE is industry-standard, simpler to implement, widely understood |
| DREAD + CVSS | DREAD for quick risk assessment; CVSS for technical severity standard |
| FastAPI over Django | Lightweight, auto-generated docs, async support for concurrent sessions |
| SQLAlchemy ORM | Mature Python ORM; easy migration from SQLite to PostgreSQL |
| Jinja2 for HTML | Server-side rendering for SEO-friendly documentation pages |
| API-first design | Enables future mobile/desktop clients; UI is one consumer of many |
