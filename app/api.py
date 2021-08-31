from fastapi import FastAPI, HTTPException, status
from pydantic import UUID4
from sqlmodel import Session

from app import models
from app.db import create_db_and_tables, engine
from app.worker import ingest_document

app = FastAPI()


@app.post(
    "/documents",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=models.DocumentInput,
)
def add_document(document: models.DocumentInput):
    ingest_document.send(document.json())
    return document


@app.get("/documents/{id:uuid}", response_model=models.Document)
def get_document(id: UUID4):
    with Session(engine) as session:
        document = session.get(models.Document, id)
        if not document:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return document


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
