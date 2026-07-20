import json
from pathlib import Path

import faiss
import numpy as np
import yaml
from sentence_transformers import SentenceTransformer

CONFIG_PATH = "configs/config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


config = load_config()

MODEL_NAME = config["embedding"]["model_name"]

VECTORSTORE_DIR = Path(config["paths"]["vectorstore_dir"])

INDEX_PATH = VECTORSTORE_DIR / "faiss.index"
METADATA_PATH = VECTORSTORE_DIR / "metadata.json"

print(f"Loading embedding model: {MODEL_NAME}")

model = SentenceTransformer(MODEL_NAME)


class Retriever:

    def __init__(self):

        self.index = None
        self.metadata = None

    def load_vectorstore(self):

        if self.index is not None:
            return

        if not INDEX_PATH.exists():
            raise FileNotFoundError(
                "Please upload a PDF first."
            )

        if not METADATA_PATH.exists():
            raise FileNotFoundError(
                "Please upload a PDF first."
            )

        self.index = faiss.read_index(str(INDEX_PATH))

        with open(
            METADATA_PATH,
            "r",
            encoding="utf-8"
        ) as f:

            self.metadata = json.load(f)

    def retrieve(
        self,
        query,
        top_k=5
    ):

        self.load_vectorstore()

        query_embedding = model.encode(
            [query],
            convert_to_numpy=True
        )

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        )

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, idx in zip(
            distances[0],
            indices[0]
        ):

            if idx == -1:
                continue

            item = self.metadata[idx]

            results.append(
                {
                    "text": item["text"],
                    "metadata": item["metadata"],
                    "score": float(distance)
                }
            )

        return results


retriever = Retriever()


def retrieve(query, top_k=5):

    return retriever.retrieve(
        query=query,
        top_k=top_k
    )