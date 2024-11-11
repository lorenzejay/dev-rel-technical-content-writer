#!/usr/bin/env python
import sys
from dev_rel_crew.crew import DevRelCrewCrew


def run():
    inputs = {
        "topic": "Using CrewAI agents with Composio tools to create a SQL agent that can query a database",
        "tech_stack": "crewai.com, python, composio.dev",
        "github_repo_name": "https://github.com/crewAIInc/crewAI",
    }

    result = DevRelCrewCrew().crew().kickoff(inputs=inputs)
    print("result", result)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Using CrewAI agents with Composio tools to create a SQL agent that can query a database",
        "tech_stack": "crewai.com, python, composio.dev",
        "github_repo_name": "https://github.com/crewAIInc/crewAI",
    }
    try:
        DevRelCrewCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            inputs=inputs,
            filename="trained_agents_data.pkl",
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay_from_task():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DevRelCrewCrew().crew().replay_from_task(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Using CrewAI agents with Composio tools to create a SQL agent that can query a database",
        "tech_stack": "crewai.com, python, composio.dev",
        "github_repo_name": "https://github.com/crewAIInc/crewAI",
    }
    DevRelCrewCrew().crew().test(
        n_iterations=2, inputs=inputs, openai_model_name="gpt-4o"
    )


# def main():
#     asyncio.run(run())


# if __name__ == "__main__":
#     main()
