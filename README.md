# Project Title: Professor Scraper

## Project Goal
The **Professor Scraper** project aims to provide an efficient web scraping tool that collects data about professors from various online sources. This data can be used for analysis, academic purposes, or to enhance educational resources. The project is built using Django and Django Rest Framework (DRF), ensuring a robust backend for managing the scraped data.

## Features
- **Web Scraping**: Uses Beautiful Soup and Requests libraries to scrape information from designated websites.
- **API Development**: Provides a RESTful API using Django Rest Framework for easy access to scraped data.
- **Data Storage**: Supports PostgreSQL (recommended) or SQLite for database management, allowing for easy data persistence and retrieval.
- **CORS Handling**: Includes configuration for Cross-Origin Resource Sharing (CORS) to enable frontend applications to communicate with the backend.
- **Environment Management**: Utilizes django-environ for managing environment variables, making it easy to configure settings based on different environments (development, production).
- **Code Quality Tools**: Integrated linting and formatting tools (Flake8 and Black) to maintain code quality and consistency.

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- PostgreSQL (or SQLite)

### Step 1: Clone the Repository
```bash
git clone https://github.com/tasim313/professor_scraper.git
cd professor_scraper
```

Step 2: Create a Virtual Environment
It’s a good practice to use a virtual environment to manage  project's dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Step 3: Install Requirements
Use pip to install the required packages.
```bash
pip install -r requirement/development.text
```

Step 4: Configure the Database
- If using PostgreSQL, create a database and update  settings.py file with the database credentials.
- For SQLite, ensure the database file path is correctly set in settings.py.

Step 5: Run Migrations
To set up the database schema, run the migrations.
- python manage.py migrate

Step 6: Create a Superuser (Optional)
If  need to access the Django admin interface, create a superuser.
```bash
python manage.py createsuperuser
```
Step 7: Start the Development Server
```bash
python manage.py runserver
```
access the application at http://127.0.0.1:8000/.

Usage

Once the server is running,  use the API endpoints to interact with the scraped data. Refer to the documentation provided within the project for details on available endpoints and their usage.
