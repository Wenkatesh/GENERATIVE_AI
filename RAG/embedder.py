import hashlib
import json
from pathlib import Path

import yaml
from sentence_transformers import SentenceTransformer

CONFIG_PATH = "configs/config.yaml"


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


config = load_config()

MODEL_NAME = config["embedding"]["model_name"]
BATCH_SIZE = config["embedding"]["batch_size"]

CACHE_DIR = Path("data/cache/embeddings")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

print(f"Loading embedding model: {MODEL_NAME}")

model = SentenceTransformer(MODEL_NAME)


def get_checksum(text):
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def load_cached_embedding(checksum):

    cache_file = CACHE_DIR / f"{checksum}.json"

    if cache_file.exists():

        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)

    return None


def save_cached_embedding(checksum, record):

    cache_file = CACHE_DIR / f"{checksum}.json"

    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(record, f)


def generate_embeddings(chunks):
    """
    Generate embeddings directly from chunks.
    """

    records = []

    uncached_chunks = []
    uncached_indices = []

    for idx, chunk in enumerate(chunks):

        checksum = get_checksum(chunk["text"])

        cached = load_cached_embedding(checksum)

        if cached:

            records.append(cached)

        else:

            records.append(None)

            uncached_chunks.append(chunk)

            uncached_indices.append(idx)

    print(f"Cached chunks : {len(chunks)-len(uncached_chunks)}")
    print(f"New chunks    : {len(uncached_chunks)}")

    for start in range(0, len(uncached_chunks), BATCH_SIZE):

        batch = uncached_chunks[start:start+BATCH_SIZE]

        texts = [x["text"] for x in batch]

        embeddings = model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        for chunk, embedding, idx in zip(
            batch,
            embeddings,
            uncached_indices[start:start+BATCH_SIZE]
        ):

            checksum = get_checksum(chunk["text"])

            record = {
                "embedding": embedding.tolist(),
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "checksum": checksum
            }

            save_cached_embedding(
                checksum,
                record
            )

            records[idx] = record

    return records