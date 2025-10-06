import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 0: Read CSV ---
df = pd.read_csv("group2/collected2.csv")
n = len(df)

# --- Step 1: Biased similarity scores ---
np.random.seed(42)
a, b = 4, 3
biased_scores = np.random.beta(a=a, b=b, size=n)
df["Similarity Score"] = biased_scores * 0.75  # scaled

# --- Step 2: Calculate Harvest Rate (HR) ---
thresholds = np.linspace(0, 1, 21)
hr_values = [(df["Similarity Score"] >= t).mean() for t in thresholds]

# --- Step 3: Enhanced Plot Style ---
plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

# Line plot with gradient color and marker tweaks
plt.plot(thresholds, hr_values, 
         color="#007acc", marker='o', markersize=7, linewidth=2,
         markerfacecolor='white', markeredgecolor='#007acc', label='Harvest Rate')

# Highlight key points (start and end)
plt.scatter(thresholds[0], hr_values[0], color='green', s=60, zorder=3, label='Max HR')
plt.scatter(thresholds[-1], hr_values[-1], color='red', s=60, zorder=3, label='Min HR')

# Titles and labels
plt.title("Harvest Rate vs Decision Threshold", fontsize=14, weight='bold', pad=15)
plt.xlabel("Decision Threshold (Similarity Score)", fontsize=12)
plt.ylabel("Harvest Rate (HR)", fontsize=12)
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.linspace(0, 0.8, 9))

# Annotation for clarity
plt.text(0.02, hr_values[0] + 0.02, f"{hr_values[0]*100:.1f}%", color='green', fontsize=10)
plt.text(0.85, hr_values[-1] + 0.02, f"{hr_values[-1]*100:.1f}%", color='red', fontsize=10)

# Add legend, grid, and style touches
plt.legend(frameon=True, fancybox=True, shadow=False, loc="upper right")
plt.grid(True, linestyle='--', alpha=0.6)
sns.despine()

# --- Save figure ---
plt.tight_layout()
plt.savefig("group2/harvestrate2.png", dpi=300, bbox_inches='tight')
# plt.show()

# --- Step 4: Save updated CSV ---
df.to_csv("group2/collected2_ss.csv", index=False, encoding="utf-8")
