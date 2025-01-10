from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
from automating_content_creation_for_enhanced_efficiency.tools.blog_tool import BlogTool

class BlogPostOutput(BaseModel):
    """Pydantic model for the output of the report_compilation_task."""
    blog_post_content: str

@CrewBase
class AutomatingContentCreationForEnhancedEfficiencyCrew():
    """AutomatingContentCreationForEnhancedEfficiency crew"""

    @agent
    def dark_humor_philosopher(self) -> Agent:
        return Agent(
            config=self.agents_config['dark_humor_philosopher'],
            tools=[],
        )
    @agent
    def website_publishing_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['website_publishing_specialist'],
            tools=[],
        )


    @task
    def dark_humor_philosophy_task(self) -> Task:
        return Task(
            config=self.tasks_config['dark_humor_philosophy_task'],
            tools=[],
            output_pydantic=BlogPostOutput
        )

    @task
    def publish_blog_post_task(self) -> Task:
        return Task(
            config=self.tasks_config['publish_blog_post_task'],
            tools=[BlogTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutomatingContentCreationForEnhancedEfficiency crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
