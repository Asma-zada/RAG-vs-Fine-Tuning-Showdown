# RAG vs Fine-Tuning Notes

## 1. RAG vs Fine-Tuning

### RAG

RAG (Retrieval-Augmented Generation) gives the AI relevant information from documents before it generates an answer. It is useful when the AI needs specific factual information from a knowledge base.

For example, if I have cloud-computing documentation, RAG can retrieve information about cloud storage and give that information to the model before it answers the user.

### Fine-Tuning

Fine-tuning trains a model using examples so that it learns a particular task, behavior, format, or style.

For example, I could fine-tune a model to explain cloud concepts in very simple language and follow a specific answer format.

### Simple Difference

* **RAG:** Gives the model relevant knowledge or information.
* **Fine-tuning:** Teaches the model a particular behavior, task, format, or style.
* **Prompting:** Gives the model instructions when asking a question.

---

## 2. My 10 Use-Case Questions

My Week 1 use case is a **cloud explainer assistant**. I classified the questions based on whether they mainly require factual knowledge or a particular behavior/style.

| #  | Question                                              | Type      | Reason                                                                                            |
------------------------------------------------------------------------------------------------- |
| 1  | What is the difference between cloud and my computer? | Knowledge | The answer requires factual information about local computers and cloud computing.                |
| 2  | What is serverless computing in simple words?         | Knowledge | The question asks for information about the concept of serverless computing.                      |
| 3  | What is cloud storage?                                | Knowledge | The answer requires factual information about how cloud storage works.                            |
| 4  | Can I lose data in the cloud?                         | Knowledge | This requires information about cloud data storage, backups, and data loss.                       |
| 5  | Do I need to install software for cloud?              | Knowledge | The question asks for factual information about accessing cloud services.                         |
| 6  | What is a virtual machine in simple words?            | Knowledge | The answer requires factual information about virtual machines.                                   |
| 7  | Is the cloud faster than my computer?                 | Knowledge | The answer depends on factual information about computing power and different types of workloads. |
| 8  | Can I use the cloud for free? What are limits?        | Knowledge | This requires factual information about cloud free tiers, storage, and usage limits.              |
| 9  | What if my internet goes down?                        | Knowledge | The answer requires factual information about internet connectivity and access to cloud services. |
| 10 | Who owns my data in the cloud?                        | Knowledge | This requires factual information about cloud data ownership and provider policies.               |

### Observation

All 10 questions are mainly **knowledge questions**. They ask about facts, concepts, or information related to cloud computing.

Some questions contain wording such as **"in simple words"**, but the main purpose is still to get factual knowledge. The phrase "in simple words" describes the desired response style, but it does not make the question primarily a behavior question.

This means RAG is a good fit for these questions because the answers can be based on reliable cloud documentation.

Fine-tuning could still be useful if I wanted the assistant to consistently explain these facts in a particular style, such as using very simple English, short answers, or a fixed format.


## 3. Five Reasons RAG Can Still Give a Wrong Answer

### 1. The correct chunk is not retrieved

The knowledge base might contain the correct information, but the retrieval system may fail to find the relevant chunk. The model then does not receive the information it needs.

### 2. An irrelevant chunk is retrieved

The system might retrieve a document that looks similar to the question but does not actually contain the correct answer. The model may use this irrelevant information and produce a wrong answer.

### 3. The information is outdated

RAG uses the information stored in its knowledge base. If the source document is old, the model may give an outdated answer.

For example, cloud providers can change their free-tier limits. If my knowledge base contains an old limit, RAG may return the old information.

### 4. Different documents contradict each other

Two documents in the knowledge base might contain different information. If both are retrieved, the model may become confused about which information is correct.

### 5. Too much context is retrieved

If the system retrieves too many large chunks, the prompt can contain unnecessary information. This can make it harder for the model to focus on the information relevant to the user's question.


## 4. What I Learned

RAG and fine-tuning solve different problems.

RAG is useful when an assistant needs access to specific factual information from documents. Fine-tuning is useful when I want the model to learn a particular task, behavior, format, or style.

For my cloud explainer assistant, RAG can provide reliable cloud-computing information from a knowledge base. Fine-tuning can help the model consistently explain that information in the style I want.

RAG can still fail if the wrong information is retrieved, the correct information is missing, the documents are outdated, documents contradict each other, or too much irrelevant context is provided.

Therefore, building a RAG system is not only about retrieving information. I also need to check whether the retrieved information is actually relevant and correct.
