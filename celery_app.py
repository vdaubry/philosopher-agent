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

# Define SSL settings for secure Redis connections
BROKER_TRANSPORT_OPTIONS = {
    "ssl_cert_reqs": "CERT_NONE"  # Change to "CERT_REQUIRED" for stricter validation
}

app = Celery('celery_app', broker=CELERY_BROKER_URL)
app.conf.update(
    result_backend=CELERY_BROKER_URL,
    task_default_queue='daily_philosopher',
    beat_schedule={
        'run-daily_blog_post': {
            'task': 'tasks.new_blog_post',
            #'schedule': crontab(hour=1, minute=0),
            'schedule': crontab(minute='*/1'),
            'args': ()
        }
    },
    broker_transport_options=BROKER_TRANSPORT_OPTIONS,
    result_backend_transport_options=BROKER_TRANSPORT_OPTIONS,  # Ensure backend uses SSL options
    include=['tasks']
)