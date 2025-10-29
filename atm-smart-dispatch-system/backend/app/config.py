"""
Application configuration settings.

This module loads settings from environment variables.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Defines the application settings.
    """
    ELASTICSEARCH_URL: str = "http://localhost:9200"
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"

settings = Settings()
