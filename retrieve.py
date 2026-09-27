import json
import sys
import numpy as np
from sentence_transformers import SentenceTransformer

VECTORS_FILE = "vectors.npy"
METADATA_FILE = "vector_metadata.json"
MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 3


def load_index():
    vectors = np.load(VECTORS_FILE)

    with open(METADATA_FILE, "r", encoding="utf-8") as file:
        metadata = json.load(file)

    return vectors, metadata


def retrieve(query, top_k=TOP_K):
    vectors, metadata = load_index()

    model = SentenceTransformer(MODEL_NAME)

    query_vector = model.encode(
        [query],
        normalize_embeddings=True
    )[0]

    # Calculate similarity
    scores = vectors @ query_vector

    # Get highest scores
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append({
            "score": float(scores[index]),
            "id": metadata[index]["id"],
            "source": metadata[index]["source"],
            "text": metadata[index]["text"]
        })

    return results


def main():

    if len(sys.argv) < 2:
        query = input("Enter your question: ")
    else:
        query = " ".join(sys.argv[1:])

    results = retrieve(query)

    print(f"\nQuery: {query}")
    print("\nTop results:")

    for number, result in enumerate(results, start=1):

        print(f"\n--- Result {number} ---")
        print(f"Score:  {result['score']:.4f}")
        print(f"Source: {result['source']}")
        print(f"ID:     {result['id']}")
        print(f"Text:   {result['text']}")


if __name__ == "__main__":
    main()