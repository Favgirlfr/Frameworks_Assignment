import pandas as pd

# Load full metadata
df = pd.read_csv("metadata.csv")

# Take a random sample of 1000 rows
sample_df = df.sample(n=1000, random_state=42)

# Save it as a smaller CSV
sample_df.to_csv("metadata_sample.csv", index=False)

print("Sample saved to metadata_sample.csv")

# Drop rows with no title or publish_time
df = df.dropna(subset=["title", "publish_time"])

# Convert to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Word count of abstract
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

import matplotlib.pyplot as plt
import seaborn as sns

# Publications by year
year_counts = df["year"].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Top journals
top_journals = df["journal"].value_counts().head(10)
top_journals.plot(kind="barh", color="skyblue")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.show()
