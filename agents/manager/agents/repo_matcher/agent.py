import os
import dotenv
from google.adk.agents.llm_agent import Agent
from .githubClient import GitApiClient
from .schema import ResumeProject
from google.adk.planners import BuiltInPlanner
from google.genai import types


dotenv.load_dotenv()
git_client = None


def _get_git_client():
    global git_client
    if git_client is None:
        git_client = GitApiClient(
            os.getenv("GITHUB_USERNAME"),
            os.getenv("GITHUB_TOKEN"),
        )
    return git_client


# match github repositories to job requirements
def get_repositories():
    """
    Tool function to fetch and return the user's GitHub repositories. This function is used by the Repo_Matcher agent to access repository data for matching against job requirements.
    """
    return _get_git_client().get_repositories()



# Initialize the agent
root_agent = Agent(
    name='Repo_Matcher',
    description="Matches GitHub repositories to job requirements based on structured analyst output.",
    instruction=(
        "You are an expert software engineer and recruiter. "
        "Read the structured job requirements from {job_analysis}. "
        "Use the get_repositories tool to inspect the user's repositories. "
        "Select the top 3 projects that best match the role requirements, skills, and seniority. "
        "Prefer evidence-backed matches from languages and README summaries, and return concise rationale per project."
    ),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=1024,
        )
    ),
    tools=[get_repositories],
    output_schema=list[ResumeProject],
    output_key="matched_repositories"
)