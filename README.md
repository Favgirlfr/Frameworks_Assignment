📊 CORD-19 Data Explorer

This project is a beginner-friendly data analysis and visualization of the CORD-19 dataset (COVID-19 research papers metadata). The goal is to practice working with real-world data, cleaning it, creating insights, and building an interactive web app using Streamlit.

🎯 Objectives

Load and explore the CORD-19 metadata.csv dataset.

Perform basic data cleaning and preparation.

Analyze and visualize research trends over time.

Build an interactive dashboard with Streamlit.

Present key insights from the dataset.

📂 Project Structure

├── frameworks.py          # Python file for exploration & cleaning  
├── streamlit_app.py      # Streamlit application file  
├── metadata.csv         # Original dataset (too large for project use)  
├── metadata_sample.csv  # Smaller sampled dataset for faster analysis  
└── README.md            # Project documentation

⚙️ Requirements

Install the required Python libraries before running the project:

pip install pandas matplotlib streamlit

▶️ How to Run
Step 1: Run Frameworks (Optional)

If you want to explore the data and test plots before Streamlit:

python frameworks.py

Step 2: Run Streamlit App

Launch the dashboard in your browser:

streamlit run streamlit_app.py

📊 Features of the App

The Streamlit app provides:

Year Range Filter → Select publication years with a slider.

Publications by Year → Bar chart showing research output over time.

Top Journals → Bar chart of the 10 most active journals.

Abstract Word Count Distribution → Histogram of abstract lengths.

Data Preview → View a sample of the dataset.

Insights Section → Displays key findings dynamically and statically.

🔎 Example Insights

COVID-19 research activity peaked in 2020.

A few journals published the majority of papers.

Abstract lengths vary widely, reflecting differences in reporting detail.

📁 Dataset Information

Source: CORD-19 Research Dataset (Kaggle)

File Used: metadata.csv (sampled to metadata_sample.csv for faster analysis).

Contains metadata on COVID-19 research papers: titles, abstracts, authors, publication date, and journals.
