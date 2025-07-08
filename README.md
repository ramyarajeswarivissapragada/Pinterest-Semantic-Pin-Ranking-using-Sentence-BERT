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

We manually annotated 20 search queries to assess real-world performance. The model achieved strong precision on stylistic and decor-related queries, with a few expected failures due to keyword ambiguity.

- **Precision@1:** 80%  
- **Precision@3:** ~85–90%  
- **Common failures:** Keyword traps (e.g. "Doja Cat" for "cat furniture")  
- **Repin count insight:** Relevant results tend to have higher engagement

📄 See [evaluation.md](./evaluation.md) for full query results and analysis

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
