from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Celery('celery_app', broker='redis://localhost:6379/0')
app.conf.update(
    result_backend='redis://localhost:6379/0',
    task_default_queue='daily_philosopher',
    beat_schedule={
        'run-daily_blog_post': {
            'task': 'tasks.new_blog_post',
            'schedule': crontab(minute='*/1'),
            'args': ()
        }
    },
    include=['tasks']
)