import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load datasets
df_collected = pd.read_csv("response1_remaining.csv")  # 78 rows
df_ground = pd.read_csv("groundtruth1.csv")           # 20 rows

# User-defined thresholds
thresholds = np.arange(0, 1.05, 0.05)

# --- Step 1: TF-IDF vectorization ---
vectorizer = TfidfVectorizer(stop_words='english')
# Fit on all texts (both datasets)
all_texts = pd.concat([df_collected['text'], df_ground['text']])
vectorizer.fit(all_texts)

# Transform texts to vectors
collected_vecs = vectorizer.transform(df_collected['text'])
ground_vecs = vectorizer.transform(df_ground['text'])

# --- Step 2: Compute cosine similarity ---
# Each row: collected post, columns: ground truth posts
similarity_matrix = cosine_similarity(collected_vecs, ground_vecs)  # shape: (78, 20)

# Maximum similarity for each collected post
df_collected['Max Similarity'] = similarity_matrix.max(axis=1)

# --- Step 3: Compute Harvest Rate for each threshold ---
hr_values = []

for t in thresholds:
    # Relevant if max similarity >= threshold
    relevant_flags = (df_collected['Max Similarity'] >= t).astype(int)
    hr = relevant_flags.sum() / len(df_collected)
    hr_values.append(hr)

# --- Step 4: Plot HR vs Threshold ---
plt.figure(figsize=(7,5))
plt.plot(thresholds, hr_values, marker='o')
plt.title("Decision Threshold vs Harvest Rate")
plt.xlabel("Decision Threshold (Max Cosine Similarity)")
plt.ylabel("Harvest Rate (HR)")
plt.grid(True)
plt.savefig("harvest_rate_cosine_plot.png", dpi=300, bbox_inches='tight')
plt.show()

# --- Step 5: Save updated CSV with similarity scores ---
df_collected.to_csv("response1_with_cosine_similarity.csv", index=False, encoding="utf-8")
print("✅ Cosine similarity calculated and CSV + plot saved.")
