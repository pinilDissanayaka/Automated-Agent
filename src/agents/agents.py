from langgraph.prebuilt import create_react_agent

from src.prompts import apply_prompt_template
from src.tools import (
    bash_tool,
    python_repl_tool,
    tavily_tool,
)
from src.config import AGENT_LLM_MAP, get_llm


research_agent = create_react_agent(
    get_llm(AGENT_LLM_MAP["researcher"]),
    tools=[tavily_tool],
    prompt=lambda state: apply_prompt_template("researcher", state),
)

coder_agent = create_react_agent(
    get_llm(AGENT_LLM_MAP["coder"]),
    tools=[python_repl_tool, bash_tool],
    prompt=lambda state: apply_prompt_template("coder", state),
)

