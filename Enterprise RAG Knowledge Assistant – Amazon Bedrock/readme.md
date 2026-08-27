# Enterprise Knowledge Base Q&A System

A **Retrieval-Augmented Generation (RAG)** application that enables employees to ask natural-language questions about proprietary company documents and receive accurate, citation-backed answers.

The system uses **Amazon Bedrock Knowledge Bases** for managed document retrieval and an LLM for grounded response generation.

## 🚀 Features

* Natural-language Q&A over private enterprise documents
* Semantic search using Amazon Bedrock Knowledge Bases
* Citation-backed responses
* Streamlit web interface
* Secure AWS access using IAM roles
* Deployed on Amazon EC2

## 🏗️ Architecture

```text
Company Documents
       ↓
    Amazon S3
       ↓
Amazon Bedrock Knowledge Base
       ↓
Semantic Retrieval
       ↓
Amazon Bedrock LLM
       ↓
Answer + Citations
       ↓
   Streamlit UI
```

## 🛠️ Tech Stack

* Python
* Amazon Bedrock
* Amazon Bedrock Knowledge Bases
* Amazon S3
* AWS IAM
* AWS EC2
* Streamlit
* Boto3

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/enterprise-kb-rag.git
cd enterprise-kb-rag
```

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure AWS

Configure:

* Amazon S3 document data source
* Amazon Bedrock Knowledge Base
* Bedrock foundation model
* IAM permissions

For EC2 deployment, use an **IAM instance role** instead of storing AWS credentials.

### 4. Run the application

```bash
streamlit run app.py
```

## ☁️ AWS Deployment

The application is deployed on **Amazon EC2** and accesses Amazon Bedrock and S3 through IAM.

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Configure the EC2 Security Group to allow access to the Streamlit application.

## 🎯 Example

**Question:**

> What is the company's remote work policy?

**Response:**

The system retrieves relevant information from the Knowledge Base and generates an answer based on the retrieved documents, along with their source citations.

## 📌 Key Concepts

**RAG • Semantic Search • Amazon Bedrock • Knowledge Bases • LLMs • AWS IAM • EC2 • S3 • Streamlit**

