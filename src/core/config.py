from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_URL_ALEMBIC: str
    DEBUG: bool

    class Config:
        env_file = '.env'


settings = Settings()
