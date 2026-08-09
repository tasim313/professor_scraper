# Professor Scraper — Global Academic Intelligence Platform

## 1. Project Vision

Professor Scraper is a global academic intelligence platform that collects, verifies, structures, indexes, and presents publicly available information about professors, researchers, universities, departments, laboratories, publications, research interests, and academic careers.

The platform should provide useful information freely to the public while generating revenue through:

* Advertising
* Newsletter sponsorship
* Premium memberships
* Premium research reports
* Institutional research access
* Carefully selected sponsorships
* Donations/grants where appropriate

It should not depend on:

* Selling software
* Selling SaaS licenses
* Selling AI agents
* Selling physical products
* Publishing fake academic information
* Creating fabricated professor profiles
* Automatically copying entire websites

The core principle is:

> Collect public information, verify it, structure it, explain it, and make it useful.

---

# 2. Primary Objectives

The platform should accomplish six major objectives.

### Objective 1 — Discover professors

Users should be able to search for professors globally.

Example:

```text
Professor:
Dr. Jane Smith

University:
University of Toronto

Department:
Computer Science

Research:
Artificial Intelligence
Machine Learning
Medical Imaging
```

### Objective 2 — Discover research

Users should be able to discover:

* Research topics
* Publications
* Research groups
* Laboratories
* Research interests
* Academic departments
* Collaborators

### Objective 3 — University intelligence

Users should be able to investigate universities.

Example:

```text
University
    ↓
Departments
    ↓
Professors
    ↓
Research areas
    ↓
Publications
    ↓
Research laboratories
```

### Objective 4 — Academic career discovery

Students should be able to find professors relevant to:

* Master's programs
* PhD programs
* Research collaboration
* Academic supervision
* Research internships

### Objective 5 — Research intelligence

Researchers should be able to identify:

* Researchers working on a specific topic
* Universities specializing in a field
* Research clusters
* Publication trends
* Geographic research distribution

### Objective 6 — Build a trusted academic knowledge database

Long-term, the platform becomes a structured global academic directory.

---

# 3. Target Users

## 3.1 Students
Students looking for professors, supervisors, universities, research topics, Master's/PhD opportunities.

## 3.2 Researchers
Researchers looking for collaborators, research groups, experts, publications, institutions.

## 3.3 Universities
Universities can use the platform to understand academic visibility, research areas, faculty profiles, research networks.

## 3.4 Journalists
Journalists can discover experts for interviews, research, academic commentary.

## 3.5 General public
People can search who researches what and where.

---

# 4. Business Model

```text
FREE INFORMATION -> SEO TRAFFIC -> RETURNING USERS -> NEWSLETTER -> TRUST -> PREMIUM MEMBERSHIP
```

## Free users
Free users can access professor profiles, university profiles, basic search, research interests, basic publications, basic statistics, articles, academic guides.

---

# 5. Advertising
Advertising should be secondary to user experience. Distinguish editorial content from sponsored content clearly.

---

# 6. Newsletter
Newsletters (e.g., Weekly Academic Intelligence, AI Research Weekly) are a strong asset.

---

# 7. Premium Membership
Premium features: Advanced filtering, saved searches, research analytics, historical changes, bulk discovery, advanced comparison, research trend reports, export.

---

# 8. Premium Research Reports
Instead of selling software, sell information products (e.g., Top 500 AI Researchers Worldwide, Global Cancer Research Landscape).

---

# 9. Ethical Scraping Policy
Respect robots.txt, website terms, reasonable request rates, avoid bypassing authentication, avoid CAPTCHA circumvention, avoid collecting private/sensitive personal information, respect takedown requests, maintain source URLs and attribution, store timestamps. Focus on public professional academic information.

---

# 10. Data Sources
University websites, Public academic profiles (ORCID, Google Scholar, etc.), Research databases (Crossref, OpenAlex, PubMed). Sources must be pluggable.

---

# 11. Source Adapter Architecture
Never create one giant scraper. Use a common interface (`BaseScraper`) with methods like `discover`, `fetch`, `parse`, `normalize`, `validate`.

---

# 12. Django Architecture
`NGINX -> Gunicorn -> Django -> Django REST API -> (PostgreSQL, Redis, Storage) -> Academic Data`

---

# 13. Recommended Backend Stack
Python 3.12+, Django, Django REST Framework, PostgreSQL, Redis, Celery, BeautifulSoup, Requests, httpx, django-environ, Gunicorn, Nginx, Docker. Optional: OpenSearch / Elasticsearch later.

---

# 14. PostgreSQL
Primary database for production, large datasets, concurrent users, analytics, and search. SQLite only for dev/testing.

---

# 15. Core Database Design
University, Department, Professor, ProfessorAffiliation, ResearchArea, ResearchInterest, Publication, Author, ProfessorPublication, ResearchGroup, Laboratory, AcademicDegree, ProfessorDegree, ProfessorEmployment, Source, SourceSnapshot, ScrapeJob, ScrapeResult, DataChange, User, Subscription, NewsletterSubscription, SavedSearch, SearchHistory, Report.

---

# 16. University Model
id, name, official_name, slug, country, state, city, website, domain, description, founded_year, type, logo, latitude, longitude, status, created_at, updated_at.

---

# 17. Department Model
id, university_id, name, slug, website, description, faculty_url, research_url, created_at, updated_at.

---

# 18. Professor Model
id, first_name, middle_name, last_name, full_name, slug, title, gender, profile_url, official_email, office, phone, bio, status, first_seen_at, last_seen_at, created_at, updated_at. Avoid unnecessary personal information.

---

# 19. Professor Affiliation
Professor -> Affiliation -> University, Department, Position, Start Date, End Date.

---

# 20. Academic Degrees
Professor -> Degree -> PhD, MSc, BSc (degree_type, field, institution, country, year, source).

---

# 21. Research Areas
Controlled vocabulary (e.g., Computer Science -> Artificial Intelligence -> Machine Learning).

---

# 22. Research Interest
Connect to a normalized research topic.

---

# 23. Publication Model
title, abstract, doi, url, publication_date, journal, publisher, type, citation_count, source, created_at, updated_at. Authors linked.

---

# 24. Author Identity Resolution
Use Name, Institution, Department, Research topic, Publication co-authors, ORCID, Email domain, Profile URL. Never rely solely on name.

---

# 25. Source System
Every important data point should have provenance (Source, Source URL, Collected Date).

---

# 26. Data Provenance
Store source, source_url, retrieved_at, parser_version, confidence, content_hash.

---

# 27. Source Snapshots
Store source_id, url, retrieved_at, http_status, content_hash, raw_content_reference, parser_version.

---

# 28. Change Detection
Detect and record changes (DataChange) when a professor's affiliation changes.

---

# 29. Scraping Pipeline
SOURCE DISCOVERY -> URL QUEUE -> FETCH -> RAW RESPONSE -> PARSER -> NORMALIZATION -> VALIDATION -> DEDUPLICATION -> ENTITY RESOLUTION -> DATABASE -> SEARCH INDEX -> PUBLIC API.

---

# 30. Celery
Use Celery + Redis for scraping tasks outside HTTP requests.

---

# 31. Task Queues
Separate queues: discovery, scraping, parsing, normalization, publication, search_index, analytics, email.

---

# 32. Request Rate Limiting
Per-domain rate limiting.

---

# 33. Retry System
Controlled retries with exponential backoff for HTTP failures.

---

# 34. HTTP Status Handling
200 (parse), 301/302 (follow safely), 403 (stop/investigate), 404 (mark unavailable), 429 (slow down), 500/503 (retry).

---

# 35. BeautifulSoup
Use for HTML parsing. HTML -> Parser -> Dictionary/DTO -> Validator -> ORM.

---

# 36. Data Normalization
Normalize names, preserve raw strings.

---

# 37. Data Validation
Reject empty names, invalid URLs, malformed profiles, duplicates.

---

# 38. Confidence Score
Assign a confidence score to profiles based on verification hierarchy.

---

# 39. Verification
Hierarchy: Official university page -> Institutional repository -> ORCID -> Research database -> Secondary source.

---

# 40-163. Platform Features & Marketing
Professor profile pages, advanced search, SEO strategy, editorial content, research articles, data journalism, newsletters, subscriptions, APIs (DRF), Django settings (django-environ), security, admin panels, moderation, analytics, user dashboards.

---

# 164. MVP

Do not build everything initially.

**Tech:**
Django, DRF, PostgreSQL, Redis, Celery, BeautifulSoup.

**Data:**
5–10 universities, 10,000–50,000 professors.

**Features:**
Professor search, University search, Professor profile, University profile, Research areas, Source tracking, Admin, Scraper dashboard, Newsletter, Basic SEO.

---

# 165-168. Future Phases
Add more universities, publications, research taxonomy, advanced search, knowledge graph, institutional access, internationalization.

---

# 169. Core Django Apps
`apps/academics`, `apps/universities`, `apps/professors`, `apps/research`, `apps/publications`, `apps/sources`, `apps/scraping`, `apps/search`, `apps/accounts`, `apps/subscriptions`, `apps/newsletter`, `apps/editorial`, `apps/analytics`, `apps/notifications`.

---

# 170. Service Layer
API -> Service -> Domain logic -> Repository / ORM. Don't put everything into Django views.

---

# 171-400. Deep Implementation Details
Scraping Service, Dependency Injection, Configuration per source, Scrape Jobs, Data Migrations, Background Scheduler, Database Transactions, Canonical Identity, API Optimization, Infrastructure Scaling.

---

# 401-500. Critical Production Requirements
Source reliability, parser isolation, queue isolation, transaction safety, duplicate protection, data provenance, ethical crawling, security, monitoring, database indexing.

**Final Vision:**
"A trustworthy global academic intelligence and knowledge platform, powered by automated data collection, human verification, structured research data, editorial content, and a sustainable audience-based business model."
