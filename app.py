import streamlit as st
import pandas as pd
import numpy as np
import re
from sentence_transformers import SentenceTransformer, CrossEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Load models
model = SentenceTransformer('all-MiniLM-L6-v2')
cross_reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Load data
df = pd.read_csv('cleaned_pins.csv')
embeddings = np.load('embeddings.npy', allow_pickle=True)

def search_pins(query, top_k=5, min_similarity=0.35, alpha=0.7):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    sorted_indices = similarities.argsort()[::-1]
    filtered_indices = [i for i in sorted_indices if similarities[i] >= min_similarity]
    top_indices = filtered_indices[:max(top_k * 2, 10)]

    results = df.iloc[top_indices][['text', 'repin_count']].copy()
    results['similarity'] = similarities[top_indices]
    results['repin_score'] = np.log1p(results['repin_count'])
    results['final_score'] = alpha * results['similarity'] + (1 - alpha) * results['repin_score']

    return results.sort_values('final_score', ascending=False).head(top_k).reset_index(drop=True)

def rerank_with_crossencoder(query, bert_results, top_k=5, alpha=0.7):
    filtered = bert_results[
        (bert_results['repin_count'] > 0) &
        (bert_results['text'].str.len() > 30) &
        (bert_results['text'].str.contains(r'[a-zA-Z]{3,}', regex=True))
    ]
    texts = filtered['text'].tolist()

    if not texts:
        return pd.DataFrame(columns=['text', 'repin_count', 'cross_score', 'final_score'])

    pairs = [[query, text] for text in texts]
    scores = cross_reranker.predict(pairs)

    reranked = pd.DataFrame({'text': texts, 'cross_score': scores})
    final = reranked.merge(filtered[['text', 'repin_count']], on='text', how='left')
    final = final.drop_duplicates(subset='text')  # ✅ REMOVE duplicates


    final['cross_score_scaled'] = MinMaxScaler().fit_transform(final[['cross_score']])
    final['log_repins'] = np.log1p(final['repin_count'])
    final['final_score'] = alpha * final['cross_score_scaled'] + (1 - alpha) * final['log_repins']

    return final.sort_values('final_score', ascending=False).head(top_k).reset_index(drop=True)

st.set_page_config(page_title="Pinterest Semantic Ranking", layout="centered")

st.title("🔍 Pinterest Pin Ranking Demo")
st.subheader("Semantic Search using BERT on Influencer Pins")
st.markdown("Type a Pinterest-style query (e.g., *'boho wedding decor'* or *'cat furniture'*) and explore ranked results based on meaning — not just keywords!")

use_crossencoder = st.checkbox("Use CrossEncoder reranking")
query = st.text_input("Enter a search query:", value="cozy bedroom ideas")

col1, col2 = st.columns(2)
with col1:
    top_k = st.slider("How many results to show?", min_value=3, max_value=10, value=5)
with col2:
    threshold = st.slider("Minimum similarity threshold", min_value=0.3, max_value=0.7, value=0.4)

alpha = st.slider("Similarity vs Popularity (α)", min_value=0.0, max_value=1.0, value=0.7, step=0.05)

if st.button("Search Pins"):
    if not re.search(r'[a-zA-Z]{3,}', query):
        st.warning("Please enter a meaningful query (e.g. 'cozy bedroom ideas').")
    else:
        bert_results = search_pins(query, top_k=30, min_similarity=threshold, alpha=alpha)

        if use_crossencoder:
            results = rerank_with_crossencoder(query, bert_results, top_k=top_k, alpha=alpha)
        else:
            results = bert_results.head(top_k)

        if results.empty:
            st.warning("No relevant pins found.")
        else:
            st.dataframe(results.rename(columns={
                'text': 'Pin Text',
                'repin_count': 'Repin Count',
                'similarity': 'Relevance Score',
                'cross_score': 'CrossEncoder Score',
                'final_score': 'Final Score'
            }).style.format({
                "Relevance Score": "{:.2f}",
                "CrossEncoder Score": "{:.2f}",
                "Final Score": "{:.2f}"
            }))

st.markdown("---")
st.caption("👩‍💻 Built by Ramya Rajeswari Vissapragada | Powered by Sentence-BERT · Streamlit")