from langchain_core.prompts import ChatPromptTemplate

from app.llm import llm
from app.mcp.registry import mcp_client
from app.prompts.weather_prompt import WEATHER_PROMPT


class WeatherAgent:

    async def analyze(self, destination: str):

        tools = await mcp_client.get_tools()

        search_tool = next(
            tool for tool in tools
            if tool.name == "tavily_search"
        )

        # Search current weather for the destination
        query = f"Current weather in {destination}"

        search_results = await search_tool.ainvoke(
            {
                "query": query
            }
        )

        prompt = ChatPromptTemplate.from_template(
            WEATHER_PROMPT
        )

        response = await llm.ainvoke(
            prompt.format(
                destination=destination,
                search_results=search_results
            )
        )

        return response.content