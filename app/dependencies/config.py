from enum import Enum
from collections import namedtuple
from pydantic import BaseSettings, validator


class AppEnv(str, Enum):
    """Application environment."""

    none = ''
    dev = 'dev'
    prod = 'prod'
    test = 'test'


class Settings(BaseSettings):
    """Application settings."""

    database_url: str
    app_env: AppEnv = AppEnv.none

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @validator('database_url')
    def postgres_dialect(cls, value):
        if value.startswith('postgres://'):
            value = value.replace('postgres://', 'postgresql://', 1)
        return value


SETTINGS = Settings()
ColValue = namedtuple('ColValue', ['column', 'value'])
