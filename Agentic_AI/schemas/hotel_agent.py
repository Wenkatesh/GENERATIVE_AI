from langchain_core.prompts import ChatPromptTemplate

from app.llm import llm
from app.mcp.registry import mcp_client
from app.prompts.hotel_prompt import HOTEL_PROMPT


class HotelAgent:

    async def recommend(self, query: str, destination: str):

        tools = await mcp_client.get_tools()

        search_tool = next(
            tool for tool in tools
            if tool.name == "tavily_search"
        )

        search_query = f"""
User Request:
{query}

Destination:
{destination}

Find the best hotels in {destination} that match the user's budget and travel preferences.

Include:
- Hotel name
- Approximate price per night
- Rating
- Key amenities
- Suitable traveler type
"""

        search_results = await search_tool.ainvoke(
            {
                "query": search_query
            }
        )

        prompt = ChatPromptTemplate.from_template(
            HOTEL_PROMPT
        )

        response = await llm.ainvoke(
            prompt.format(
                destination=destination,
                user_query=query,
                search_results=search_results
            )
        )

        return response.content