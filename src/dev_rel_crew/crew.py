import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

openai_llm = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
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
            tools=[SerperDevTool()],
            verbose=True,
            llm=openai_llm,
        )

    @agent
    def blog_chapter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_chapter_writer"],
            verbose=True,
            llm=openai_llm,
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
            verbose=True,
            llm=openai_llm,
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def tweet_writer(self) -> Agent:
        return Agent(config=self.agents_config["tweet_writer"], verbose=True)

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
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
