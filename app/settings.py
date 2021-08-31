from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    database_dsn: str = "sqlite://database.db"
    redis_dsn: RedisDsn

    class Config:
        env_file = ".env"


settings = Settings()
