from fastapi import FastAPI, Query
from database.db import SessionLocal
from database.models import Job
from database.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()