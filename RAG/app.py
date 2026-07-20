import sys
import tempfile
from pathlib import Path

import streamlit as st

# =====================================
# Fix Imports
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))

# =====================================
# Local Imports
# =====================================

from src.ingestion.loader import (
    load_uploaded_document,
    chunk_documents
)

from src.embedding.embedder import (
    generate_embeddings
)

from src.embedding.indexer import (
    create_vectorstore
)

# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="Research Paper RAG",
    page_icon="📄",
    layout="wide"
)

# =====================================
# Session State
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False

if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

if "index_ready" not in st.session_state:
    st.session_state.index_ready = False

# =====================================
# Header
# =====================================

st.title("📄 Research Paper RAG")

st.write(
    "Upload any research paper and ask questions."
)

# =====================================
# Sidebar
# =====================================

with st.sidebar:

    st.header("Upload Research Paper")

    uploaded_pdf = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    top_k = st.slider(
        "Top K Chunks",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# =====================================
# Process Uploaded PDF
# =====================================

if uploaded_pdf is not None:

    if st.session_state.current_pdf != uploaded_pdf.name:

        with st.spinner("Processing PDF..."):

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp:

                tmp.write(uploaded_pdf.getbuffer())

                temp_pdf_path = tmp.name

            docs = load_uploaded_document(
                temp_pdf_path
            )

            chunks = chunk_documents(
                docs
            )

            records = generate_embeddings(
                chunks
            )

            create_vectorstore(
                records
            )

            st.session_state.current_pdf = uploaded_pdf.name

            st.session_state.pdf_loaded = True

            st.session_state.index_ready = True

            st.session_state.messages = []

            st.success(
                "✅ PDF indexed successfully!"
            )

# =====================================
# Display Chat
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            with st.expander("Sources"):

                for src in message["sources"]:

                    st.write(
                        f"📄 {src['filename']} | Page {src['page']}"
                    )

# =====================================
# Chat Section
# =====================================

if st.session_state.index_ready:

    prompt = st.chat_input(
        "Ask anything about the uploaded paper..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Searching paper..."):

                # Import AFTER index creation
                from src.generation.chain import ask_question

                result = ask_question(
                    question=prompt,
                    top_k=top_k
                )

                answer = result["answer"]

                sources = result["sources"]

                st.markdown(answer)

                if sources:

                    with st.expander("Sources"):

                        for src in sources:

                            st.write(
                                f"📄 {src['filename']} | Page {src['page']}"
                            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": sources
            }
        )

else:

    st.info(
        "📄 Upload a PDF to begin."
    )