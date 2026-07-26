from langchain_core.prompts import ChatPromptTemplate

from app.llm import llm
from app.prompts.itinerary_prompt import ITINERARY_PROMPT


class ItineraryAgent:

    async def generate(
        self,
        query: str,
        destination: str,
        weather: str,
        hotel: str,
        budget: str
    ):

        prompt = ChatPromptTemplate.from_template(
            ITINERARY_PROMPT
        )

        response = await llm.ainvoke(
            prompt.format(
                query=query,
                destination=destination,
                weather=weather,
                hotel=hotel,
                budget=budget
            )
        )

        return response.content