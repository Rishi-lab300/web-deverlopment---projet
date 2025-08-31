import pandas as pd
import matplotlib.pyplot as plt
#load the csv file
df = pd.read_csv("youtube.csv")
df.dropna(subset=["video_id","title","channel_name","category","views","likes","dislikes"])

cateogry_count = df['category'].value_counts().head(5)
plt.figure(figsize=(8,5))
plt.bar(cateogry_count.index,cateogry_count.values,color = 'purple')
plt.title("Top 5 categories by number of videos")
plt.xlabel("Types of catgories")
plt.ylabel("Number of Videos")
plt.tight_layout()
plt.savefig("categories_count.png")
plt.show()
# Plot histogram of views (normalized 0–1 range)
plt.figure(figsize=(9,6))
plt.hist(df['views'], bins=20, color="orange", edgecolor="black", alpha=0.8)

# Title & labels
plt.title("Distribution of Video Views", fontsize=14, fontweight="bold")
plt.xlabel("Views (%)", fontsize=12)
plt.ylabel("Number of Videos", fontsize=12)

# Convert x-axis from 0–1 to 0–100%
plt.xticks([i/10 for i in range(0,11)], [f"{i*10}%" for i in range(0,11)])

# Grid for better readability
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save & show
plt.tight_layout()
plt.savefig("views_histogram.png")
plt.show()
