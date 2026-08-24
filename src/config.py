"""Application settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Threat Modeling Studio"
    version: str = "0.1.0"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/tms"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
