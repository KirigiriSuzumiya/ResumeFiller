from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
import contextlib


class ChromeMCPClient:

    def __init__(self):
        self.client = None
        self.session = None
        self._exit_stack = None
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
                    "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"],
                }
            }
        )

        # Use an AsyncExitStack to ensure the async context is exited from the
        # same task that entered it and that cleanup happens cleanly.
        self._exit_stack = contextlib.AsyncExitStack()
        self.session = await self._exit_stack.enter_async_context(
            self.client.session("chrome-devtools")
        )

        self.tools = await load_mcp_tools(self.session)

        self.is_initialized = True

    async def close(self):
        """Close any active session and release resources."""
        if self._exit_stack is not None:
            await self._exit_stack.aclose()
            self._exit_stack = None
        self.session = None
        self.tools = None
        self.is_initialized = False

    async def get_session(self):
        if not self.is_initialized:
            await self.initialize()
        return self.session

    async def get_tools(self):
        if not self.is_initialized:
            await self.initialize()
        return self.tools


chrome_mcp_client = ChromeMCPClient()