from langchain.agents import create_agent
from llms import base_chat_model
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

agent = create_agent(
    model=base_chat_model,
    tools=[get_weather],
)

