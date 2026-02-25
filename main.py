from agents.webpage_extractor import get_webpage_extractor
from agents.retriever import retriever_agent
from agents.form_filler import get_form_filler
from tools import chrome_mcp_client
from models import FormField
from knowledge import information_entry
import asyncio

async def main():
    webpage_extractor = await get_webpage_extractor()
    response = await webpage_extractor.ainvoke(
        {
            "messages": [
                    {"role": "user", "content":"处理我当前打开标签页中的字段信息"}
                ]
        }
    )
    print(response)
    form_field: FormField = response["structured_response"]
    
    response = retriever_agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "\n".join([f"字段名：{i.name} uid:{i.uid}" for i in form_field.fields])}
            ]
        }
    )
    form_field: FormField = response["structured_response"]
    
    for field in form_field.fields:
        if field.value == "unknown":
            field.value = input(f"请补充「{field.name}」：")
            information_entry(field.name, field.value)
            print("字段信息已持久化加入检索库！")

    form_filler = await get_form_filler()
    response = await form_filler.ainvoke(
        {
            "messages": [
                    {"role": "user", "content":form_field.__str__()}
                ]
        }
    )
    
    print(response)
    await chrome_mcp_client.close()
    

if __name__ == "__main__":
    asyncio.run(main())