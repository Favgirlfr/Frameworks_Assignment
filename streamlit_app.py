import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------
# Load the dataset
# --------------------------
df = pd.read_csv("metadata_sample.csv")

# Convert dates and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# --------------------------
# Streamlit App Layout
# --------------------------
st.title("CORD-19 Data Explorer")
st.write("An interactive app to explore COVID-19 research publications from the CORD-19 dataset.")

# --------------------------
# Interactive Widgets
# --------------------------
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (2019, 2022))

# Filter data based on year selection
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# --------------------------
# Visualization 1: Publications by Year
# --------------------------
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("COVID-19 Publications per Year")
st.pyplot(fig)

# --------------------------
# Visualization 2: Top Journals
# --------------------------
st.subheader("Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)

fig, ax = plt.subplots()
top_journals.plot(kind="bar", ax=ax)
ax.set_xlabel("Journal")
ax.set_ylabel("Number of Publications")
ax.set_title("Top 10 Journals Publishing COVID-19 Research")
st.pyplot(fig)

# --------------------------
# Visualization 3: Word Count Distribution
# --------------------------
st.subheader("Abstract Word Count Distribution")
filtered_df["abstract_word_count"] = filtered_df["abstract"].fillna("").apply(lambda x: len(x.split()))

fig, ax = plt.subplots()
ax.hist(filtered_df["abstract_word_count"], bins=30)
ax.set_xlabel("Word Count")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Abstract Word Counts")
st.pyplot(fig)

# --------------------------
# Data Preview
# --------------------------
st.subheader("Sample of the Data")
st.write(filtered_df.head())

# --------------------------
# Insights Section
# --------------------------
st.subheader("Insights")

# Dynamic Insights
if not year_counts.empty:
    peak_year = year_counts.idxmax()
    peak_pubs = year_counts.max()
    st.write(f"📌 The highest number of publications was in **{peak_year}**, with **{peak_pubs} papers**.")
else:
    st.write("No publications in the selected year range.")

# Static Insights
st.write("""
- COVID-19 research activity increased sharply in 2020 as the pandemic spread.  
- Research output is spread across multiple journals, with a few publishing most of the work.  
- Abstracts vary widely in length, showing differences in reporting detail.  
""")

