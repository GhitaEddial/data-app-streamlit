import streamlit as st

st.set_page_config(page_title="Competitor Analysis", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .stApp {
            background-color: #0D3311;
        }
        h1 {
            font-size: 64px;
            line-height: 1.2;
            color: white;
            font-weight: 700;
            text-align: center;
            margin-bottom: 40px;
        }
        .highlight {
            background-color: #ffffff33;
            padding: 5px 15px;
            border-radius: 12px;
        }
        .description-box {
            background-color: #ADEBB3;
            padding: 30px;
            margin: 0 auto;
            width: 80%;
            border-radius: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: 500;
            color: #0D3311;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .tagline {
            font-size: 36px;
            font-weight: 800;
            margin-top: 25px;
            color: #0D3311;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1>
        Monitor <span class="highlight">all</span> your competitors'<br>marketing moves
    </h1>
""", unsafe_allow_html=True)

# Description with big bold tagline
st.markdown("""
    <div class="description-box">
        Ever wondered how your competitors are crushing it on app stores? 📱<br><br>
        This app lets you spy (ethically 😉) on trending apps, track their ratings, features, and more — all in one clean dashboard.<br><br>
        <span class="tagline">Search it, see it, analyze it.</span>
    </div>
""", unsafe_allow_html=True)
