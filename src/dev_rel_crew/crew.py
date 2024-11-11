import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, GithubSearchTool, EXASearchTool
from dotenv import load_dotenv
# from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

github_dev_tool = GithubSearchTool(
    gh_token=os.getenv("GITHUB_API_KEY"),
    content_types=["code", "repo"],
)


@CrewBase
class DevRelCrewCrew:
    """DevRelCrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[EXASearchTool(), github_dev_tool],
            verbose=True,
            llm="openai/gpt-4o-mini",
        )

    @agent
    def blog_chapter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_chapter_writer"],
            verbose=True,
            llm="openai/gpt-4o-mini",
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            verbose=True,
            tools=[ScrapeWebsiteTool()],
            llm="openai/gpt-4o-mini",
        )

    @agent
    def tweet_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["tweet_writer"],
            verbose=True,
            llm="openai/gpt-4o-mini",
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.researcher())

    @task
    def chapter_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config["chapter_writer_task"],
            agent=self.blog_chapter_writer(),
        )

    @task
    def blog_post_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_post_task"],
            agent=self.blog_writer(),
        )

    @task
    def tweet_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config["tweet_writer_task"],
            agent=self.tweet_writer(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DevRelCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
