import re
from pathlib import Path

from langchain_docling import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import yaml

CONFIG_PATH = "configs/config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


config = load_config()


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_uploaded_document(pdf_path):
    """
    Load a single uploaded PDF.
    """

    print(f"Loading: {pdf_path}")

    loader = DoclingLoader(file_path=str(pdf_path))

    docs = loader.load()

    for doc in docs:
        doc.page_content = clean_text(doc.page_content)

        doc.metadata["filename"] = Path(pdf_path).name

    return docs


def chunk_documents(documents):
    """
    Split documents into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config["chunking"]["chunk_size"],
        chunk_overlap=config["chunking"]["chunk_overlap"],
    )

    chunks = []

    chunk_index = 0

    for doc in documents:

        split_docs = splitter.create_documents(
            [doc.page_content]
        )

        for split_doc in split_docs:

            chunks.append(
                {
                    "text": split_doc.page_content,
                    "metadata": {
                        "filename": doc.metadata.get("filename"),
                        "page_number": doc.metadata.get("page", 1),
                        "chunk_index": chunk_index,
                    },
                }
            )

            chunk_index += 1

    return chunks