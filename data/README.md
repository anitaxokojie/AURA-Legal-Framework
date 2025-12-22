# Dataset Information: NIST TREC 2011 Legal Track

** Note:** This repository contains a **small sample subset** of the dataset for demonstration purposes.

## Background
The full dataset used for this project comes from the **NIST TREC 2011 Legal Track (Learning Task)**, which uses the **Enron Email Corpus** (EDRM Version 2). It is an industry-standard benchmark for evaluating Information Retrieval (IR) and e-Discovery systems.
The corpus consists of ~685,000 emails seized by the **Federal Energy Regulatory Commission (FERC)** during the investigation into the **Enron scandal**.

The pipeline simulates a response to three distinct production requests (Topics), representing diverse legal scenarios:

*   **Topic 401 (EnronOnline):**
    *   *Context:* EnronOnline was the first web-based transaction system for commodities, which allowed Enron to manipulate energy markets.
    *   *Discovery Goal:* Find all documents related to the **design, development, and operation** of this platform, specifically regarding the trading of financial derivatives and commodities.

*   **Topic 402 (Derivatives Legality):**
    *   *Context:* A major part of the Enron scandal involved complex financial instruments used to hide debt.
    *   *Discovery Goal:* Identify communications discussing whether specific **over-the-counter (OTC) derivatives** or financial products were compliant with domestic or foreign regulations (e.g., "gaming" the system vs. legal hedging).

*   **Topic 403 (Environmental Compliance):**
    *   *Context:* Corporate malfeasance often extends beyond finance to operational negligence.
    *   *Discovery Goal:* Uncover documents related to **environmental impact**, specifically attempts to influence, avoid, or circumvent environmental rules regarding emissions, spills, or pollution.


## Data Access & Reproduction
The full corpus contains ~685,000 documents (approx. 100GB raw). Due to GitHub file size limits and data usage terms, the full dataset is not included in this repository.

To reproduce the full results (F1 Score: 0.763), you must acquire the original data sources:

1.  **The Corpus (Documents):** 
    *   Download the **EDRM Enron Email Data Set v2** (XML or PST format) from the [EDRM Website](https://edrm.net/resources/data-sets/edrm-enron-email-data-set/).
    *   *Note: This pipeline expects the extracted text format.*

2.  **The Ground Truth (QRELs & Topics):**
    *   Download the **2011 Learning Task Relevance Judgments** (`qrels.t11legallearn`) from the [NIST TREC Legal Track Data Archive](https://trec.nist.gov/data/legal11.html).
    *   Place the `.qrel` files into the `relevance_judgments/` folder.

## Sample Data
The files currently in the `docs/` folder are **anonymized samples** selected to demonstrate the pipeline's functionality without requiring the full corpus download.
