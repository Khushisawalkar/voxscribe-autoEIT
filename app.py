import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from src.database import init_db

# Ensure DB exists
init_db()

st.set_page_config(
    page_title="VoxScribe AutoEIT",
    layout="wide"
)

st.title("🎤 VoxScribe — AutoEIT Dashboard")
st.markdown("AI-powered transcription + evaluation system for learner speech")

# Load DB
conn = sqlite3.connect("results.db")

try:
    df = pd.read_sql_query("SELECT * FROM runs", conn)
except:
    df = pd.DataFrame()

if df.empty:
    st.warning("⚠️ No runs found. Run `python main.py` first.")
else:
    # 🔥 METRICS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📊 Total Runs", len(df))

    with col2:
        st.metric("🏆 Best Accuracy", f"{df['accuracy'].max():.2f}%")

    with col3:
        st.metric("📉 Avg Accuracy", f"{df['accuracy'].mean():.2f}%")

    st.divider()

    # 🔥 GRAPH
    st.subheader("📈 Accuracy Trend")

    fig, ax = plt.subplots()
    ax.plot(df["accuracy"], marker='o')
    ax.set_xlabel("Run Index")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Model Performance Over Runs")
    ax.grid(True)

    st.pyplot(fig)

    st.divider()

    # 🔥 TABLE
    st.subheader("📊 Run History")
    st.dataframe(df, use_container_width=True)

    st.divider()

    # 🔥 SELECT RUN
    st.subheader("🔍 Inspect Run")

    idx = st.selectbox(
        "Select Run",
        df.index,
        format_func=lambda x: f"{df.loc[x,'filename']} | {df.loc[x,'accuracy']:.2f}%"
    )

    selected = df.loc[idx]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧾 Raw Transcription")
        st.text_area("", selected["transcription"], height=250)

    with col2:
        st.markdown("### ✨ Cleaned Output")
        st.text_area("", selected["cleaned_text"], height=250)

    st.divider()

    # 🔥 BEST RUN
    st.subheader("🏆 Best Run")

    best = df.loc[df["accuracy"].idxmax()]

    st.success(f"""
    📁 File: {best['filename']}  
    🎯 Accuracy: {best['accuracy']:.2f}%  
    🕒 Time: {best['timestamp']}
    """)

conn.close()