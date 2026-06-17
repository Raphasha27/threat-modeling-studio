# Threat Modeling Studio API

| Method | Path                          | Description              |
|--------|-------------------------------|--------------------------|
| GET    | /                             | Root health check        |
| GET    | /health                       | Health status            |
| GET    | /api/v1/models                | List threat models       |
| GET    | /api/v1/models/{id}/stride    | Get STRIDE analysis      |
| GET    | /api/v1/models/{id}/flows     | Get data flow diagrams   |
