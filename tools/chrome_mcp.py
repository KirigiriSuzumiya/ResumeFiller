from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

class ChromeMCPClient:
    
    def __init__(self):
        self.client = None
        self.session = None
        self._session_context = None
        self.tools = None
        self.is_initialized = False

    async def initialize(self):
        if self.is_initialized:
            return
        
        self.client = MultiServerMCPClient(  
            {
                "chrome-devtools": {
                    "transport": "stdio",
                    "command": "npx",
                    "args": ["-y", "chrome-devtools-mcp@latest","--autoConnect"]
                }
            }
        )
        
        self._session_context = self.client.session("chrome-devtools")
        self.session = await self._session_context.__aenter__()
        
        self.tools = await load_mcp_tools(self.session)
        
        self.is_initialized = True

    async def get_session(self):
        if not self.is_initialized:
            await self.initialize()
        return self.session

    async def get_tools(self):
        if not self.is_initialized:
            await self.initialize()
        return self.tools

chrome_mcp_client = ChromeMCPClient()