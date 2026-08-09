# Global Academic Intelligence Platform
*(Formerly Professor Scraper)*

## Project Vision
The Global Academic Intelligence Platform is a worldwide academic discovery and structured data platform. 
We aggregate, verify, and structure data from thousands of official university domains to provide a reliable knowledge graph covering:
- **Universities & Colleges**
- **Degree Programs & Subjects**
- **Scholarships & Fellowships**
- **Researchers & Professors**
- **Tuition & Living Costs**

## System Architecture
This project utilizes a highly decoupled, scalable architecture:

1. **Backend API (Django + DRF)**
   - Strict Domain-Driven Design (20+ isolated apps)
   - PostgreSQL Relational Database Schema (30+ normalized tables)
   - Read-Only JSON API exposed via Django Rest Framework at `/api/v1/`

2. **Scraping Engine (Celery + BeautifulSoup + Playwright + Selenium)**
   - Custom `BaseScraper` Adapter Pattern
   - Asynchronous execution via Celery & Redis
   - Intelligent DOM parsing mapped directly to the ORM

3. **Frontend (Next.js 15 + Tailwind CSS v4 + Three.js)**
   - High-fidelity premium user interface
   - Next.js App Router for SEO-optimized programmatic landing pages
   - Located in the `/frontend/` directory

4. **Internal CMS (Django Admin + RangeFilter + ImportExport)**
   - Enterprise-grade CRM for data moderation
   - Bulk CSV import/export capabilities
   - Advanced temporal and relational filtering

## Installation and Setup

### Prerequisites
- Python 3.10+
- Node.js 18.17+
- PostgreSQL
- Redis (for Celery)

### 1. Backend Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirement/development.text
```
Configure your `.env` file with your database credentials.
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2. Scraping Engine Setup
Start the Redis server, then run the Celery worker:
```bash
celery -A professor_scraper worker -l info
```
To run a sample scraper directly:
```bash
python manage.py run_wikipedia_scraper
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## Contributing
Please see `CONTRIBUTING.md` for our branch strategy and coding standards.

## Security
See `SECURITY.md` for information on our data provenance, GDPR compliance, and vulnerability reporting.
