import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text

app = FastAPI()

def get_engine():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set")
    return create_engine(db_url, pool_pre_ping=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    engine = get_engine()
    with engine.connect() as conn:
        return {"db": conn.execute(text("SELECT 1")).scalar()}
