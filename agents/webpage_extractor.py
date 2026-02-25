from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware 
from llms import base_code_model
from tools import chrome_mcp_client
from models import FormField


from langchain.agents import create_agent




async def get_webpage_extractor():
    chrome_mcp_client.initialize()
    chrome_mcp_tools = await chrome_mcp_client.get_tools()
    return create_agent(
        model=base_code_model,
        tools= chrome_mcp_tools,
        system_prompt="你是一个专业的网页表单填写助手.你需要从用户所提供的浏览器网页表单中抽取出所有需要填写的字段信息.",
        response_format=FormField,
    )
