from celery_app import app
from automating_content_creation_for_enhanced_efficiency.crew import AutomatingContentCreationForEnhancedEfficiencyCrew
import agentops

@app.task
def daily_blog_post():
    """Run the BlogPostCrew."""
    agentops.init()

    inputs = {
    }
    crew_output = AutomatingContentCreationForEnhancedEfficiencyCrew().crew().kickoff(inputs=inputs)