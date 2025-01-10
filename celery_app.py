import os
import sys
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Add the `src` directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
app = Celery('celery_app', broker=CELERY_BROKER_URL)
app.conf.update(
    result_backend='redis://localhost:6379/0',
    task_default_queue='daily_philosopher',
    beat_schedule={
        'run-daily_blog_post': {
            'task': 'tasks.new_blog_post',
            #'schedule': crontab(hour=1, minute=0),
            'schedule': crontab(minute='*/1'),
            'args': ()
        }
    },
    include=['tasks']
)