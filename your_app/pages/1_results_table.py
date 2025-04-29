import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import search_api, apps_to_dataframe

# Page config
st.set_page_config(page_title="📱 App Search Results", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #0D3311;
        }
        .title {
            text-align: center;
            color: white;
            font-size: 48px;
            font-weight: bold;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        .input-box {
            background-color: #ADEBB3;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: center;
        }
        .data-section {
            background-color: #ffffffcc;
            padding: 20px;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Title
st.markdown("<div class='title'>🔍 Find Trending Apps Instantly</div>", unsafe_allow_html=True)

# Search input box
with st.container():
    st.markdown("<div class='input-box'>", unsafe_allow_html=True)
    search_query = st.text_input('Enter the app name you want to search:')
    clicked = st.button("Search")
    st.markdown("</div>", unsafe_allow_html=True)

# Handle search and display results
if clicked:
    if search_query.strip():
        result = search_api(search_query)
        data = apps_to_dataframe(result)

        # Styled results section
        st.markdown("<div class='data-section'>", unsafe_allow_html=True)
        st.subheader("📋 Results Table")
        st.dataframe(data, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Optional: save to CSV
        data.to_csv("data.csv", index=False)
    else:
        st.warning("⚠️ You did not enter an app name!")
