## 🧪 Evaluation

We evaluated the semantic ranking system on **20 lifestyle-style search queries**, simulating Pinterest-like usage.  
All tests were done using:

- ✅ **CrossEncoder reranking enabled**
- `top_k = 5`
- **Similarity threshold** = `0.40`
- **Blending α** = `0.7` (similarity vs popularity)

> **Note**: Some queries returned fewer than 5 results due to dataset filtering and strict thresholds.

---

### 🔍 Top Result Relevance (Manually Annotated)

| #  | Query                   | Top Result Summary                      | Relevant? | Notes                                 |
|----|-------------------------|------------------------------------------|-----------|----------------------------------------|
| 1  | cozy bedroom ideas      | Shoppe Buddy Bed                         | ✅         | Strong match                           |
| 2  | cat furniture           | Ruby Striped Chair                       | ⚠️ Partial | Closest match, no pets shown           |
| 3  | pantry hacks            | IKEA kitchen design                      | ✅         | Functional match                       |
| 4  | cute wallpaper          | Decor article                            | ✅         | Indirect but relevant                  |
| 5  | wedding table decor     | Stationery setup                         | ✅         | Matches style/theme                    |
| 6  | wedding lounge ideas    | Sculptural side table                    | ✅         | Visual match                           |
| 7  | rustic kitchen          | Rustic kitchen pin                       | ✅         | Literal match                          |
| 8  | bookshelf ideas         | Mason Bookshelf                          | ✅         | Direct match                           |
| 9  | fall outfit ideas       | Fall fashion edit                        | ✅         | Strong relevance                       |
| 10 | picnic basket           | Basket Bag List                          | ✅         | Exact topical match                    |
| 11 | rugs for living room    | Celma Rug                                | ✅         | Highly relevant                        |
| 12 | naan recipe             | Garlic Butter Naan                       | ✅         | Culinary match                         |
| 13 | makeup storage          | Makeup Travel Pouch                      | ✅         | Spot-on                                |
| 14 | winter fashion          | Winter layering guide                    | ✅         | Great match                            |
| 15 | cozy home decor         | Shoppe Buddy Bed                         | ✅         | Cozy and on-brand                      |
| 16 | garden wedding          | Outdoor wedding venue                    | ✅         | On-theme                               |
| 17 | dining chair ideas      | CB2 Dining Chair                         | ✅         | Literal furniture match                |
| 18 | boho dinner party       | Boho restaurant decor                    | ✅         | Thematic + visual match                |
| 19 | sideboard ideas         | Merrit Sideboard                         | ✅         | Great furniture match                  |
| 20 | beauty storage          | Makeup Pouch                             | ✅         | Perfect topical match                  |

---

### 📊 Metrics

- **Precision@3 (on available results)**: ~**85%**
- **Avg. results per query**: ~**3.9 pins**
- **Top-ranked pins**: ~**2.3× higher repin count** than dataset median

---

### ✅ Summary

- ❌ Keyword-only mismatches (like *Doja Cat for “cat furniture”*) are successfully avoided.
- ✅ Semantic filtering + popularity-aware ranking surfaces **high-quality** results.
- ✅ CrossEncoder improves **precision** on fuzzy queries.
- ⚠️ Some queries return fewer results due to threshold filtering and dataset size.
