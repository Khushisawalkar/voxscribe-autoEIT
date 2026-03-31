import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

from src.database import init_db

init_db()

st.set_page_config(page_title="VoxScribe AutoEIT", layout="wide")

st.title("VoxScribe — AutoEIT Dashboard")
st.markdown("AI-powered transcription + evaluation for Spanish EIT learner speech")

conn = sqlite3.connect("results.db")
try:
    df = pd.read_sql_query("SELECT * FROM runs ORDER BY timestamp DESC", conn)
except:
    df = pd.DataFrame()
conn.close()

if df.empty:
    st.warning("No runs found. Run `python main.py` first.")
    st.stop()

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Runs", len(df))
col2.metric("Best Accuracy", f"{df['accuracy'].max():.2f}%")
col3.metric("Avg Accuracy", f"{df['accuracy'].mean():.2f}%")

st.divider()

# Chart
st.subheader("Accuracy per Participant")
fig, ax = plt.subplots(figsize=(10, 4))
colors = ['#4CAF50' if s >= 50 else '#FF9800' if s >= 30 else '#F44336'
          for s in df['accuracy']]
bars = ax.bar(df['filename'], df['accuracy'], color=colors, edgecolor='white')
ax.set_ylabel("Accuracy (%)")
ax.set_ylim(0, 100)
ax.tick_params(axis='x', rotation=15)
for bar, val in zip(bars, df['accuracy']):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1,
            f'{val:.1f}%', ha='center', fontsize=9, fontweight='bold')
avg = df['accuracy'].mean()
ax.axhline(y=avg, color='navy', linestyle='--', label=f"Avg: {avg:.1f}%")
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

st.divider()

# Scores table
if os.path.exists("results/sentence_scores.csv"):
    st.subheader("Sentence-level Scores")
    scores_df = pd.read_csv("results/sentence_scores.csv")
    participant = st.selectbox("Filter by participant", ["All"] + list(scores_df["Participant"].unique()))
    if participant != "All":
        scores_df = scores_df[scores_df["Participant"] == participant]
    st.dataframe(scores_df, use_container_width=True)

st.divider()

# Inspect run
st.subheader("Inspect Transcription")
idx = st.selectbox("Select run",
    df.index,
    format_func=lambda x: f"{df.loc[x,'filename']} | {df.loc[x,'accuracy']:.2f}%")
selected = df.loc[idx]
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Raw Transcription")
    st.text_area("Raw", selected["transcription"], height=250,
                 label_visibility="collapsed")
with col2:
    st.markdown("#### Cleaned Output")
    st.text_area("Cleaned", selected["cleaned_text"], height=250,
                 label_visibility="collapsed")

st.divider()

# Best run
best = df.loc[df['accuracy'].idxmax()]
st.success(f"Best: {best['filename']} | Accuracy: {best['accuracy']:.2f}% | {best['timestamp']}")