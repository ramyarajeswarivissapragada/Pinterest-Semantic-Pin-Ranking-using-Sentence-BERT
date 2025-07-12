# 📌 Pinterest Semantic Pin Ranking (with BERT + CrossEncoder)

This project is an end-to-end semantic ranking system that simulates Pinterest's content discovery experience using modern NLP. Given a user query like `"kitchen storage hacks"` or `"boho wedding decor"`, the app returns **top influencer pins ranked by semantic similarity** — not just keyword overlap.

Built using **Sentence-BERT**, **CrossEncoder reranking**, and **Streamlit**, this MVP demonstrates how semantic search can power intelligent recommendation systems using limited metadata.

---

## 📦 Dataset

**Top Pinterest Influencers — A Snapshot of Popularity and Engagement**  
Curated from the top 5 most followed Pinterest accounts (2024 snapshot).  
**5000 pins** with the following fields:

- `id`: unique identifier  
- `title`: pin title (optional)  
- `description`: text content  
- `repin_count`: number of repins (proxy for engagement)

Only **publicly available and ethically mined** content was used.

---

## 🧹 Preprocessing Steps

1. ✅ Drop missing descriptions
2. 🔄 Combine `title` + `description` into unified `text`
3. 🌐 Remove non-English or emoji-only content (`[a-zA-Z]{3,}` regex)
4. 📏 Filter out pins with text length ≤ 10 characters
5. 🔢 Convert and clean `repin_count`

Final dataset size: **2428 influencer pins**

---

## ⚙️ Semantic Search Pipeline

### Stage 1: BERT Embedding + Cosine Similarity

- Use `sentence-transformers/all-MiniLM-L6-v2`
- Encode all pin texts
- At query time:
  - Encode the input query
  - Compute cosine similarity between query and all pins
  - Apply minimum similarity threshold (e.g., `0.40`)
  - Select top-k pins (default `k=5`)
  - Optionally blend cosine similarity with `log(repin_count)` for final ranking:

```python
final_score = α * similarity + (1 - α) * log(1 + repin_count)
````

---

### Stage 2: CrossEncoder Reranking (Optional)

* Take top 30 candidate pins from Stage 1
* Use a pretrained **CrossEncoder** to rescore each `(query, pin)` pair jointly
* Scale CrossEncoder scores to \[0, 1]
* Combine with log-repin counts for final score:

```python
final_score = α * cross_score_scaled + (1 - α) * log(1 + repin_count)
```

This helps reduce keyword traps like:

> ❌ `"cat furniture"` → "Doja Cat Met Gala"

---

## 🧪 Evaluation Summary

We manually tested 20 diverse queries using:

* ✅ CrossEncoder reranking
* ⚙️ `top_k=5`, `threshold=0.4`, `alpha=0.7` (defaults)

### ⚡ Highlights

* **Precision\@3 ≈ 85%**
* **False positives significantly reduced**
* **Some queries returned <5 results due to semantic filtering**
* **Top-ranked pins had 2–3× more repins than average**

📂 For detailed results → [`evaluation.md`](./evaluation.md)

---

## 🎛️ Streamlit App Features

| Feature                     | Description                                             |
| --------------------------- | ------------------------------------------------------- |
| 🔎 Query Input              | Text box for semantic search                            |
| 🔢 Top-K Slider             | Choose how many results to show (3–10)                  |
| 🎯 Similarity Threshold     | Minimum cosine similarity to be considered relevant     |
| ⚖️ Similarity vs Popularity | Blend score using `alpha` slider                        |
| ✅ CrossEncoder Reranking    | Toggle to activate second-stage reranking               |
| 📊 Output Table             | Pin text, repin count, similarity & CrossEncoder scores |

---



---

## ✍️ Author

**Ramya Rajeswari Vissapragada**
MS Business Analytics & AI, UT Dallas
💻 Passionate about NLP, ML, and Responsible AI

---

## 🌐 Future Improvements

* 🔄 Bi-encoder fine-tuning (supervised triplet ranking)
* 🗂️ Query expansion using synonyms or search logs
* 🧠 Personalized reranking using user preferences
* 📊 Advanced evaluation with user-level engagement labels

---

## ⭐ Try It Yourself

```bash
streamlit run app.py
```
