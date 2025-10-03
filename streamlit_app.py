import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Merged CSV EDA", layout="wide")
st.title("Exploratory Data Analysis (EDA)")

# File path to merged CSV
file_path = os.path.join("data\raw\merged_file.csv")  # relative path from app folder

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, encoding='utf-8')
    df.columns = df.columns.str.strip()
    return df

df = load_data(file_path)

# Sidebar options
st.sidebar.header("EDA Options")
show_data = st.sidebar.checkbox("Show DataFrame")
show_info = st.sidebar.checkbox("Show Info")
show_summary = st.sidebar.checkbox("Show Summary Statistics")
show_visuals = st.sidebar.checkbox("Show Visualizations")

if show_data:
    st.subheader("DataFrame")
    st.dataframe(df)

if show_info:
    st.subheader("DataFrame Info")
    buffer = df.info()
    st.text(buffer)

if show_summary:
    st.subheader("Summary Statistics")
    st.dataframe(df.describe(include='all'))

if show_visuals:
    st.subheader("Feature Visualizations")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    st.markdown("### Numeric Column Histogram")
    if numeric_cols:
        selected_num = st.selectbox("Select numeric column", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_num].dropna(), kde=True, ax=ax)
        st.pyplot(fig)
    
    st.markdown("### Categorical Column Countplot")
    if categorical_cols:
        selected_cat = st.selectbox("Select categorical column", categorical_cols)
        fig, ax = plt.subplots()
        sns.countplot(y=df[selected_cat], order=df[selected_cat].value_counts().index, ax=ax)
        st.pyplot(fig)
    
    st.markdown("### Correlation Heatmap")
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)
