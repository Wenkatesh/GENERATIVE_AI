import os
import logging
import streamlit as st

# -----------------------------------
# FIRST STREAMLIT COMMAND
# -----------------------------------

st.set_page_config(
    page_title="AI Blog Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# IMPORTS
# -----------------------------------

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_core.output_parsers import StrOutputParser

# -----------------------------------
# LOGGING CONFIGURATION
# -----------------------------------

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# -----------------------------------
# LOAD ENV VARIABLES
# -----------------------------------

load_dotenv()

# -----------------------------------
# GEMINI MODEL
# -----------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
    max_output_tokens=500
)

# -----------------------------------
# PROMPT TEMPLATE
# -----------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Blog Assistant.

Instructions:
- Generate structured blog content
- Use headings
- Keep responses concise
- Avoid fake information
"""
        ),

        MessagesPlaceholder(
            variable_name="history",
            n_messages=6
        ),

        (
            "human",
            "{user_input}"
        )
    ]
)

# -----------------------------------
# OUTPUT PARSER
# -----------------------------------

parser = StrOutputParser()

# -----------------------------------
# CREATE CHAIN
# -----------------------------------

chain = prompt | llm | parser

# -----------------------------------
# CHAT MEMORY
# -----------------------------------

if "chat_history" not in st.session_state:

    st.session_state.chat_history = (
        InMemoryChatMessageHistory()
    )

# -----------------------------------
# MEMORY FUNCTION
# -----------------------------------

def get_session_history(session_id):

    return st.session_state.chat_history

# -----------------------------------
# ADD MEMORY TO CHAIN
# -----------------------------------

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="user_input",
    history_messages_key="history"
)

# -----------------------------------
# STREAMLIT UI
# -----------------------------------

st.title("🤖 AI Blog Assistant")

st.markdown(
    "Generate blog content using Gemini + LangChain"
)

# -----------------------------------
# DISPLAY OLD MESSAGES
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------------
# USER INPUT
# -----------------------------------

user_input = st.chat_input(
    "Enter your blog request..."
)

# -----------------------------------
# GENERATE RESPONSE
# -----------------------------------

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_input)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Generating response..."):

            try:

                logger.info(
                    "Sending request to Gemini API"
                )

                response = chain_with_memory.invoke(
                    {
                        "user_input": user_input
                    },

                    config={
                        "configurable": {
                            "session_id": "user_1"
                        }
                    }
                )

                logger.info(
                    "Response generated successfully"
                )

            except Exception as e:

                logger.error(f"Error: {e}")

                response = (
                    "Unable to generate response."
                )

            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )