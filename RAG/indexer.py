import faiss
import numpy as np
import json
from pathlib import Path
import yaml

CONFIG_PATH = "configs/config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


config = load_config()

VECTOR_DIM = config["vectorstore"]["dimension"]

VECTORSTORE_DIR = Path(config["paths"]["vectorstore_dir"])
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

INDEX_PATH = VECTORSTORE_DIR / "faiss.index"
METADATA_PATH = VECTORSTORE_DIR / "metadata.json"


def build_vectorstore(records):
    """
    Build FAISS index from embedding records.
    """

    print("Creating FAISS Index...")

    index = faiss.IndexFlatL2(VECTOR_DIM)

    vectors = []
    metadata_store = []

    for record in records:

        vectors.append(record["embedding"])

        metadata_store.append(
            {
                "text": record["text"],
                "metadata": record["metadata"]
            }
        )

    vectors = np.array(
        vectors,
        dtype=np.float32
    )

    index.add(vectors)

    print(f"Indexed {index.ntotal} chunks")

    return index, metadata_store


def save_vectorstore(index, metadata_store):
    """
    Save FAISS index and metadata.
    """

    faiss.write_index(
        index,
        str(INDEX_PATH)
    )

    with open(
        METADATA_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata_store,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("Vector Store Saved")
    print(INDEX_PATH)
    print(METADATA_PATH)


def create_vectorstore(records):
    """
    Complete pipeline.
    """

    index, metadata = build_vectorstore(records)

    save_vectorstore(index, metadata)

    return index, metadata