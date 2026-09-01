# Threat Modeling Studio — API Documentation

> STRIDE-based threat modeling API for systematically identifying and cataloguing security threats in software architectures.

## Base URL

```
http://localhost:8000
```

## Overview

This API implements the **STRIDE** threat classification framework:

| Category | Description |
|----------|-------------|
| **S**poofing | Impersonation of users or systems |
| **T**ampering | Unauthorized modification of data |
| **R**epudiation | Denial of actions without proof |
| **I**nformation Disclosure | Exposure of sensitive data |
| **D**enial of Service | Disruption of availability |
| **E**levation of Privilege | Unauthorized access escalation |

---

## Endpoints

### Health & Info

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Service status and version |
| `GET` | `/health` | Health check |

### Threat Models

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/v1/models` | List all threat models |
| `GET` | `/api/v1/models/{model_id}/stride` | Get STRIDE analysis for a model |
| `GET` | `/api/v1/models/{model_id}/flows` | Get data flow diagrams for a model |

---

## Example Requests

### List Threat Models

```bash
curl http://localhost:8000/api/v1/models
```

**Response:**
```json
[
  {
    "id": "TM-001",
    "name": "Web Application Threat Model",
    "methodology": "STRIDE",
    "risk_rating": "high",
    "description": "Threat model for customer-facing web application",
    "created_at": "2025-01-15T10:30:00Z"
  }
]
```

### Get STRIDE Analysis

```bash
curl http://localhost:8000/api/v1/models/TM-001/stride
```

**Response:**
```json
[
  {
    "category": "Spoofing",
    "threat": "Attacker impersonates legitimate user via stolen session token",
    "mitigation": "Implement MFA and short-lived JWT tokens",
    "risk_score": 8
  },
  {
    "category": "Tampering",
    "threat": "API request modification in transit",
    "mitigation": "Enforce HTTPS with certificate pinning",
    "risk_score": 7
  },
  {
    "category": "Information Disclosure",
    "threat": "Database error messages expose schema details",
    "mitigation": "Implement generic error responses and input validation",
    "risk_score": 6
  }
]
```

### Get Data Flows

```bash
curl http://localhost:8000/api/v1/models/TM-001/flows
```

**Response:**
```json
[
  {
    "id": "DF-01",
    "source": "Browser",
    "destination": "API Gateway",
    "protocol": "HTTPS",
    "data_classification": "sensitive",
    "trust_boundary": true
  },
  {
    "id": "DF-02",
    "source": "API Gateway",
    "destination": "Application Server",
    "protocol": "HTTP",
    "data_classification": "sensitive",
    "trust_boundary": false
  }
]
```

---

## Interactive Docs

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI Spec:** [`docs/api-spec.yaml`](./api-spec.yaml)
