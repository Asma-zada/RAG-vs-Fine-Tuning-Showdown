# RAG vs Fine-Tuning Showdown

## Project Information

**Student:** Your Name
**Course:** Generative AI / LLM Engineering
**Week:** 8
**Project Title:** RAG vs Fine-Tuning Showdown


# Use Case

The use case for this project is a **Cloud Explainer Assistant**.

The assistant answers beginner-friendly questions about cloud computing topics such as:

* What is cloud computing?
* What is a virtual machine?
* What is serverless computing?
* What is cloud storage?
* How is cloud computing different from a personal computer?

The goal is to provide simple, accurate explanations using either:

1. A base language model
2. A fine-tuned model
3. A Retrieval-Augmented Generation (RAG) system


# What is RAG?

Retrieval-Augmented Generation (RAG) is a method that combines:

* Information retrieval
* Language generation

Instead of answering only from model memory, a RAG system first searches a knowledge base and retrieves relevant information.

The complete RAG pipeline used in this project is:


Source Documents
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector Search
        ↓
Top-K Retrieval
        ↓
Grounded Prompt
        ↓
Answer Generation


This approach helps reduce hallucinations because the model answers using retrieved information instead of relying only on learned parameters.


# Project Components

## Knowledge Base

A small cloud-computing knowledge base was created using text documents.

Examples include:

* Cloud basics
* Cloud storage
* Virtual machines
* Serverless computing
* Backups
* Security
* Public, private, and hybrid cloud


## Chunking

The source documents were divided into fixed-size chunks.

* Chunk size: 200 words
* Output file: `chunks.jsonl`

Fixed-size chunking was selected because:

* It is simple
* It keeps enough context
* It works well for a small dataset

The chunking script reads text files from:

```text
knowledge_base/
```

and creates:

```text
chunks.jsonl
```


## Embeddings

The project uses:

```text
all-MiniLM-L6-v2
```

from Sentence Transformers to convert text chunks into embeddings.

Embeddings are stored as:

```text
vectors.npy
vector_metadata.json
```


## Retrieval

Cosine similarity is used to retrieve the most relevant chunks.

Top retrieved chunks:

```text
TOP_K = 3
```

The retrieval system uses NumPy vector operations for similarity search.


## Generator Model

This project uses:

### Base Model

```text
google/flan-t5-small
```

### Fine-Tuning

LoRA adapters were applied to create a specialized model.


# Systems Compared

Three systems were evaluated:

## 1. Base Model

* Uses only pretrained knowledge
* No retrieval
* No domain specialization


## 2. Fine-Tuned Model

* Learns task behavior
* Produces more consistent answers
* Knowledge updates require retraining


## 3. RAG + Fine-Tuned Model

Pipeline:

```
Question
   ↓
Retrieve Chunks
   ↓
Build Prompt
   ↓
Fine-Tuned Generator
   ↓
Answer
```

This system combines:

* Fine-tuning → behavior
* RAG → external knowledge


# Evaluation

All systems were tested using:

```text
eval_v3.jsonl
```

The same evaluation questions were used for:

* Base Model
* Fine-Tuned Model
* RAG Model

Evaluation criteria:

* Accuracy
* Clarity
* Completeness
* Grounding
* No invented facts


# Headline Result

The experiment showed that:

* Base models perform reasonably on common questions.
* Fine-tuning improves consistency and response style.
* RAG improves factual grounding when relevant information is retrieved.
* The strongest approach is often a combination of RAG and fine-tuning.

No single method is always best.

The correct choice depends on:

* Whether knowledge changes often
* Whether behavior customization is required
* Whether both are needed


# Lessons Learned

Important findings:

1. Retrieval quality matters.
2. Good chunking improves results.
3. Wrong retrieval causes wrong answers.
4. Fine-tuning changes behavior more than knowledge.
5. RAG helps with changing information.
6. Combining both approaches is often practical.


# Future Improvements

Possible future work:

* Larger knowledge base
* Better chunking methods
* FAISS vector search
* Re-ranking retrieved documents
* Better grounding prompts
* Larger generator models
* Fine-tuning specifically for retrieved context


# Project Structure

```text
week8_project/
├── README.md
├── rag_vs_finetune_notes.md
├── knowledge_base/
├── chunks.jsonl
├── chunk_documents.py
├── build_index.py
├── retrieve.py
├── retrieval_samples.md
├── rag_pipeline.py
├── rag_eval_results.jsonl
├── retrieval_impact_notes.md
├── three_way_comparison.md
└── decision_framework.md
```


# Conclusion

This project demonstrated that RAG and fine-tuning solve different problems.

* Fine-tuning teaches behavior.
* RAG provides external knowledge.

Real-world AI systems often combine both techniques to produce accurate, useful, and up-to-date responses.
