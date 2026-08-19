# Threat Modeling Studio

[![CI](https://github.com/koketseraphasha/threat-modeling-studio/actions/workflows/ci.yml/badge.svg)](https://github.com/koketseraphasha/threat-modeling-studio/actions/workflows/ci.yml)

A collaborative threat modeling platform for security teams. Perform STRIDE analysis, create data flow diagrams, assess risk ratings, and generate actionable recommendations.

## Features

- **STRIDE Analysis** — Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **Data Flow Diagrams** — Interactive diagram editor
- **Risk Ratings** — DREAD and CVSS-based scoring
- **Recommendations** — Automated mitigation suggestions
- **Collaboration** — Multi-user workspace
- **Export** — Generate threat model reports

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React + TypeScript + React Flow
- **Database:** PostgreSQL
- **Container:** Docker

## Quick Start

```bash
docker compose up -d
```

## Security

Defensive security tool. See [SECURITY.md](SECURITY.md).

## Author

**Koketso Raphasha** — Full-Stack Developer, AI Engineer, Cybersecurity Enthusiast

## Ethical Use Notice

This tool is built strictly for **educational and defensive cybersecurity purposes**.

It must only be used in:
- Controlled lab environments
- Authorized systems
- Security research contexts

**Unauthorized use is strictly prohibited.**
## Deployment & Architecture

This project is designed with cloud-ready principles:

- **Containerized** using Docker for consistent deployment
- **Environment-based configuration** — no hardcoded secrets
- **Modular structure** for independent scaling
- **Stateless design** where applicable
- **Separation of concerns** for maintainability

### Run Locally

`ash
docker-compose up --build
`

---

*Part of the Kirov Dynamics Technology portfolio — backend engineering focused on security, scalability, and system design.*


## Usage Instructions
Framework detected: Python
Open the HTML files directly in your browser or run a simple local web server (e.g. `npx serve` or `python -m http.server`).
