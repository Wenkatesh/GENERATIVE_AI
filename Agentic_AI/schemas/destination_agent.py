import json

from app.llm import llm
from app.mcp.registry import mcp_client
from app.prompts.destination_prompt import DESTINATION_PROMPT


class DestinationAgent:

    async def recommend(self, query: str):

        tools = await mcp_client.get_tools()

        search_tool = next(
            tool for tool in tools
            if tool.name == "tavily_search"
        )

        search_results = await search_tool.ainvoke(
            {
                "query": query
            }
        )

        prompt = DESTINATION_PROMPT.format(
            search_results=search_results
        )

        response = await llm.ainvoke(prompt)

        # Parse JSON returned by the LLM
        destination = json.loads(response.content)

        return {
            "destination_name": destination["destination_name"],
            "destination_summary": destination["destination_summary"],
            "best_time": destination["best_time"],
            "estimated_budget": destination["estimated_budget"],
        }