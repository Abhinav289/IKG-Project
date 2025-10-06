import pandas as pd

df = pd.read_csv('group2/response2.csv')

# Calculate tweet length in characters and words
df["char_length"] = df["text"].str.len()
df["word_length"] = df["text"].apply(lambda x: len(str(x).split()))

# Summary statistics
avg_chars = df["char_length"].mean()
min_chars = df["char_length"].min()
max_chars = df["char_length"].max()

avg_words = df["word_length"].mean()
min_words = df["word_length"].min()
max_words = df["word_length"].max()

print("📏 Tweet Length Statistics:")
print(f"Characters → Avg: {avg_chars:.2f}, Min: {min_chars}, Max: {max_chars}")
print(f"Words      → Avg: {avg_words:.2f}, Min: {min_words}, Max: {max_words}")

# --- Sampling process ---

# Filter tweets with at least 35 words
filtered_df = df[df["word_length"] >= 35]

# Randomly sample 20 tweets (ground truth)
sampled_df = filtered_df.sample(n=20, random_state=42) if len(filtered_df) >= 20 else filtered_df
sampled_df.to_csv("group2/groundtruth2.csv", index=False, encoding="utf-8")

# Randomly sample 5 tweets for seed
seed_df = df.sample(n=5, random_state=42)
seed_df.to_csv("group2/seed2.csv", index=False, encoding="utf-8")

# --- Remove sampled tweets from df before saving ---
# Remove rows that appear in either sampled_df or seed_df
ids_to_remove = pd.concat([sampled_df["id"], seed_df["id"]]).unique()
df_remaining = df[~df["id"].isin(ids_to_remove)]

# Save the remaining tweets
df_remaining.to_csv("group2/collected2.csv", index=False, encoding="utf-8")

print(f"✅ Original rows: {len(df)}")
print(f"🗑️  Removed rows: {len(ids_to_remove)}")
print(f"📄 Remaining rows: {len(df_remaining)}")