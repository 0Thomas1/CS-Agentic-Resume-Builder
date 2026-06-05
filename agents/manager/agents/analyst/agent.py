from typing import List, Optional
from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field

# 1. Define the Schema for the Data we want to extract
class JobAnalysis(BaseModel):
    title: str = Field(description="The job title")
    company: str = Field(description="The company hiring for the position")
    work_model: str = Field(description="Remote, Hybrid, or On-site")
    location: str = Field(description="City, State, or Country (if applicable)")
    years_of_experience: float = Field(description="Minimum years of experience required. Use 0 if entry level.")
    core_skills: List[str] = Field(description="List of primary programming languages, tools,tech stack and frameworks required")
    salary_range: Optional[str] = Field(description="The stated salary range, if any")
    visa_sponsorship: str = Field(description="Yes, No, or Unknown regarding H1B or similar visa sponsorship")
    summary: str = Field(description="A 3-4 sentence summary of the primary responsibilities")

# 3. Define the Analyst Agent
root_agent = LlmAgent(
    name='Job_Analyst',

    description="Analyzes raw, unstructured job descriptions and extracts structured metrics like skills, salary, and requirements.",
    instruction=(
        "You are an expert technical recruiter and job analyst. "
        "The user will provide you with a raw job description text. "
        "Your task is to carefully read the job description, extract the critical requirements, "
        "compensation, skills, and logistics, and then summarize the key responsibilities in a concise manner."
    ),
    
    output_schema=JobAnalysis,
    output_key="job_analysis",
)