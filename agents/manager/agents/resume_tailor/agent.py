from google.adk.agents.llm_agent import Agent
from .schema import ResumeSchema
from google.adk.planners import BuiltInPlanner
from google.genai import types

root_agent = Agent(
    model='gemini-3.1-flash-lite-preview',
    name='Resume_Tailor',
    description="The Root Agent responsible for writing a resume given a list of projects.",
    instruction=(
        "You are an expert resume writer. "
        "Use {job_analysis} and {matched_repositories} to produce a tailored project section for the target role. "
        "Also use {resume_intake} for user profile details and preferences. "
        "If {resume_intake} contains sample_resume_text, mirror that style while keeping content factual. "
        "If provided, also use {user_selected_projects} as human-curated project input. "
        "Treat user_selected_projects as high-priority guidance when choosing the final 3 projects, "
        "including a user-selected project when it is relevant even if repository matching ranked it lower. "
        "Prioritize role-relevant skills, quantified impact, and concise recruiter-friendly bullets. "
        "Do not invent experience that is not supported by the repository/project details."
        "return to parent Agent if you determine that there is insufficient information to produce a tailored resume, and clearly specify what information is missing."
    ),
    planner = BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=1024,
        )
    ),
    output_schema=ResumeSchema,
    output_key="produced_resume",
)
