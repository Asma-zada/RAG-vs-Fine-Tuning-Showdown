import json
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = "chunks.jsonl"
VECTORS_FILE = "vectors.npy"
METADATA_FILE = "vector_metadata.json"

MODEL_NAME = "all-MiniLM-L6-v2"


def load_chunks():
    chunks = []

    with open(CHUNKS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line:
                chunks.append(json.loads(line))

    return chunks


def main():
    chunks = load_chunks()

    if not chunks:
        print("No chunks found in chunks.jsonl")
        return

    # Load the embedding model
    model = SentenceTransformer(MODEL_NAME)

    # Get the text from every chunk
    texts = [chunk["text"] for chunk in chunks]

    # Convert text into embeddings
    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    # Save embeddings
    np.save(VECTORS_FILE, embeddings)

    # Save chunk information
    metadata = [
        {
            "id": chunk["id"],
            "source": chunk["source"],
            "text": chunk["text"]
        }
        for chunk in chunks
    ]

    with open(METADATA_FILE, "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=2, ensure_ascii=False)

    print(f"Created {VECTORS_FILE}")
    print(f"Created {METADATA_FILE}")
    print(f"Indexed {len(chunks)} chunks.")


if __name__ == "__main__":
    main()