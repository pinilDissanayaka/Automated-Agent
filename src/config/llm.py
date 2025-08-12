from typing import Literal
from langchain_openai import ChatOpenAI
from src.config.env import (
    BASIC_MODEL_NAME,
    BASIC_MODEL_PROVIDER,
    BASIC_MODEL_API_KEY,
    REASONING_MODEL_NAME,
    REASONING_MODEL_PROVIDER,
    REASONING_MODEL_API_KEY,
    VL_MODEL_NAME,
    VL_MODEL_PROVIDER,
    VL_MODEL_API_KEY
)
from langchain.chat_models import init_chat_model




LLMType = Literal["basic", "reasoning", "vision"]


AGENT_LLM_MAP: dict[str, LLMType] = {
    "coordinator": "basic", 
    "planner": "reasoning", 
    "supervisor": "basic", 
    "researcher": "basic", 
    "coder": "basic", 
    "browser": "vision", 
    "reporter": "basic", 
}



def get_llm(llm_type:LLMType)->ChatOpenAI:
    """
    Retrieves a Langchain OpenAI chat model of the specified type.

    Args:
        llm_type: The type of the LLM to retrieve.

    Returns:
        A Langchain OpenAI chat model of the specified type.

    Raises:
        ValueError: If the LLM type is unknown.
    """
    if llm_type == "basic":
        return init_chat_model(
            model=BASIC_MODEL_NAME,
            model_provider=BASIC_MODEL_PROVIDER,
            api_key=BASIC_MODEL_API_KEY
        )
    elif llm_type == "reasoning":
        return init_chat_model(
            model=REASONING_MODEL_NAME,
            model_provider=REASONING_MODEL_PROVIDER,
            api_key=REASONING_MODEL_API_KEY
        )
    elif llm_type == "vision":
        return init_chat_model(
            model=VL_MODEL_NAME,
            model_provider=VL_MODEL_PROVIDER,
            api_key=VL_MODEL_API_KEY
        )
    else:
        raise ValueError(f"Unknown LLM type: {llm_type}")
