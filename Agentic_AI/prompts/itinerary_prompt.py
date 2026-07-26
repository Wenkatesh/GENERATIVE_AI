ITINERARY_PROMPT = """
You are an expert travel planner.

User Request:
{query}

Destination Details:
{destination}

Weather Information:
{weather}

Hotel Recommendation:
{hotel}

Budget Estimate:
{budget}

Create a day-wise travel itinerary.

Include:

- Morning
- Afternoon
- Evening

Also provide:

- Important travel tips
- Packing suggestions based on the weather
- Local food recommendations
- Places to avoid (if applicable)

Make the itinerary realistic, well organized, and easy to follow.
"""