import streamlit as st
import pandas as pd
from query_faiss import faiss_search  # ✅ Your search logic

# Page config
st.set_page_config(
    page_title="SHL Assessment Recommender",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS for dark theme and stylish cards
st.markdown("""
    <style>
        .stApp {
            background-color: #121212;
            color: #ffffff;
        }
        .title {
            font-size: 2.8em;
            font-weight: bold;
            color: #00ADB5;
            margin-bottom: 0.5em;
        }
        .subtitle {
            font-size: 1.2em;
            color: #BBBBBB;
            margin-bottom: 1.5em;
        }
        .assessment-card {
            background-color: #1E1E1E;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 1.2em;
            margin-bottom: 1em;
            box-shadow: 0 4px 10px rgba(0, 173, 181, 0.2);
        }
        .assessment-title {
            font-size: 1.3em;
            color: #00ADB5;
            font-weight: bold;
            margin-bottom: 0.3em;
        }
        .assessment-detail {
            font-size: 0.95em;
            color: #DDDDDD;
            margin: 0.2em 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🔍 SHL Assessment Recommendation Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter a job description or role to get matching SHL assessments.</div>", unsafe_allow_html=True)

# User input
query = st.text_input("💼 Enter job description or query:")

# Search and display results
if query:
    with st.spinner("🔎 Searching for matching assessments..."):
        results = faiss_search(query)

        if not results.empty:
            st.success("✅ Top Matching Assessments")
            for _, row in results.iterrows():
                assessment_name = f"<a href='{row['Link']}' target='_blank' class='assessment-title'>{row['Test Name']}</a>"
                remote = f"🖥️ Remote: {row['Remote Testing']}"
                adaptive = f"🧠 Adaptive/IRT: {row['Adaptive/IRT']}"
                test_type = f"📘 Test Type: {row['Test Type']}"
                duration = f"⏱️ Duration: {row['Duration']}"

                st.markdown(f"""
                    <div class='assessment-card'>
                        {assessment_name}
                        <div class='assessment-detail'>{remote}</div>
                        <div class='assessment-detail'>{adaptive}</div>
                        <div class='assessment-detail'>{test_type}</div>
                        <div class='assessment-detail'>{duration}</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No matching assessments found. Try refining your query.")
