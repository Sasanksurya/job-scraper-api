#  Job Scraper API

A FastAPI-based backend project that scrapes job data and stores it in a MySQL database. It provides REST APIs to fetch jobs with filtering and pagination.

---

##  Tech Stack

* Python
* FastAPI
* SQLAlchemy
* MySQL
* BeautifulSoup / Requests

---

##  Features

* Scrape job listings
* Store jobs in database
* REST API endpoints
* Filter by location & company
* Pagination support

---

##  API Endpoints

### Get all jobs

```
GET /jobs
```

### With filters

```
GET /jobs?location=USA&company=Google
```

### With pagination

```
GET /jobs?page=1&page_size=5
```

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

---

##  Output

Visit:

```
http://127.0.0.1:8000/jobs
```

---

##  Author

Shashank Surya
