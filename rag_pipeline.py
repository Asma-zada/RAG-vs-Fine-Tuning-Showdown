import json
import sys

import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel


# ============================================================
# SETTINGS
# ============================================================

VECTORS_FILE = "vectors.npy"
METADATA_FILE = "vector_metadata.json"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Base model used during LoRA fine-tuning
BASE_MODEL = "google/flan-t5-small"

# Your LoRA adapter
ADAPTER_PATH = "saved_lora_model\\saved_lora_model"

# Number of chunks retrieved for each question
TOP_K = 3

# Evaluation input/output files
EVAL_FILE = "eval_v3.jsonl"
RESULTS_FILE = "rag_eval_results.jsonl"


# ============================================================
# DEVICE
# ============================================================

if torch.cuda.is_available():
    DEVICE = "cuda"
else:
    DEVICE = "cpu"

print(f"Using device: {DEVICE}")

if DEVICE == "cuda":
    print(f"GPU: {torch.cuda.get_device_name(0)}")


# ============================================================
# LOAD VECTOR INDEX
# ============================================================

def load_index():

    vectors = np.load(VECTORS_FILE)

    with open(
        METADATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        metadata = json.load(file)

    return vectors, metadata


# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

def load_embedding_model():

    print("\nLoading embedding model...")

    embedding_model = SentenceTransformer(
        EMBEDDING_MODEL,
        device=DEVICE
    )

    print("Embedding model loaded.")

    return embedding_model


# ============================================================
# RETRIEVE TOP-K CHUNKS
# ============================================================

def retrieve(
    query,
    vectors,
    metadata,
    embedding_model,
    top_k=TOP_K
):

    query_vector = embedding_model.encode(
        [query],
        normalize_embeddings=True
    )[0]

    # Cosine similarity because vectors are normalized
    scores = vectors @ query_vector

    # Highest scores first
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in top_indices:

        results.append(
            {
                "score": float(scores[index]),
                "id": metadata[index]["id"],
                "source": metadata[index]["source"],
                "text": metadata[index]["text"]
            }
        )

    return results


# ============================================================
# BUILD GROUNDED PROMPT
# ============================================================

def build_prompt(
    question,
    retrieved_chunks
):

    context = "\n\n".join(
        [
            (
                f"Source: {chunk['source']}\n"
                f"{chunk['text']}"
            )
            for chunk in retrieved_chunks
        ]
    )

    prompt = f"""
You are a helpful Cloud Explainer Assistant.

Answer the user's question using ONLY the information
provided in the context.

Do not use outside knowledge.
Do not make up facts.

If the context does not contain enough information
to answer the question, say:

"The provided context does not contain enough information
to answer this question."

Context:
{context}

User question:
{question}

Answer:
"""

    return prompt.strip()


# ============================================================
# LOAD FINE-TUNED GENERATOR
# ============================================================

def load_generator():

    print("\nLoading base FLAN-T5 model...")

    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL,
        use_fast=False
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        BASE_MODEL
    )

    print("Loading LoRA adapter...")

    model = PeftModel.from_pretrained(
        model,
        ADAPTER_PATH
    )

    # Move model to GPU or CPU
    model = model.to(DEVICE)

    model.eval()

    print(f"Generator model loaded on: {DEVICE}")

    return tokenizer, model


# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(
    question,
    retrieved_chunks,
    tokenizer,
    model
):

    prompt = build_prompt(
        question,
        retrieved_chunks
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Move input tensors to the same device as the model
    inputs = {
        key: value.to(DEVICE)
        for key, value in inputs.items()
    }

    # No gradients are needed during inference
    with torch.inference_mode():

        outputs = model.generate(
            **inputs,
            max_new_tokens=128
        )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer.strip()


# ============================================================
# RUN ONE RAG QUESTION
# ============================================================

def run_rag(
    question,
    vectors,
    metadata,
    embedding_model,
    tokenizer,
    model
):

    retrieved_chunks = retrieve(
        question,
        vectors,
        metadata,
        embedding_model,
        TOP_K
    )

    answer = generate_answer(
        question,
        retrieved_chunks,
        tokenizer,
        model
    )

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks
    }


# ============================================================
# RUN ALL EVALUATION QUESTIONS
# ============================================================

def run_evaluation():

    print("\n" + "=" * 60)
    print("STARTING RAG EVALUATION")
    print("=" * 60)

    # --------------------------------
    # Load evaluation questions
    # --------------------------------

    evaluation_data = []

    with open(
        EVAL_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            if line.strip():

                item = json.loads(line)

                evaluation_data.append(item)

    print(
        f"\nFound {len(evaluation_data)} "
        f"evaluation questions."
    )

    if len(evaluation_data) == 0:

        print("ERROR: eval_v3.jsonl is empty.")

        return

    # --------------------------------
    # Load models once
    # --------------------------------

    vectors, metadata = load_index()

    embedding_model = load_embedding_model()

    tokenizer, model = load_generator()

    # --------------------------------
    # Run evaluation
    # --------------------------------

    with open(
        RESULTS_FILE,
        "w",
        encoding="utf-8"
    ) as output_file:

        for number, item in enumerate(
            evaluation_data,
            start=1
        ):

            # Most eval files use "question".
            # If yours uses "input", this handles it too.
            question = item.get(
                "question",
                item.get("input", item.get("instruction"))
            )

            if not question:

                print(
                    f"\nSkipping item {number}: "
                    "no question field found."
                )

                continue

            print(
                f"\n[{number}/{len(evaluation_data)}]"
            )

            print(
                f"Question: {question}"
            )

            # Run RAG
            result = run_rag(
                question,
                vectors,
                metadata,
                embedding_model,
                tokenizer,
                model
            )

            # --------------------------------
            # Create JSONL record
            # --------------------------------

            output_record = {
                "question": result["question"],
                "answer": result["answer"],
                "retrieved_chunks": result["retrieved_chunks"]
            }

            # Write ONE JSON object per line
            output_file.write(
                json.dumps(
                    output_record,
                    ensure_ascii=False
                ) + "\n"
            )

            # Make sure it is written immediately
            output_file.flush()

            print(
                f"Answer: {result['answer']}"
            )

    print("\n" + "=" * 60)
    print("RAG EVALUATION COMPLETE")
    print("=" * 60)

    print(
        f"\nResults saved to: {RESULTS_FILE}"
    )

    print(
        f"Total questions processed: "
        f"{len(evaluation_data)}"
    )


# ============================================================
# RUN ONE QUESTION
# ============================================================

def run_single_question():

    question = " ".join(sys.argv[1:])

    if not question:

        question = input(
            "Enter your question: "
        )

    vectors, metadata = load_index()

    embedding_model = load_embedding_model()

    tokenizer, model = load_generator()

    result = run_rag(
        question,
        vectors,
        metadata,
        embedding_model,
        tokenizer,
        model
    )

    print("\n" + "=" * 60)

    print("\nQuestion:")
    print(result["question"])

    print("\nRetrieved chunks:")

    for number, chunk in enumerate(
        result["retrieved_chunks"],
        start=1
    ):

        print(
            f"\n--- Chunk {number} ---"
        )

        print(
            f"Score: {chunk['score']:.4f}"
        )

        print(
            f"Source: {chunk['source']}"
        )

        print(
            f"Text: {chunk['text']}"
        )

    print("\nAnswer:")
    print(result["answer"])


# ============================================================
# MAIN
# ============================================================

def main():

    # If a question is provided on the command line,
    # run only that question.
    #
    # Otherwise, run the complete evaluation.
    if len(sys.argv) > 1:

        run_single_question()

    else:

        run_evaluation()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
