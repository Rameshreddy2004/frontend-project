from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev'

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'prompts',
]

ROOT_URLCONF = 'backend.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prompts_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
import time
import psycopg2

for i in range(10):
    try:
        conn = psycopg2.connect(
            dbname='prompts_db',
            user='postgres',
            password='postgres',
            host='db',
            port='5432'
        )
        conn.close()
        print("DB connected successfully")
        break
    except psycopg2.OperationalError:
        print("Waiting for DB...")
        time.sleep(2)