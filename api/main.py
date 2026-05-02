from fastapi import FastAPI
from database.db import SessionLocal
from database.models import Job
from database.init_db import init_db   # ✅ REQUIRED

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()   # ✅ REQUIRED

@app.get("/jobs")
def get_jobs(page: int = 1, page_size: int = 5):
    session = SessionLocal()

    offset = (page - 1) * page_size
    jobs = session.query(Job).offset(offset).limit(page_size).all()

    result = []
    for job in jobs:
        result.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location
        })

    session.close()
    return result