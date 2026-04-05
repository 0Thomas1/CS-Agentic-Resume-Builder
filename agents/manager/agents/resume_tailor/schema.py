from pydantic import BaseModel, Field
from typing import Optional


class ResumeProject(BaseModel):
    title: str = Field(description="The title of the project")
    techstack: list[str] = Field(description="The technologies used in the project")
    bullet_points: list[str] = Field(description="The bullet points describing the project, ideally with quantifiable metrics")
    def model_post_init(self, __context) -> None:
        if len(self.bullet_points) not in range(1, 4):
            raise ValueError("bullet_points must contain 1-3 items")
        
class ProjectList(BaseModel):
    projects: list[ResumeProject] = Field(description="A list of projects to be included in the resume")
    def model_post_init(self, __context) -> None:
        if len(self.projects) != 3:
            raise ValueError("projects must contain exactly 3 items")

class EducationSchema(BaseModel):
    degree: str = Field(description="The degree obtained, e.g. Bachelor of Science in Computer Science")
    institution: str = Field(description="The name of the educational institution")
    graduation_year: Optional[int] = Field(default=None, description="The year of graduation, if applicable")
    relavent_courses: Optional[list[str]] = Field(default=None, description="List of relevant courses taken, if applicable")
    note: Optional[str] = Field(default=None, description="Additional notes about the education entry, e.g. honors or GPA")
class ExperienceSchema(BaseModel):
    title: str = Field(description="The job title held at the company")
    company: str = Field(description="The name of the company")
    start_date: str = Field(description="The start date of the experience, e.g. Jan 2020")
    end_date: Optional[str] = Field(default=None, description="The end date of the experience, e.g. Dec 2022 or 'Present' if currently employed")
    description: str = Field(description="A brief description of the role and responsibilities")

class ResumeSchema(BaseModel):
    project_list: ProjectList = Field(description="The list of projects to include in the resume, with details for each project")
    name: str = Field(description="Candidate full name")
    email: str = Field(description="Primary email")
    phone: str = Field(description="Phone number")
    location:Optional[str] = Field(default=None, description="City, State, or Country")
    educations: list[EducationSchema] = Field(description="The candidate's educational background")
    experiences: list[ExperienceSchema] = Field(description="The candidate's work experience")
