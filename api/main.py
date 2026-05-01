from fastapi import FastAPI, Query
from database.db import SessionLocal
from database.models import Job

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job API is running"}


@app.get("/jobs")
def get_jobs(
    location: str = Query(None),
    company: str = Query(None),
    page: int = Query(1),
    page_size: int = Query(5)
):
    session = SessionLocal()

    query = session.query(Job)

    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    if company:
        query = query.filter(Job.company.ilike(f"%{company}%"))

    offset = (page - 1) * page_size
    jobs = query.offset(offset).limit(page_size).all()

    session.close()

    result = []
    for job in jobs:
        result.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location
        })

    return result