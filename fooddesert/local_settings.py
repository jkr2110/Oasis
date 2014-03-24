from settings import PROJECT_ROOT, SITE_ROOT
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
"default": {
  "ENGINE": "django.db.backends.postgresql_psycopg2",
  "NAME": "oasis",
  "USER": "warren",
  "PASSWORD": "",
  "HOST": "localhost",
  "PORT": "5432",
		}
}
