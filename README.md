# 📌 Pinterest Semantic Ranking App

This project simulates Pinterest’s content discovery experience using a semantic ranking system powered by Sentence-BERT and CrossEncoder models. Given a query like `"boho wedding decor"` or `"cat furniture"`, the system returns top influencer pins ranked by meaning—not just keyword overlap.

## 🔍 Project Overview

Millions of users rely on Pinterest to discover ideas. This project builds an intelligent search system that mimics how Pinterest might semantically rank influencer content based on:
- User query relevance
- Content popularity (repins)
- Meaning—not just text matching

The final app is built with **Streamlit** and supports real-time interactive search.

---

## ⚙️ Features

| Component                | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 🧹 Text Preprocessing     | Cleans and combines title + description, filters short/emoji/non-English rows |
| 🤖 Sentence-BERT Encoder | Generates vector embeddings for all pins using `all-MiniLM-L6-v2`           |
| 🔁 CrossEncoder Reranker | Re-ranks top pins using `cross-encoder/ms-marco-MiniLM-L-6-v2`              |
| ⚖️ Alpha Blending        | Balances relevance vs. popularity using repin count log-scaling             |
| 🎛 Interactive App       | Query input, top-K slider, similarity threshold, and reranker toggle        |
| 📊 Evaluation            | Manual annotation of 20 real-world queries with precision@3 and insights   |

---

## 🖥️ Streamlit App Demo

### Inputs:
- 🔎 Query input (e.g., `"fall home decor"`)
- 🎯 Minimum similarity threshold
- 🎚 Top-K results to show
- ⚖️ Alpha slider: blend semantic vs. repin score
- ✅ Toggle: use CrossEncoder for reranking

### Outputs:
- Table with:
  - Pin text
  - Repin count
  - Relevance score (BiEncoder / CrossEncoder)
  - Final score (blended)

---

## 📁 Project Files

| File                  | Purpose                                      |
|-----------------------|----------------------------------------------|
| `app.py`              | Streamlit frontend with full functionality   |
| `notebook.ipynb`      | Jupyter notebook for preprocessing and testing |
| `cleaned_pins.csv`    | Final dataset after cleaning                 |
| `embeddings.npy`      | Sentence-BERT embeddings                     |
| `evaluation.md`       | Manual evaluation for 20 real-world queries  |

---

## 📊 Evaluation

We manually annotated 20 diverse queries to evaluate real-world performance.

| Query                  | Top Result                       | Relevant? | Notes                                 |
|------------------------|----------------------------------|-----------|----------------------------------------|
| `cat furniture`        | Cozy Buddy Bed                   | ✅        | On-theme but not exact                 |
| `cat furniture`        | Doja Cat Met Gala                | ❌        | False positive (keyword trap)         |
| `wedding table decor`  | Boho centerpiece                 | ✅        | Strong contextual relevance           |
| `pantry hacks`         | IKEA kitchen storage             | ✅        | Highly relevant and practical         |
| `shelf styling`        | Urban Outfitters bookshelf pin   | ✅        | Visual and semantic match             |

> **Precision@3 across 20 queries**: ~85%  
> **Top-5 results had ~3× higher repin count than random pins**, suggesting relevance aligns with engagement.

See full breakdown in [`evaluation.md`](evaluation.md).

---

## 🚀 Run Locally

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
