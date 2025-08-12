import logging
from langchain_community.tools.tavily_search import TavilySearchResults
from src.config import TAVILY_MAX_RESULTS
from src.log import create_logged_tool

logger = logging.getLogger(__name__)


LoggedTavilySearch = create_logged_tool(TavilySearchResults)
tavily_tool = LoggedTavilySearch(name="tavily_search", max_results=TAVILY_MAX_RESULTS)