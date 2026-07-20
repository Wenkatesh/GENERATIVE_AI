#  Research Paper RAG

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload research papers in PDF format and ask natural language questions about the document. The system extracts the content, generates semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant information, and produces context-aware answers using a Large Language Model (LLM).

---

##  Features

- Upload any research paper (PDF)
- Automatic document parsing and text extraction
- Intelligent text chunking
- Semantic embedding generation using Sentence Transformers
- FAISS vector database for fast similarity search
- Context-aware question answering using Groq LLM
- Source page references for every response
- Interactive Streamlit web interface

---

##  Project Architecture

```
Upload PDF
      │
      ▼
Document Loader
      │
      ▼
Text Cleaning
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Groq LLM
      │
      ▼
Generated Answer
```

---

##  Project Structure

```
research-paper-rag/
│
├── app.py
├── configs/
│   └── config.yaml
│
├── src/
│   ├── ingestion/
│   │   └── loader.py
│   │
│   ├── embedding/
│   │   ├── embedder.py
│   │   └── indexer.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   └── generation/
│       └── chain.py
│
├── vectorstore/
│
├── requirements.txt
│
└── README.md
```

---

##  Technologies Used

- Python
- Streamlit
- LangChain
- Sentence Transformers
- FAISS
- Groq LLM
- Hugging Face Embeddings
- PyPDF / Docling
- NumPy

---

##  Workflow

### Step 1: Upload PDF

The user uploads a research paper through the Streamlit interface.

### Step 2: Document Processing

The PDF is parsed and converted into text.

### Step 3: Text Chunking

The extracted text is divided into overlapping chunks for better retrieval.

### Step 4: Embedding Generation

Each chunk is converted into dense vector embeddings using a Sentence Transformer model.

### Step 5: Vector Store Creation

The embeddings are indexed using FAISS for efficient similarity search.

### Step 6: User Query

The user asks a question related to the uploaded document.

### Step 7: Semantic Retrieval

The system retrieves the most relevant chunks from the FAISS index.

### Step 8: Answer Generation

The retrieved context is passed to the Groq LLM, which generates an accurate response based only on the uploaded document.

---

##  Example

### Upload

```
Attention Is All You Need.pdf
```

### Question

```
What is self-attention?
```

### Answer

```
Self-attention is a mechanism that allows each token in a sequence to attend to every other token, enabling the model to capture contextual relationships without recurrence.
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/research-paper-rag.git
```

Move into the project

```bash
cd research-paper-rag
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

You can add screenshots here after deployment.

Example:

- Upload Page
- Chat Interface
- Source References

---

##  Future Improvements

- Multi-document support
- Chat history with memory
- Hybrid Retrieval (BM25 + Dense Embeddings)
- Document summarization
- Citation highlighting
- Multi-modal document support
- Persistent vector database
- User authentication

---

##  License

This project is intended for educational and research purposes.

---

##  Author

**Venkatesh M**

Artificial Intelligence & Data Science Engineer

Passionate about Machine Learning, NLP, Large Language Models, and Retrieval-Augmented Generation (RAG).
