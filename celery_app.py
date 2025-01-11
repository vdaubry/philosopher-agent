import os
import sys
import ssl
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Add the `src` directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Use the REDIS_URL environment variable, default to localhost for local development
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Initialize Celery with SSL settings for secure Redis connections
app = Celery(
    'celery_app',
    broker=CELERY_BROKER_URL,
    broker_use_ssl={
        'ssl_cert_reqs': ssl.CERT_NONE  # Bypass SSL certificate validation for the broker
    },
    redis_backend_use_ssl={
        'ssl_cert_reqs': ssl.CERT_NONE  # Bypass SSL certificate validation for the result backend
    }
)

# Update Celery configuration
app.conf.update(
    result_backend=CELERY_BROKER_URL,
    task_default_queue='daily_philosopher',
    beat_schedule={
        'run-daily_blog_post': {
            'task': 'tasks.new_blog_post',
            #'schedule': crontab(minute='*/1'),  # Runs every minute for testing
            'schedule': crontab(hour=1, minute=0),  # Run daily at 1:00 AM
            'args': ()
        }
    },
    include=['tasks']
)