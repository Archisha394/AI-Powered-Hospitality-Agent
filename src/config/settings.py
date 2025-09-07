from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List

class Settings(BaseSettings):
    # === Core App ===
    APP_ENV: str = "dev"
    APP_NAME: str = "AI Hospitality Agent"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # === Google ADK / Gemini Stub ===
    GOOGLE_ADK_API_KEY: str | None = None

    # === GCP / BigQuery (optional) ===
    GCP_PROJECT_ID: str | None = None
    BIGQUERY_DATASET: str | None = None
    BIGQUERY_TABLE_ANALYTICS: str | None = None

    # === Security ===
    CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
