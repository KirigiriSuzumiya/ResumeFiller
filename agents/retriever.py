from tools import retrieve_context
from llms import base_chat_model
from langchain.agents import create_agent
from models import FormField

SYSTEM_PROMPT="""
你是一个高效的简历字段信息检索助手.
你需要根据用户所提供的字段名，通过检索工具来匹配合适的字段值.
所有的检索结果都必须基于检索工具所返回的内容。
如果无法通过检索工具获得合适的字段内容，那么将该字段的值返回为unknown
"""

retriever_agent = create_agent(
    model=base_chat_model,
    tools=[retrieve_context],
    system_prompt=SYSTEM_PROMPT,
    response_format=FormField,
)