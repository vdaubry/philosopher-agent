import os
import sys
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Add the `src` directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Use the REDIS_URL environment variable, default to localhost for local development
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Define SSL options for Redis
REDIS_SSL_OPTIONS = {
    "ssl_cert_reqs": "CERT_NONE"  # Use "CERT_REQUIRED" for stricter SSL validation
}

# Initialize Celery app
app = Celery('celery_app', broker=CELERY_BROKER_URL)
app.conf.update(
    result_backend=CELERY_BROKER_URL,  # Use the same URL for result backend
    broker_transport_options=REDIS_SSL_OPTIONS,  # Apply SSL options to the broker
    result_backend_transport_options=REDIS_SSL_OPTIONS,  # Apply SSL options to the result backend
    task_default_queue='daily_philosopher',
    beat_schedule={
        'run-daily_blog_post': {
            'task': 'tasks.new_blog_post',
            #'schedule': crontab(hour=1, minute=0),
            'schedule': crontab(minute='*/1'),  # For testing
            'args': ()
        }
    },
    include=['tasks']
)