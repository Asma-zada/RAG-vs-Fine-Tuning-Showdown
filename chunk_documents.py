import os
import json

INPUT_FOLDER = "knowledge_base"
OUTPUT_FILE = "chunks.jsonl"
CHUNK_SIZE = 200


def create_chunks(text, chunk_size):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    for filename in os.listdir(INPUT_FOLDER):

        if filename.endswith(".txt"):

            filepath = os.path.join(INPUT_FOLDER, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                text = file.read()

            chunks = create_chunks(text, CHUNK_SIZE)

            for number, chunk in enumerate(chunks):

                record = {
                    "id": f"{filename}_{number}",
                    "source": filename,
                    "text": chunk
                }

                output.write(json.dumps(record) + "\n")

print("Chunking completed!")