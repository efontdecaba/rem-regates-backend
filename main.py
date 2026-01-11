import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db": result.scalar()}
