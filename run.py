from scraper.scraper import scrape_jobs, save_jobs

jobs = scrape_jobs()
save_jobs(jobs)

print("Data saved to MySQL!")