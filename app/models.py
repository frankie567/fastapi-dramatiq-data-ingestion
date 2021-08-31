import uuid
from datetime import datetime
from typing import Optional

from pydantic import UUID4
from sqlmodel import Field, SQLModel


class DocumentInput(SQLModel):
    id: UUID4 = Field(default_factory=uuid.uuid4, primary_key=True)
    content: str


class Document(DocumentInput, table=True):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    category: Optional[str] = Field(default=None)
