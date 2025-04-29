import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import utils

# ---- PAGE CONFIG ----
st.set_page_config(page_title="📊 Visualizations", layout="wide")

# ---- STYLING ----
st.markdown("""
    <style>
        .stApp {
            background-color: #0D3311;
        }
        .section {
            background-color: #ffffffdd;
            padding: 20px 30px;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        .header {
            color: white;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<div class='header'>📊 App Competitor Analysis Dashboard</div>", unsafe_allow_html=True)

# ---- LOAD DATA ----
data = pd.read_csv('data.csv')

# ---- SIDEBAR FILTER ----
st.sidebar.header("🔍 Filter Apps")
app_ids = data['appId'].dropna().unique()
selected_app_ids = st.sidebar.multiselect(
    "Select Application ID(s):",
    options=app_ids,
    default=app_ids
)

filtered_data = data[data['appId'].isin(selected_app_ids)]

# ---- SCORE DISTRIBUTION ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader('📈 Score Distribution')
    utils.scorecounts(filtered_data)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- AVERAGE SCORE BY GENRE ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("📊 Average Score by Genre")
    avg_score_by_genre = data.groupby('genre')['score'].mean().sort_values()
    st.bar_chart(avg_score_by_genre)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- GENRE DISTRIBUTION ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader('📚 Genre Distribution')
    genre_counts = filtered_data['genre'].value_counts()
    st.bar_chart(genre_counts)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- FREE VS PAID PIE CHART ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader('💸 Free vs Paid Apps')
    utils.paid_vs_free(filtered_data)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- PRICE DISTRIBUTION ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("💰 Price Distribution (Paid Apps)")
    paid_apps = data[data['free'] == False]
    if not paid_apps.empty:
        fig, ax = plt.subplots()
        ax.hist(paid_apps['price'], bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Price')
        ax.set_ylabel('Number of Apps')
        st.pyplot(fig)
    else:
        st.info("No paid apps found.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---- TOP 10 INSTALLED ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader('🚀 Top 10 Apps by Installs')
    top_installed_apps = filtered_data[['title', 'installs']].sort_values('installs', ascending=False).head(10).set_index('title')
    st.bar_chart(top_installed_apps)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- VIDEO VS NO VIDEO ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("🎥 Apps With vs Without Videos")
    data['has_video'] = data['video'].notnull()
    video_counts = data['has_video'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(video_counts, labels=['With Video', 'Without Video'], autopct='%1.1f%%', startangle=90, colors=['#2196F3', '#FFC107'])
    ax.axis('equal')
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- TOP DEVELOPERS ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("👨‍💻 Top Developers by Number of Apps")
    top_developers = data['developer'].value_counts().head(10).sort_values()
    st.bar_chart(top_developers)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- WORD CLOUD ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader('☁️ Word Cloud from App Descriptions')
    if filtered_data['descriptionHTML'].notnull().any():
        text = ' '.join(filtered_data['descriptionHTML'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.warning("No descriptions available to generate word cloud.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---- SCATTER: INSTALLS VS SCORE ----
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("📉 Installs vs Score (Scatter Plot)")
    score_installs = data[['score', 'installs']]
    st.scatter_chart(score_installs, x='score', y='installs')
    st.markdown("</div>", unsafe_allow_html=True)
