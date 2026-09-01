from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Threat Modeling Studio",
    description=(
        "STRIDE-based threat modeling API for systematically identifying and "
        "cataloguing security threats in software architectures.\n\n"
        "## Features\n"
        "- **Threat Models** — List and manage threat model definitions\n"
        "- **STRIDE Analysis** — Retrieve categorized threat entries with mitigations\n"
        "- **Data Flow Mapping** — Document data flows and trust boundaries\n\n"
        "## Methodology\n"
        "This API implements the **STRIDE** threat classification framework:\n"
        "- **S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, "
        "**D**enial of Service, **E**levation of Privilege"
    ),
    version="0.1.0",
    contact={
        "name": "Threat Modeling Studio Support",
        "url": "https://github.com/Raphasha27/threat-modeling-studio",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "threats",
            "description": "Threat model listing, STRIDE analysis, and data flow mapping",
        },
        {"name": "Health", "description": "Service health checks"},
    ],
)
app.include_router(router)


@app.get("/")
async def root():
    return {
        "service": "threat-modeling-studio",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}
