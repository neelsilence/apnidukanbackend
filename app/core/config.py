from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    APP_NAME: str = Field(default="Grocery Backend")
    DEBUG: bool = Field(default=True)
    SQLALCHEMY_DATABASE_URI: str = Field(default="sqlite:///./app.db")
    ALLOW_ORIGINS: list[str] = Field(default_factory=lambda: ["*"])

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
