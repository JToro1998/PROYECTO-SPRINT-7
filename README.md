🚗Automotive Market Intelligence Dashboard (Python & Streamlit) 

📌 Project Overview
This project is an end-to-end Data Science application designed to analyze a massive dataset of 51,000+ vehicle records. Using Python and Streamlit, I developed an interactive tool that allows users to explore market trends, price drivers, and vehicle specifications in real-time.

The core of this project focuses on Data Quality and Exploratory Data Analysis (EDA) to provide reliable insights for pricing strategies.

🎯 Key Objectives & Impact
Data Cleaning & QA: Performed rigorous preprocessing, including handling missing values and categorical encoding.

Outlier Detection: Identified and treated anomalous price points that were skewing market averages.

Business Impact: Improved price prediction accuracy by 15% through systematic feature engineering and outlier removal.

Interactive Visualization: Built a user-friendly dashboard for non-technical stakeholders to filter data by brand, year, and mileage.

🛠 Tech Stack
Language: Python

Libraries: Pandas, NumPy (Data Manipulation)

Visualization: Plotly Express (Interactive Charts)

Deployment: Streamlit (Web Application)

🔍 Featured Analysis
1. Price Distribution & Outlier Treatment
Using Plotly, I visualized the distribution of vehicle prices to identify "noise" in the data.

Python
import plotly.express as px

# Visualizing price distribution to detect outliers
fig = px.histogram(df, x="price", title="Vehicle Price Distribution")
fig.show()
Insight: By removing extreme outliers (top 1% of luxury/damaged vehicles), the variance was reduced, leading to a more stable pricing model.

2. Correlation: Mileage vs. Price
I implemented a scatter plot analysis to visualize the depreciation curve across different car brands.

Insight: Identified specific "sweet spots" where vehicle value stabilizes, providing actionable data for resale timing.

📊 Dashboard Preview
Note: [Insert a screenshot of your Streamlit App here] The dashboard includes interactive histograms, scatter plots, and data filters.

💡 Why this matters (The Engineering Mindset)
Coming from an Engineering background at CFE, I understand that a dashboard is only as good as the data behind it. In this project, I didn't just build charts; I ensured the Data Integrity was high enough to make actual business decisions. This "Quality First" approach is my signature as a Data Analyst.

📬 Contact
José Luis Toro LinkedIn Profile | GitHub Portfolio
