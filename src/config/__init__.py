from .llm import AGENT_LLM_MAP, LLMType, get_llm
from .env import (TAVILY_API_KEY, TAVILY_MAX_RESULTS)

RESPONSE_FORMAT = "Response from {}:\n\n<response>\n{}\n</response>\n\n*Please execute the next step.*"

TEAM_MEMBERS = ["researcher","reporter", "coder"]
