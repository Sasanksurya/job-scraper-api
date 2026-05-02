from fastapi import FastAPI, Query
from database.db import SessionLocal
from database.models import Job
from database.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()


@app.get("/jobs")
def get_jobs(
    page: int = 1,
    page_size: int = 5,
    location: str = None,
    title: str = None
):
    session = SessionLocal()

    query = session.query(Job)

    # 🔥 filtering
    if location:
        query = query.filter(Job.location == location)

    if title:
        query = query.filter(Job.title.contains(title))

    offset = (page - 1) * page_size

    jobs = query.offset(offset).limit(page_size).all()

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