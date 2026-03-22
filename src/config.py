"""
Multi-Agent AI System - Configuration Module.
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings."""

    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    serper_api_key: str = Field(default="", env="SERPER_API_KEY")
    model_name: str = Field(default="gpt-4o-mini", env="MODEL_NAME")
    temperature: float = Field(default=0.7, env="TEMPERATURE")
    max_iterations: int = Field(default=15, env="MAX_ITERATIONS")
    verbose: bool = Field(default=True, env="VERBOSE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()
