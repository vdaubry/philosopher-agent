from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import Systeme.io

@CrewBase
class AutomatingContentCreationForEnhancedEfficiencyCrew():
    """AutomatingContentCreationForEnhancedEfficiency crew"""

    @agent
    def news_monitoring_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['news_monitoring_specialist'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def topic_suggestion_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['topic_suggestion_expert'],
            tools=[],
        )

    @agent
    def blog_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['blog_content_creator'],
            tools=[],
        )

    @agent
    def website_publishing_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['website_publishing_specialist'],
            tools=[Systeme.io()],
        )


    @task
    def monitor_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['monitor_news_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def suggest_topic_task(self) -> Task:
        return Task(
            config=self.tasks_config['suggest_topic_task'],
            tools=[],
        )

    @task
    def generate_blog_post_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_blog_post_task'],
            tools=[],
        )

    @task
    def publish_blog_post_task(self) -> Task:
        return Task(
            config=self.tasks_config['publish_blog_post_task'],
            tools=[Systeme.io()],
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
