from celery_app import app
from daily_philosopher.crew import DailyPhilosopherCrew
import agentops

@app.task
def new_blog_post():
    """Run the BlogPostCrew."""
    agentops.init()

    inputs = {
    }
    crew_output = DailyPhilosopherCrew().crew().kickoff(inputs=inputs)