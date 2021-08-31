from app.predict import CategoryPrediction
from datetime import datetime

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from sqlmodel import Session

from app.db import engine
from app.models import Document, DocumentInput
from app.settings import settings

redis_broker = RedisBroker(url=settings.redis_url)
dramatiq.set_broker(redis_broker)


category_prediction = CategoryPrediction()


@dramatiq.actor
def ingest_document(document_json: str):
    document = DocumentInput.parse_raw(document_json)
    with Session(engine) as session:
        document_db = session.get(Document, document.id)
        if document_db is None:
            document_db = Document(**document.dict())
        else:
            document_dict = document.dict(exclude_unset=True)
            for key, value in document_dict.items():
                setattr(document_db, key, value)

        document_db.category = category_prediction.predict(document_db.content)
        document_db.updated_at = datetime.utcnow()

        session.add(document_db)
        session.commit()
