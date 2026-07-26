from app.llm import llm
from app.prompts.supervisor_prompt import SUPERVISOR_PROMPT


class SupervisorAgent:

    async def decide(self, query: str) -> str:

        prompt = SUPERVISOR_PROMPT.format(
            query=query
        )

        response = await llm.ainvoke(prompt)

        route = response.content.strip().lower()

        # Normalize the LLM output
        if "weather" in route:
            return "weather"

        if "hotel" in route:
            return "hotel"

        return "destination"