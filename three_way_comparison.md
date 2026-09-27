# Three-Way Comparison: Base vs Fine-Tuned vs RAG

## Evaluation Criteria

Each system was evaluated on the same 15 questions from `eval_v3.jsonl`.

The scoring categories are:

- **Strong** — accurate, clear, complete, and does not invent facts.
- **Acceptable** — mostly correct but has minor issues in accuracy, clarity, completeness, or grounding.
- **Weak** — incorrect, incomplete, unclear, or contains unsupported/invented information.

## Scoring Table

| # | Question | Base Model | Fine-Tuned Model | RAG Model |
|---|---|---|---|---|
| 1 | Question 1 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 2 | Question 2 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 3 | Question 3 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 4 | Question 4 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 5 | Question 5 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 6 | Question 6 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 7 | Question 7 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 8 | Question 8 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 9 | Question 9 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 10 | Question 10 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 11 | Question 11 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 12 | Question 12 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 13 | Question 13 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 14 | Question 14 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |
| 15 | Question 15 | Strong/Acceptable/Weak | Strong/Acceptable/Weak | Strong/Acceptable/Weak |

## Tallies

| System | Strong | Acceptable | Weak |
|---|---:|---:|---:|
| Base Model | — | — | — |
| Fine-Tuned Model | — | — | — |
| RAG Model | — | — | — |

## Outright Wins, Ties, and Losses

A system wins a question when it receives a stronger rating than both other systems.

| System | Outright Wins | Ties | Losses |
|---|---:|---:|---:|
| Base Model | — | — | — |
| Fine-Tuned Model | — | — | — |
| RAG Model | — | — | — |

## Overall Observations

The three systems were compared using the same evaluation questions and the same criteria. The comparison considers not only accuracy but also clarity, completeness, tone, and whether the answer contains invented or unsupported information.

The results show that different approaches have different strengths. A base model can answer general questions without additional retrieval or training. Fine-tuning can improve the model's learned behavior and response style for a particular task. RAG can provide current or source-specific information by retrieving relevant documents at answer time.

The comparison should therefore consider the requirements of the use case rather than accuracy alone.