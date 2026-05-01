import requests

def scrape_jobs():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)
    data = response.json()

    jobs = []

    for job in data["jobs"]:
        jobs.append({
            "title": job["title"],
            "company": job["company_name"],
            "location": job["candidate_required_location"]
        })

    return jobs

from database.db import SessionLocal
from database.models import Job

def save_jobs(jobs):
    session = SessionLocal()

    for job in jobs:
        new_job = Job(
            title=job["title"],
            company=job["company"],
            location=job["location"]
        )
        session.add(new_job)

    session.commit()
    session.close()