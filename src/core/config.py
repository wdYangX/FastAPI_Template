import os
import secrets
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator
from dotenv import load_dotenv
from pathlib import Path


class Settings(BaseSettings):
    env_path = Path('.') / 'dev.env'
    load_dotenv(dotenv_path=env_path)
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME = "FastAPITemplate"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    DB_PORT: str = os.getenv("DB_PORT")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI  = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True


settings = Settings()