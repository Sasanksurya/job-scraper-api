from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:surya@localhost/job_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

# Test connection
try:
    conn = engine.connect()
    print("✅ Connected to MySQL successfully!")
    conn.close()
except Exception as e:
    print("❌ Error:", e)