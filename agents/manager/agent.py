from manager.agents.analyst.agent import root_agent as job_analyst_agent
from manager.agents.repo_matcher.agent import root_agent as repo_matcher_agent
from manager.agents.resume_tailor.agent import root_agent as resume_tailor_agent
from google.adk.tools import agent_tool
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_response import LlmResponse
from google.adk.models.llm_request import LlmRequest
from typing import Optional
import dotenv
import os
dotenv.load_dotenv()

# initialize agents as sub-agents for the manager agent to call
job_analyst_agent_tool = agent_tool.AgentTool(job_analyst_agent)
repo_matcher_agent_tool = agent_tool.AgentTool(repo_matcher_agent)
resume_tailor_agent_tool = agent_tool.AgentTool(resume_tailor_agent)


def before_model_call(callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:
    """
    Callback function that runs before the model is called. Can be used to prepare or modify the context or request.
    Args:
        callback_context (CallbackContext): The context of the callback, which includes state and actions.
        llm_request (LlmRequest): The request that will be sent to the LLM
    Returns:
        Optional[LlmResponse]: You can return an LlmResponse to short-circuit the model call and return a response immediately, or return None to continue with the model call as normal.
        
    """
    print(f"  [Pre-Agent Call] Preparing context for {callback_context.agent_name}")
    # Here you can implement any necessary context preparation logic before calling sub-agents
    # For example, you could aggregate information from previous steps or ensure certain keys are present in the context
    callback_context.state['user_selected_projects'] = callback_context.state.get('user_selected_projects', [])
    return None

#- save resume_intake into context
def save_resume_to_context(resume: str, tool_context):
    """
    Saves the resume intake information into the shared context for downstream agents to access.
    Args:
        resume (str): The resume intake information in JSON string format.
        tool_context (ToolContext): The context of the tool call, which includes state and actions.

    Returns:
        dict: An empty dictionary as tools should return JSON-serializable output.
    """
    print(f"  [Tool Call] save_resume_to_context triggered by {tool_context.agent_name}")
    tool_context.state['resume_intake'] = resume
    # Return empty dict as tools should typically return JSON-serializable output
    return {}

from google.adk.models.lite_llm import LiteLlm




lm_stduio = LiteLlm(
    model='ollama_chat/gemma4:12b',
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key='fake_api_key_for_local_testing',
)

root_agent = LlmAgent(
    model=lm_stduio,
    name='Manager_Agent',
    description=(
        "The Manager Agent oversees the entire resume-building process, coordinating between sub-agents and ensuring a smooth workflow. "
        "The Manager Agent handle conversation with the user to collect necessary information for resume building."
        "The Manager Agent should handle any necessary context passing between agents and ensure that the final output is a tailored resume based on the user's input and the target job description."
        "You MUST call save_resume_to_context after receiving resume intake information from user to store it in the shared context for downstream agents to access."
        "Work flow: 1) Receive resume intake and job description from user, save to context. 2) Call job analyst agent to analyze the job description and extract key requirements. 3) Call repo matcher agent to find relevant projects from user's repositories that match the job requirements. 4) Call resume tailor agent to write a tailored project section for the resume using the job analysis and matched projects. 5) Return the tailored resume output to the user."
    ),
    before_model_callback=before_model_call,
    tools=[save_resume_to_context, job_analyst_agent_tool, repo_matcher_agent_tool, resume_tailor_agent_tool],
)