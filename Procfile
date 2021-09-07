web: uvicorn app.api:app --host 0.0.0.0 --port $PORT
worker: dramatiq -p 4 -t 4 app.worker
