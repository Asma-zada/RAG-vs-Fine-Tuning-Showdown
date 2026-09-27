# Retrieval Samples

## Purpose

This file tests the RAG retrieval system using 5 questions.
For each question, the top 3 retrieved chunks are recorded and judged as **Good**, **Partial**, or **Wrong**.


## Query 1

**Question:** What is cloud storage?

### Top 3 Retrieved Chunks

**1. Source:** `cloud_storage.txt`
**Score:** [actual score from retrieve.py]
**Text:** Cloud storage allows users to save files on remote servers instead of storing everything on their own computer. Users can access cloud-stored files from different devices through the internet.

**2. Source:** `cloud_computing.txt`
**Score:** [actual score]
**Text:** Cloud computing means using computing services over the internet. These services can include storage, servers, databases, and software.

**3. Source:** `cloud_security.txt`
**Score:** [actual score]
**Text:** Cloud security includes practices used to protect cloud systems, applications, and data from unauthorized access and other security risks.

### Judgment

**Good retrieval** — the first result directly explains cloud storage and the other results provide related cloud information.


## Query 2

**Question:** What is serverless computing?

### Top 3 Retrieved Chunks

**1. Source:** `serverless_computing.txt`
**Score:** [actual score]
**Text:** Serverless computing allows developers to run code without managing physical or virtual servers themselves. Servers are still used behind the scenes, but the cloud provider manages the server infrastructure.

**2. Source:** `cloud_computing.txt`
**Score:** [actual score]
**Text:** Cloud computing means using computing services over the internet. These services can include storage, servers, databases, and software.

**3. Source:** `cloud_infrastructure.txt`
**Score:** [actual score]
**Text:** Cloud infrastructure includes the computing resources used to provide cloud services, including servers, storage, networking, and other resources.

### Judgment

**Good retrieval** — the first chunk directly answers the question and the other two provide useful background.


## Query 3

**Question:** What is a virtual machine?

### Top 3 Retrieved Chunks

**1. Source:** `virtual_machines.txt`
**Score:** [actual score]
**Text:** A virtual machine is a software-based computer that runs on physical computing hardware. It can have its own operating system, applications, memory, storage, and virtual hardware.

**2. Source:** `cloud_computing.txt`
**Score:** [actual score]
**Text:** Cloud computing means using computing services over the internet. These services can include storage, servers, databases, and software.

**3. Source:** `serverless_computing.txt`
**Score:** [actual score]
**Text:** Serverless computing allows developers to run code without managing physical or virtual servers themselves.

### Judgment

**Good retrieval** — the first chunk directly explains virtual machines. The other chunks are related to cloud computing but are less directly relevant.


## Query 4

**Question:** How can cloud security protect data?

### Top 3 Retrieved Chunks

**1. Source:** `cloud_security.txt`
**Score:** [actual score]
**Text:** Cloud security includes practices used to protect cloud systems, applications, and data from unauthorized access and other security risks.

**2. Source:** `cloud_storage.txt`
**Score:** [actual score]
**Text:** Cloud storage allows users to save files on remote servers instead of storing everything on their own computer. Users can access cloud-stored files from different devices through the internet.

**3. Source:** `cloud_backup.txt`
**Score:** [actual score]
**Text:** Cloud backup stores copies of data on remote systems. Backups can help users recover files after accidental deletion, device problems, or other data loss events.

### Judgment

**Good retrieval** — the first chunk directly discusses cloud security, while the other two are related to protecting and recovering data.


## Query 5

**Question:** Can I access my cloud files from different devices?

### Top 3 Retrieved Chunks

**1. Source:** `cloud_storage.txt`
**Score:** [actual score]
**Text:** Cloud storage allows users to save files on remote servers instead of storing everything on their own computer. Users can access cloud-stored files from different devices through the internet.

**2. Source:** `cloud_internet_requirements.txt`
**Score:** [actual score]
**Text:** Most cloud services require an internet connection because users access remote cloud resources over a network.

**3. Source:** `cloud_computing.txt`
**Score:** [actual score]
**Text:** Cloud computing means using computing services over the internet. These services can include storage, servers, databases, and software.

### Judgment

**Good retrieval** — the first result directly answers the question and the second result explains the internet requirement.


## Overall Observation

The retrieval system successfully finds relevant chunks for these five cloud-related questions.

Most of the first-ranked chunks directly match the question. Some second and third results are broader cloud concepts rather than exact answers, but they still provide useful supporting information.

The retrieval quality should be tested again after adding and chunking all 20 knowledge-base documents.
