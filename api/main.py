from fastapi import FastAPI
from database.db import SessionLocal
from database.models import Job
app = FastAPI()
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

    session.close()   # ✅ VERY IMPORTANT

    return result