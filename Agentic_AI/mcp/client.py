from app.config import DATA_DIR, TAVILY_API_KEY
from langchain_mcp_adapters.client import MultiServerMCPClient


class MCPClient:
    """
    Central MCP client for the application.
    """

    def __init__(self) -> None:
        self.client = MultiServerMCPClient(
            {
                "filesystem": {
                    "transport": "stdio",
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        str(DATA_DIR),
                    ],
                },

                "tavily": {
                    "transport": "stdio",
                    "command": "npx",
                    "args": [
                        "-y",
                        "tavily-mcp@latest",
                    ],
                    "env": {
                        "TAVILY_API_KEY": TAVILY_API_KEY
                    },
                },
            }
        )

    async def get_tools(self):
        return await self.client.get_tools()