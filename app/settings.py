from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    database_url: str = "sqlite://database.db"
    redis_url: RedisDsn

    class Config:
        env_file = ".env"


settings = Settings()
