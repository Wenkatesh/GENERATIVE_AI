import sys
from pathlib import Path

# =====================================
# Fix Imports
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.append(str(PROJECT_ROOT))

# =====================================
# Environment Variables
# =====================================

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

# =====================================
# LangChain Imports
# =====================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# =====================================
# Local Import
# =====================================

from src.retrieval.retriever import retrieve

# =====================================
# Prompt
# =====================================

PROMPT = ChatPromptTemplate.from_template(
"""
You are an AI Research Paper Assistant.

Rules:

1. Answer ONLY from the retrieved context.

2. Do NOT make up information.

3. If the answer is not available in the context, reply:

"I could not find this in the uploaded document."

------------------------

Context:

{context}

------------------------

Question:

{question}

------------------------

Answer:
"""
)

# =====================================
# LLM
# =====================================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

parser = StrOutputParser()

MAX_CONTEXT_CHARS = 12000


# =====================================
# Build Context
# =====================================

def build_context(retrieved_docs):

    if not retrieved_docs:
        return ""

    context = []

    total = 0

    for doc in retrieved_docs:

        text = doc["text"]

        if total + len(text) > MAX_CONTEXT_CHARS:
            break

        meta = doc["metadata"]

        filename = meta.get(
            "filename",
            "Unknown File"
        )

        page = meta.get(
            "page_number",
            "Unknown"
        )

        context.append(

            f"""
SOURCE : {filename}
PAGE   : {page}

{text}
"""
        )

        total += len(text)

    return "\n\n".join(context)


# =====================================
# Ask Question
# =====================================

def ask_question(
    question,
    top_k=5
):

    retrieved_docs = retrieve(
        query=question,
        top_k=top_k
    )

    if len(retrieved_docs) == 0:

        return {
            "answer":
            "I could not find this in the uploaded document.",
            "sources":[]
        }

    context = build_context(
        retrieved_docs
    )

    chain = (
        PROMPT
        | llm
        | parser
    )

    answer = chain.invoke(
        {
            "context":context,
            "question":question
        }
    )

    sources = []

    for doc in retrieved_docs:

        meta = doc["metadata"]

        sources.append(
            {
                "filename":meta.get("filename"),
                "page":meta.get("page_number"),
                "chunk":meta.get("chunk_index")
            }
        )

    return {

        "answer":answer,

        "sources":sources

    }


# =====================================
# Testing
# =====================================

if __name__ == "__main__":

    while True:

        question = input("\nAsk Question (exit to quit): ")

        if question.lower() == "exit":
            break

        result = ask_question(question)

        print("\n")
        print("="*80)
        print(result["answer"])
        print("="*80)

        print("\nSources:\n")

        for s in result["sources"]:

            print(
                f"{s['filename']} | Page {s['page']}"
            )