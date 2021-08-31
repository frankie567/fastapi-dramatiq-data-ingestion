from sqlmodel import SQLModel, create_engine

from app.settings import settings

engine = create_engine(settings.database_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
