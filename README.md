# Atomic Unit Relevance Assessment (AURA) Framework
### Automated Legal e-Discovery Optimization using LLMs & Combinatorial Search

![Status](https://img.shields.io/badge/Status-Completed-success) ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![GenAI](https://img.shields.io/badge/GenAI-Google%20Gemini-orange)

**Tech Stack:** Python, Google Gemini (GenAI), NetworkX, SentenceTransformers, Scikit-Learn
**Dataset:** NIST TREC (Legal Track) - ~4,500 Documents

---

## 1. The Problem
Legal e-Discovery is computationally expensive and error-prone.
*   **Keyword Search (Ctrl+F):** Results in high False Positives (low precision) because it relies on exact string matching.
*   **Standard TF-IDF:** Misses semantic context (e.g., failing to link "power outage" with "blackout").
*   **The Goal:** Attorneys need a way to retrieve relevant documents based on *thematic concepts* ("Atomic Units"), not just keywords.

## 2. The Solution
I architected the **AURA Framework**, a hybrid NLP pipeline that automates the relevance feedback loop:
1.  **Extracts** high-level semantic themes ("Atomic Units") using **Generative AI (Google Gemini)**.
2.  **Propagates** relevance to documents using **Semantic Vector Search**.
3.  **Optimizes** the query using a **$2^n$ Exhaustive Search** algorithm against ground-truth data to filter out hallucinations.

## 3. Architecture & Methodology
The framework moves beyond simple Boolean search by implementing a **Vector-Based Relevance Propagation** engine.

### The "Invisible Link": Cosine Similarity Ranking
Unlike Boolean search (which is binary), this pipeline creates a continuous relevance ranking for every document:
1.  **Vectorization:** Extracted "Atomic Units" and raw documents are encoded into 384-dimensional vectors using `all-MiniLM-L6-v2`.
2.  **Scoring:** The system computes the **Cosine Similarity** between specific Atomic Units and every document in the corpus.
3.  **Ranking:** This generates a leaderboard where documents with high semantic overlap float to the top. When a theme is selected, the system propagates that signal to retrieve the top-ranked documents, bridging the vocabulary gap between legal concepts and raw evidence.

### Optimization Engine (The "Attorney Simulator")
To validate this ranking, the pipeline executes a **Combinatorial Optimization ($2^n$)**:
*   It tests every possible boolean combination of the extracted themes.
*   It utilizes NIST Ground Truth (QRELs) to simulate "Ideal User Feedback" (Supervised Learning).
*   It identifies the precise threshold on the relevance leaderboard that maximizes the **F1 Score**, effectively filtering out "hallucinated" themes that do not correlate with relevant documents.

## 4. Key Results
The pipeline was benchmarked against ~4,500 legal documents in a full factorial experiment (3 Extraction Methods x 2 Propagation Methods).

| Metric | TF-IDF Baseline | AURA (Generative LLM) | Improvement |
| :--- | :--- | :--- | :--- |
| **F1 Score** | 0.634 | **0.763** | **+20.3%** |

*   **Operational Impact:** With a **Precision of 74%**, the system allows attorneys to identify the majority of relevant evidence while reviewing **~50% less document volume** than a linear review.
*   **Winner:** The **Pure LLM extraction** outperformed a Hybrid (TextRank + LLM) approach (0.657 F1). This proves that preserving specific entities (dates, names, dollar amounts) found in raw text is critical for high-precision retrieval, whereas graph-based summarization often smooths over these vital details.

## 5. Technical Highlights

### A. High-Information Density Sampling
To handle large document chunks (500+ docs) without exploding API costs, the pipeline sorts documents by information density (length) and processes the top 15 "heavy hitter" documents to extract global themes. This ensures coverage of dominant threads (email chains, memos) while filtering transactional noise.

### B. Self-Healing Infrastructure
The pipeline is built for production reliability:
*   **Dynamic Model Selection:** Automatically falls back to lightweight models (Gemini Flash) if latency increases or rate limits are hit.
*   **Exponential Backoff:** Handles API timeouts gracefully without crashing the pipeline.

### C. Domain Shift Analysis
While the model achieved 0.76 F1 on the training matter (Financial Fraud), performance dropped on hold-out matters (Energy Regulation). This validates the need for **Few-Shot Tuning** in production deployment, as legal relevance is highly domain-specific and does not transfer Zero-Shot.

## 6. How to Run
1.  **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/aura-legal-framework.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment:**
    Rename `.env.example` to `.env` and add your Google API Key:
    ```
    GOOGLE_API_KEY=your_key_here
    ```
4.  **Run the notebook:**
    ```bash
    jupyter notebook aura_pipeline.ipynb
    ```

---
*Note on Data: This repository contains the code logic and sample files. The full NIST TREC dataset is proprietary. The pipeline includes automatic checks to skip execution if full data is not present.*
