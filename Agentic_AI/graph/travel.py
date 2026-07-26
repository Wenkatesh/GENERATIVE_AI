from langgraph.graph import StateGraph, END

from app.graph.state import TravelState

from app.schemas.supervisor_agent import SupervisorAgent
from app.schemas.destination_agent import DestinationAgent
from app.schemas.weather_agent import WeatherAgent
from app.schemas.hotel_agent import HotelAgent
from app.schemas.budget_agent import BudgetAgent
from app.schemas.itinerary_agent import ItineraryAgent


# --------------------------------------------------
# Agent Instances
# --------------------------------------------------

supervisor = SupervisorAgent()

destination_agent = DestinationAgent()
weather_agent = WeatherAgent()
hotel_agent = HotelAgent()
budget_agent = BudgetAgent()
itinerary_agent = ItineraryAgent()


# --------------------------------------------------
# Supervisor Node
# --------------------------------------------------

async def supervisor_node(state: TravelState):

    next_agent = await supervisor.decide(
        state["query"]
    )

    return {
        "next_agent": next_agent
    }


# --------------------------------------------------
# Destination
# --------------------------------------------------

async def destination_node(state: TravelState):

    destination = await destination_agent.recommend(
        state["query"]
    )

    return {
        "destination_name": destination["destination_name"],
        "destination_summary": destination["destination_summary"],
        "best_time": destination["best_time"],
        "estimated_budget": destination["estimated_budget"],
    }


# --------------------------------------------------
# Weather
# --------------------------------------------------

async def weather_node(state: TravelState):

    weather = await weather_agent.analyze(
        state["destination_name"]
    )

    return {
        "weather": weather
    }


# --------------------------------------------------
# Hotel
# --------------------------------------------------

async def hotel_node(state: TravelState):

    hotel = await hotel_agent.recommend(
        query=state["query"],
        destination=state["destination_name"]
    )

    return {
        "hotel": hotel
    }


# --------------------------------------------------
# Budget
# --------------------------------------------------

async def budget_node(state: TravelState):

    budget = await budget_agent.estimate(
        query=state["query"],
        destination=state["destination_name"],
        hotel=state["hotel"]
    )

    return {
        "budget": budget
    }


# --------------------------------------------------
# Itinerary
# --------------------------------------------------

async def itinerary_node(state: TravelState):

    itinerary = await itinerary_agent.generate(
        query=state["query"],
        destination=state["destination_summary"],
        weather=state["weather"],
        hotel=state["hotel"],
        budget=state["budget"]
    )

    return {
        "itinerary": itinerary
    }


# --------------------------------------------------
# Graph
# --------------------------------------------------

builder = StateGraph(TravelState)

builder.add_node("supervisor", supervisor_node)
builder.add_node("destination", destination_node)
builder.add_node("weather", weather_node)
builder.add_node("hotel", hotel_node)
builder.add_node("budget", budget_node)
builder.add_node("itinerary", itinerary_node)

builder.set_entry_point("supervisor")

builder.add_conditional_edges(
    "supervisor",
    lambda state: state["next_agent"],
    {
        "destination": "destination",
        "weather": "weather",
        "hotel": "hotel",
    }
)

builder.add_edge("destination", "weather")
builder.add_edge("weather", "hotel")
builder.add_edge("hotel", "budget")
builder.add_edge("budget", "itinerary")

builder.add_edge("weather", END)
builder.add_edge("hotel", END)

builder.add_edge("itinerary", END)

travel_graph = builder.compile()

