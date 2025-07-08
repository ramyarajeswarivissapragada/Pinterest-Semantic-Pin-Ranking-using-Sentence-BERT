# 🧪 Evaluation: Pinterest Semantic Ranking (Manual Annotations)

We evaluated 20 real user-style queries using the deployed semantic search system. The results below reflect the top-ranked pin returned for each query, judged manually for relevance to the query’s intent.

---

| Query | Top Result (Short Summary) | Relevant? | Notes |
|-------|-----------------------------|-----------|-------|
| cozy home ideas | Cozy blankets, fall decor, quilts | ✅ | Strong theme alignment |
| cat furniture | Velvet sofa / Doja Cat mention | ❌ | False positive, keyword trap |
| pantry hacks | IKEA kitchen hack by Norm Architects | ✅ | Practical & thematic |
| teen room decor | "Black decor", eclectic styles | 🟡 | Somewhat ambiguous |
| dorm setup | Guest bedroom, Cozy corner bed | ✅ | Close functional match |
| wedding table decor | Floral centerpiece with name cards | ✅ | Excellent visual & intent alignment |
| rustic lighting | Rustic kitchen in warm colors | ✅ | Good aesthetic match |
| bookshelf design | How to Style Shelves + Urban Outfitters shelf | ✅ | Direct content match |
| fall outfit ideas | Fall dresses, layering tips | ✅ | Strong seasonal fit |
| summer picnic | Basket bags, summer wearables | ✅ | Thematic and visual match |
| indoor plant styling | No relevant pins | ❌ | Sparse recall for niche query |
| breakfast nook | "Our Breakfast Nook" pin | ✅ | Spot-on result |
| makeup storage | Makeup pouch, drawer organizers | ✅ | Matches function + keyword |
| winter fashion | Layering, knitwear, ski style | ✅ | Very relevant |
| cozy decor | Cozy Shoppe corners, blankets | ✅ | Perfect match |
| wedding inspiration | Summer wedding with black-white theme | ✅ | Excellent photo and theme fit |
| pet furniture | Chair, Buddy Bed, but not pet-specific | 🟡 | Semantically adjacent but unclear |
| boho kitchen | Rustic kitchen in warm colors | ✅ | Style and decor fit |
| bedroom moodboard | Guest bedroom, moodboard vibes | ✅ | Relevant and clean layout |
| floral makeup | Makeup pouch, flower eyeshadow | ✅ | Slightly generic but acceptable |

---

### 📊 Summary

- **Relevant (✅):** 16 / 20  
- **Partial relevance (🟡):** 2  
- **Not relevant (❌):** 2  
- **Precision@1:** 80%  
- **Precision@3:** Estimated ~85–90% based on broader hits  
- **Failure Cases:** Mostly keyword confusion (e.g. “Doja Cat”), sparse dataset coverage

---

### 🧠 Observations

- Model handles stylistic queries (e.g. "cozy home", "boho kitchen") very well  
- Occasional false positives arise from surface keyword overlap  
- Most top pins had above-average repin counts, aligning with engagement trends  
- Improving niche recall could benefit from query expansion or reranking

---

### 🧪 Evaluation Settings

- top_k = 5  
- min_similarity = 0.40  
- Source: Streamlit App (`app.py`)  
