from langchain.agents import create_agent
from llms import base_code_model
from tools import chrome_mcp_client

SYSTEM_PROMPT= """
你是一个专业的网页表单填写助手.
你需要通过工具连接到用户的浏览器，并根据用户所提供的UID找到输入对象，并逐个将值通过调用ChromeMCP工具填入到对应的表单中
如果需要输入的表单对象是选择型，你需要点击表单对象后再查看选项，并根据用户所提供的字段值来选择合适的选项.
"""

async def get_form_filler():
    await chrome_mcp_client.initialize()
    chrome_mcp_tools = await chrome_mcp_client.get_tools()
    return create_agent(
        model=base_code_model,
        tools=chrome_mcp_tools,
        system_prompt=SYSTEM_PROMPT,
    )
