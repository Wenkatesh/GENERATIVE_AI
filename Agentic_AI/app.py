import streamlit as st
import asyncio

from app.graph.travel import travel_graph

st.set_page_config(
    page_title="AI Multi-Agent Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Multi-Agent Travel Planner")
st.caption("Powered by LangGraph • Groq • MCP • Tavily")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
query = st.chat_input("Where do you want to travel?")

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):

        with st.spinner("Planning your trip..."):

            result = asyncio.run(
                travel_graph.ainvoke(
                    {
                        "query": query
                    }
                )
            )

        st.markdown("## 📍 Destination")
        st.write(result["destination_name"])

        st.markdown("### 📖 Destination Details")
        st.write(result["destination_summary"])

        st.markdown("### 🗓 Best Time to Visit")
        st.write(result["best_time"])

        st.markdown("### 💵 Estimated Trip Budget")
        st.write(result["estimated_budget"])

        st.markdown("---")

        st.markdown("## 🌦 Weather")
        st.write(result["weather"])

        st.markdown("---")

        st.markdown("## 🏨 Hotels")
        st.write(result["hotel"])

        st.markdown("---")

        st.markdown("## 💰 Budget Estimate")
        st.write(result["budget"])

        st.markdown("---")

        st.markdown("## 🗓 Itinerary")
        st.write(result["itinerary"])

        response = f"""
## 📍 Destination

**{result['destination_name']}**

### 📖 Destination Details

{result['destination_summary']}

### 🗓 Best Time to Visit

{result['best_time']}

### 💵 Estimated Trip Budget

{result['estimated_budget']}

---

## 🌦 Weather

{result['weather']}

---

## 🏨 Hotels

{result['hotel']}

---

## 💰 Budget Estimate

{result['budget']}

---

## 🗓 Itinerary

{result['itinerary']}
"""

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )