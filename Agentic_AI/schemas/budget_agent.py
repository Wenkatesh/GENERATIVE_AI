from langchain_core.prompts import ChatPromptTemplate

from app.llm import llm
from app.prompts.budget_prompt import BUDGET_PROMPT


class BudgetAgent:

    async def estimate(
        self,
        query: str,
        destination: str,
        hotel: str
    ):

        prompt = ChatPromptTemplate.from_template(
            BUDGET_PROMPT
        )

        response = await llm.ainvoke(
            prompt.format(
                query=query,
                destination=destination,
                hotel=hotel
            )
        )

        return response.content