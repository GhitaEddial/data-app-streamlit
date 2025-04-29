from google_play_scraper import search
import pandas as pd
import streamlit as st
import plotly.express as px

# Columns we want to keep in the final DataFrame
REQUIRED_COLUMNS = {
    'appId',
    'icon',
    'screenshots',
    'title',
    'score',
    'genre',
    'price',
    'free',
    'currency',
    'video',
    'videoImage',
    'descriptionHTML',
    'developer',
    'installs'
}

# Function to search for apps from the Play Store using a query
def search_api(search_query):
    result = search(
        search_query,
        lang="en",
        country="us",

    )
    return result

# Function to convert raw results into a DataFrame and clean it
def apps_to_dataframe(apps_list):
    df = pd.DataFrame(apps_list)

    # Keep only desired columns
    df = df[[col for col in REQUIRED_COLUMNS if col in df.columns]]

    # Convert list-type columns to string for readability
    list_columns = df.select_dtypes(include=['object']).columns
    for col in list_columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df[col] = df[col].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

    return df

# Function to show score distribution as bar chart
def scorecounts(filtered_data):
    bins = [0, 1, 2, 3, 4, 5]
    labels = ['0-1', '1-2', '2-3', '3-4', '4-5']
    filtered_data['score_bin'] = pd.cut(filtered_data['score'], bins=bins, labels=labels, include_lowest=True)
    score_counts = filtered_data['score_bin'].value_counts().sort_index()
    st.bar_chart(score_counts)

# Function to show pie chart of Free vs Paid apps
def paid_vs_free(filtered_data):
    free_paid_counts = filtered_data['free'].value_counts().reset_index()
    free_paid_counts.columns = ['Free', 'Count']
    free_paid_counts['Free'] = free_paid_counts['Free'].map({True: 'Free', False: 'Paid'})

    fig = px.pie(
        free_paid_counts,
        names='Free',
        values='Count',
        color='Free',
        color_discrete_map={'Free': '#66b3ff', 'Paid': '#ff9999'},
        title="Distribution of Free vs Paid Apps",
        hole=0.4
    )
    st.plotly_chart(fig)
