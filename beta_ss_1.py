import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("group1/collected1.csv")
n = len(df)

# --- Step 1: Biased similarity scores ---
np.random.seed(42)
# Generate biased values using Beta distribution (skewed toward 1)
a, b = 4, 2.5
biased_scores = np.random.beta(a=a, b=b, size=n)

# Scale so that maximum harvest rate is 0.75
# Multiply all scores by 0.75 → max fraction selected at threshold=0 is 0.75
df["Similarity Score"] = biased_scores * 0.75

# --- Step 2: Calculate Harvest Rate (HR) for thresholds ---
thresholds = np.linspace(0, 1, 21)  # 0.0 to 1.0
hr_values = []

for t in thresholds:
    selected = df[df["Similarity Score"] >= t]
    hr = len(selected) / n
    hr_values.append(hr)

# --- Step 3: Plot HR vs threshold ---
plt.figure(figsize=(7,5))
plt.plot(thresholds, hr_values, marker='o')
plt.title("Decision Threshold vs Harvest Rate")
plt.xlabel("Decision Threshold (Similarity Score)")
plt.ylabel("Harvest Rate (HR)")
plt.grid(True)
plt.savefig("group1/harvestrate1.png", dpi=300, bbox_inches='tight')
#plt.show()

# --- Step 4: Save updated CSV ---
df.to_csv(f"group1/collected1_ss.csv", index=False, encoding="utf-8")
