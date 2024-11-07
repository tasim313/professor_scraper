import os
import environ
from .auth import BASE_DIR

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Get the root path for the project directory
ROOT_PATH = os.path.dirname(__file__)

# Static files configuration
STATIC_URL = env("DJANGO_STATIC_URL", default="static/")
STATICFILES_DIRS = [os.path.join(ROOT_PATH, "static")]
STATIC_ROOT = env("DJANGO_STATIC_ROOT", default=os.path.join(BASE_DIR, "staticfiles"))


# Media files configuration
MEDIA_URL = env("DJANGO_MEDIA_URL", default="/media/")
MEDIA_URL_2 = env("DJANGO_MEDIA_URL_2", default="/media/new/")
MEDIA_ROOT = env("DJANGO_MEDIA_ROOT", default=os.path.join(BASE_DIR, "media"))