import os
import environ
import psycopg2  # Ensure psycopg2 is installed if using PostgreSQL
from .auth import BASE_DIR

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Attempt to connect to PostgreSQL
try:
    # Attempt a test connection to PostgreSQL
    conn = psycopg2.connect(
        dbname=env("DJANGO_DB_NAME"),
        user=env("DJANGO_DB_USER"),
        password=env("DJANGO_DB_PASSWORD"),
        host=env("DJANGO_DB_HOST"),
        port=env("DJANGO_DB_PORT", default=5432),
    )
    conn.close()

    # If successful, configure PostgreSQL as the default database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DJANGO_DB_NAME"),
            "USER": env("DJANGO_DB_USER"),
            "PASSWORD": env("DJANGO_DB_PASSWORD"),
            "HOST": env("DJANGO_DB_HOST"),
            "PORT": env("DJANGO_DB_PORT", default=5432),
        }
    }
except (psycopg2.OperationalError, psycopg2.InterfaceError):
    # Fallback to SQLite if PostgreSQL is not available
    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
