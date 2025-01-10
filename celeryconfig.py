from celery.schedules import crontab

# Celery Beat schedule configuration
CELERY_BEAT_SCHEDULE = {
    # Example task to run every minute
    'daily-task-schedule': {
        'task': 'celery_app.daily_blog_post',  # Task name (must match exactly with the Celery task)
        'schedule': crontab(minute='*/1'),    # Runs every minute for testing
        # 'args': ('optional_arg1', 'optional_arg2'),  # Uncomment to pass arguments
    },
}

# Timezone configuration
CELERY_TIMEZONE = 'UTC'

# Result backend (optional, for storing task results)
# Uncomment and configure if you need to store task results
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Broker URL (Redis in this case)
CELERY_BROKER_URL = 'redis://localhost:6379/0'

# Optional: Serializer settings (if needed)
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'