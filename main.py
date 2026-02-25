from agents.webpage_extractor import get_webpage_extractor
from models import FormField
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
    form_field: FormField = response["structured_response"]
    print(form_field)

if __name__ == "__main__":
    asyncio.run(main())
