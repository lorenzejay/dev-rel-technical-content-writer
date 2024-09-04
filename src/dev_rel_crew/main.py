#!/usr/bin/env python
import sys
from dev_rel_crew.crew import DevRelCrewCrew


def run():
    inputs = {
        "topic": "Using crewai to automate content creation for a tech saas focused on researching competitors and content idea listing.",
        "tech_stack": "crewai.com, python, groq",
        "output_blog_path": "output/crew_ai_doc.md",
        "output_tweet_path": "output/crew_ai_tweet.md",
        "deployment_blog_file_name": "/Users/lorenzejay/workspace/experimental/ai_tools/dev_rel_crew/output/crew_ai_doc.md",
        "github_repo_name": "https://github.com/crewAIInc/crewAI",
    }

    result = DevRelCrewCrew().crew().kickoff(inputs=inputs)

    print(result)


# to run multiple inputs
# async def run():
#     inputs = [
#         {
#             "topic": "Using crewai agents to automate researching competitors and optimizing a tech company's content creation",
#             "tech_stack": "crewai, crewai-tools",
#             "output_blog_path": "output/blog_1.md",
#             "output_tweet_path": "output/tweet_1.md",
#             "deployment_blog_file_name": "output/blog_1.md",
#             "github_repo_name": "https://github.com/crewAIInc/crewAI",
#         },
#         {
#             "topic": "Using crewai to automate content creation for a tech company.",
#             "tech_stack": "crewai.com",
#             "output_blog_path": "output/blog_2.md",
#             "output_tweet_path": "output/tweet_2.md",
#             "deployment_blog_file_name": "output/blog_2.md",
#             "github_repo_name": "https://github.com/crewAIInc/crewAI",
#         },
#     ]

#     result = await DevRelCrewCrew().crew().kickoff_for_each_async(inputs=inputs)

#     print(result)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Simple RAG app with Haystack",
        "tech_stack": "Python, Haystack, Langchain",
    }
    try:
        DevRelCrewCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

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


# def main():
#     asyncio.run(run())


# if __name__ == "__main__":
#     main()
