#  AI Multi-Agent Travel Planner

An intelligent **AI-powered Multi-Agent Travel Planner** built using **LangGraph, LangChain, Groq LLM, MCP (Model Context Protocol), Tavily Search, and Streamlit**.

The application uses multiple specialized AI agents that collaborate to generate personalized travel plans including destination recommendations, weather updates, hotel suggestions, budget estimation, and day-wise itineraries.

---

#  Features

-  Multi-Agent Architecture using LangGraph
-  Supervisor Agent for intelligent routing
-  Destination Recommendation Agent
-  Real-time Weather Analysis
-  Hotel Recommendation Agent
-  Budget Estimation Agent
-  AI-generated Day-wise Travel Itinerary
-  Real-time Web Search using Tavily MCP
-  Powered by Groq Llama 3.3 70B Model
-  Interactive Streamlit Interface

---

# 🏗 Project Architecture

```
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
          LangGraph Workflow
                  │
                  ▼
         Supervisor Agent
                  │
                  ▼
       Destination Agent
                  │
                  ▼
         Weather Agent
                  │
                  ▼
          Hotel Agent
                  │
                  ▼
         Budget Agent
                  │
                  ▼
       Itinerary Agent
                  │
                  ▼
          Final Travel Plan
```

---

# 🤖 Multi-Agent Workflow

### 1️⃣ Supervisor Agent

- Understands the user's request.
- Decides which workflow should be executed.
- Routes the request to the appropriate agent using LangGraph.

---

### 2️⃣ Destination Agent

- Searches for suitable travel destinations.
- Uses Tavily Search to retrieve travel information.
- Returns:
  - Destination Name
  - Destination Summary
  - Best Time to Visit
  - Estimated Budget

---

### 3️⃣ Weather Agent

- Retrieves live weather information.
- Provides:
  - Current Temperature
  - Weather Conditions
  - Travel Tips
  - Clothing Suggestions

---

### 4️⃣ Hotel Agent

- Searches hotels based on:
  - Destination
  - User Budget
- Recommends hotels with:
  - Ratings
  - Amenities
  - Approximate Price

---

### 5️⃣ Budget Agent

Calculates estimated travel expenses including:

- Hotel
- Food
- Transportation
- Sightseeing
- Miscellaneous Expenses

Provides money-saving recommendations.

---

### 6️⃣ Itinerary Agent

Generates a complete day-wise travel itinerary using:

- Destination Details
- Weather
- Hotel Information
- Budget

Includes:

- Places to Visit
- Food Recommendations
- Travel Tips
- Packing Suggestions

---

# 🛠 Tech Stack

## Programming Language

- Python

## Frameworks

- LangGraph
- LangChain
- Streamlit

## Large Language Model

- Groq
- Llama 3.3 70B Versatile

## Search Tool

- Tavily Search
- Model Context Protocol (MCP)

## Prompt Engineering

- Structured Prompting
- Role Prompting
- JSON Output Prompting

---

# 📂 Project Structure

```
AI-Multi-Agent-Travel-Planner/

│

├── app/
│   │
│   ├── graph/
│   │      ├── travel.py
│   │      └── state.py
│   │
│   ├── schemas/
│   │      ├── supervisor_agent.py
│   │      ├── destination_agent.py
│   │      ├── weather_agent.py
│   │      ├── hotel_agent.py
│   │      ├── budget_agent.py
│   │      └── itinerary_agent.py
│   │
│   ├── prompts/
│   │      ├── supervisor_prompt.py
│   │      ├── destination_prompt.py
│   │      ├── weather_prompt.py
│   │      ├── hotel_prompt.py
│   │      ├── budget_prompt.py
│   │      └── itinerary_prompt.py
│   │
│   ├── llm.py
│   └── mcp/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Workflow

```
User Query
      │
      ▼
Supervisor Agent
      │
      ▼
Destination Agent
      │
      ▼
Weather Agent
      │
      ▼
Hotel Agent
      │
      ▼
Budget Agent
      │
      ▼
Itinerary Agent
      │
      ▼
Final AI Travel Plan
```

---

#  Prompt Engineering

Each AI agent has its own specialized prompt designed for a specific task.

- Supervisor Prompt
- Destination Prompt
- Weather Prompt
- Hotel Prompt
- Budget Prompt
- Itinerary Prompt

This modular prompt design improves:

- Maintainability
- Reusability
- Response Quality
- Scalability

---

# 📌 Example User Query

```
Plan a 3-day trip under ₹20,000
```

The system generates:

- Recommended Destination
- Best Time to Visit
- Weather Forecast
- Hotel Recommendations
- Budget Breakdown
- Complete Day-wise Itinerary

---

#  Key Concepts Demonstrated

- Multi-Agent Systems
- Agent Orchestration
- LangGraph Workflows
- Prompt Engineering
- State Management
- Conditional Routing
- Tool Calling
- Retrieval-Augmented Generation (RAG)
- Real-Time Web Search
- AI Workflow Automation

---

#  Future Improvements

- Flight Recommendation Agent
- Restaurant Recommendation Agent
- Google Maps Integration
- Currency Conversion
- Live Hotel Booking APIs
- Conversation Memory
- Personalized Recommendations
- Parallel Agent Execution
- PDF Itinerary Export
- Voice-based Travel Assistant

---

# 📈 Learning Outcomes

This project demonstrates practical implementation of:

- Large Language Models (LLMs)
- Multi-Agent AI Systems
- LangGraph Orchestration
- Prompt Engineering
- Model Context Protocol (MCP)
- Real-Time Information Retrieval
- Streamlit Application Development
- AI Workflow Design

---

# 👨‍💻 Author

**Venkatesh Madaparthi**

AI/ML & Generative AI Enthusiast

- Python
- Machine Learning
- Deep Learning
- LangChain
- LangGraph
- MCP
- Generative AI
