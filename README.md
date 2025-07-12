# 📌 Pinterest Semantic Ranking

This project builds an **end-to-end semantic ranking system** that simulates Pinterest’s content discovery engine using NLP. Given a user query like `"boho wedding decor"` or `"kitchen storage hacks"`, the app returns the **top influencer pins** ranked by **semantic similarity**, not just keyword overlap.

Built with Sentence-BERT, CrossEncoder, and Streamlit, this system reimagines how Pinterest-style search can surface more relevant and engaging content.

---

## 🎯 Problem Statement

How do we help users find **relevant**, **engaging**, and **diverse** Pinterest pins based on short natural language queries?

- Traditional keyword search often fails due to vocabulary mismatch or noisy descriptions.
- Pinterest users type vague or aesthetic-heavy queries (e.g., "cozy chic corner") that require **semantic understanding**.
- Our goal: **Rank influencer pins** by relevance, while also considering **popularity (repin count)**.

---

## 🛠️ Tech Stack

| Component               | Description                                              |
|------------------------|----------------------------------------------------------|
| `Sentence-BERT`        | Converts pin text and queries into vector embeddings     |
| `Cosine Similarity`    | Measures semantic closeness between query and pin text   |
| `CrossEncoder (MiniLM)`| Jointly encodes query–pin pairs for deeper reranking     |
| `Streamlit`            | Interactive app UI with sliders and input box            |
| `scikit-learn`         | Score blending and MinMax scaling                        |

---

## 📦 Dataset

**Dataset**: *Top Pinterest Influencers – A Snapshot of Popularity & Engagement*  
**Rows**: 5,000 → 2,428 (after cleaning)  
**Columns**:
- `id`
- `title`
- `description`
- `repin_count`

**Preprocessing**:
- Combined `title` and `description` → `text`
- Dropped missing or very short rows
- Filtered non-English and emoji-only pins
- Converted `repin_count` to integers
- Saved outputs:
  - `cleaned_pins.csv`
  - `embeddings.npy`

---

## 🔍 Ranking Pipeline

### ➤ Stage 1: Sentence-BERT + Cosine Similarity

1. Embed user query and all pin texts
2. Compute cosine similarity
3. Filter out low-relevance pins (threshold slider)
4. Blend semantic similarity and pin popularity using a tunable `α` value:

```python
final_score = α * similarity + (1 - α) * log(repin_count + 1)


### Stage 2: CrossEncoder Reranking (Optional)
Take top 30 candidate pins from Stage 1

Use a pretrained CrossEncoder to rescore each (query, pin) pair jointly

Scale CrossEncoder scores to [0, 1]

Combine with log-repin counts for final score:

python
Copy
Edit
final_score = α * scaled_cross_score + (1 - α) * log1p(repin_count)
📌 You can toggle this reranking in the Streamlit UI.

🧪 Evaluation Summary
We manually tested 20 diverse queries using:

✅ CrossEncoder reranking

⚙️ top_k=5, threshold=0.4, alpha=0.7 (defaults)

⚡ Highlights
Precision@3 ≈ 85%

False positives reduced (e.g., Doja Cat filtered out)

Some queries returned <5 results due to semantic filtering

Top-ranked pins had 2–3× more repins than average

📂 For detailed results → evaluation.md

🎛️ Streamlit App Features
🔎 Text input box

🔢 Top-K slider

🎯 Similarity threshold slider

⚖️ Similarity vs Popularity blending (α)

✅ CrossEncoder reranking toggle

📊 Outputs: Pin Text, Repin Count, Relevance Score, Cross Score

