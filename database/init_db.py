from database.db import engine, SessionLocal
from database.models import Base, Job

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    if db.query(Job).count() == 0:
        db.add_all([
            Job(title="Python Developer", company="ABC Company", location="India"),
            Job(title="Data Analyst", company="XYZ Company", location="USA"),
            Job(title="Backend Engineer", company="Google", location="USA")
        ])
        db.commit()

    db.close()