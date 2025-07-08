# 🔍 Pinterest Semantic Pin Ranking using Sentence-BERT

This project is an end-to-end semantic ranking system that simulates Pinterest's content discovery experience using NLP. Given a user query like `"kitchen storage hacks"` or `"boho wedding decor"`, the app returns top influencer pins ranked by **semantic similarity** — not just keyword overlap.

<p align="center">
  <img src="screenshot.png" width="700"/>
</p>

---

## 🧠 Problem Statement

Pinterest is a visual discovery engine — but search still depends on matching user intent with content across a massive catalog of pins. We aim to replicate **Pinterest-style semantic search** using real influencer pins and a modern NLP embedding pipeline.

---

## 📦 Dataset

**Top Pinterest Influencers – A Snapshot of Popularity and Engagement**  
- 5,000 pins from top-followed Pinterest accounts  
- Columns: `id`, `title`, `description`, `repin_count`  
- Cleaned to ~2,400 usable examples with rich English text

---

## 🛠️ Tech Stack

| Component | Tools Used |
|----------|------------|
| Embeddings | `Sentence-BERT (all-MiniLM-L6-v2)` |
| Similarity | Cosine similarity using `sklearn` |
| Preprocessing | Emoji filtering, short-text drop, non-English filtering |
| UI | Streamlit |
| Evaluation | Manual annotation + engagement alignment (repin count) |

---

## ⚙️ How It Works

1. Pins are embedded using **Sentence-BERT**
2. User enters a free-text search query
3. We compute cosine similarity with all pin embeddings
4. Top-K results are returned based on similarity and minimum threshold
5. (Optional) Repin count can be used for secondary ranking or insights

---

## 🧪 Evaluation

We manually annotated 20 diverse queries to evaluate real-world performance.

| Query | Top Result | Relevant? | Notes |
|-------|------------|-----------|-------|
| "cat furniture" | Cozy Shoppe Buddy Bed | ✅ | On-theme but not exact |
| "wedding table decor" | Boho table centerpiece | ✅ | High visual & contextual relevance |
| "pantry hacks" | IKEA hack kitchen | ✅ | Matches intent |
| "cat furniture" | Doja Cat Met Gala | ❌ | False positive (keyword trap) |
| "modern workspace" | IKEA desk setup | ✅ | Strong match |

> **Precision@3 across 20 queries**: ~85%  
> **Top-5 results had ~3× higher repin count than random pins**, suggesting relevance aligns with engagement.

---

## 🚀 Demo App

The app is powered by Streamlit with:
- Query input box
- Top-K slider
- Similarity threshold control
- Output table with pin text, repin count, and similarity score

<p align="center">
  <img src="app_ui.png" width="700"/>
</p>

To run locally:

```bash
streamlit run app.py
