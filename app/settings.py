from pydantic import BaseSettings, RedisDsn, validator


class Settings(BaseSettings):
    database_url: str = "sqlite://database.db"
    redis_url: RedisDsn
    loader_io_verification_token: str = "DUMMY_TOKEN"

    class Config:
        env_file = ".env"

    @validator("database_url")
    def replace_postgres_scheme(cls, url: str) -> str:
        """
        Ensures scheme is compatible with newest version of SQLAlchemy.
        Ref: https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
        """
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql://", 1)
        return url


settings = Settings()
