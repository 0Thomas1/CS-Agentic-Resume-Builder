from pydantic import BaseModel, Field

class ResumeProject(BaseModel):
    title: str = Field(description="The title of the project")
    description: str = Field(description="A brief description of the project")
    url: str = Field(description="The URL to the project repository")
    date: str = Field(description="The date the project was last updated")
    category: str = Field(description="The category of the project")
    tech_stack: list[str] = Field(description="The technologies used in the project")
    core_problem_solved: str = Field(description="The core problem the project solves")
    key_features: list[str] = Field(description="The key features of the project")
    quantifiable_metrics: list[str] = Field(description="The quantifiable metrics of the project")