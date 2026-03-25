import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from difflib import ndiff

from src.database import init_db

# Init DB
init_db()

st.set_page_config(page_title="VoxScribe Dashboard", layout="wide")

st.title("🎤 VoxScribe — AutoEIT Dashboard")
st.markdown("AI-powered transcription + evaluation system for learner speech (EIT)")

# Load DB
conn = sqlite3.connect("results.db")

try:
    df = pd.read_sql_query("SELECT * FROM runs", conn)
except:
    df = pd.DataFrame()

if df.empty:
    st.warning("⚠️ No runs found. Run the model first.")
else:
    # =====================
    # METRICS
    # =====================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📊 Total Runs", len(df))

    with col2:
        st.metric("🏆 Best Accuracy", f"{df['accuracy'].max()*100:.2f}%")

    with col3:
        st.metric("📉 Avg Accuracy", f"{df['accuracy'].mean()*100:.2f}%")

    st.divider()

    # =====================
    # GRAPH
    # =====================
    df["run_id"] = range(1, len(df) + 1)

    st.subheader("📈 Accuracy Trend Over Runs")

    fig, ax = plt.subplots()

    ax.plot(df["run_id"], df["accuracy"], marker='o', linewidth=3)

    best_idx = df["accuracy"].idxmax()
    ax.scatter(df.loc[best_idx, "run_id"], df["accuracy"].max(), s=100)

    ax.set_title("Model Performance")
    ax.set_xlabel("Run Number")
    ax.set_ylabel("Accuracy")
    ax.set_xticks(df["run_id"])
    ax.set_ylim(0, 1)
    ax.grid(True)

    st.pyplot(fig)

    if len(df) == 1:
        st.info("Only one run available. Run more samples to see trends.")

    st.divider()

    # =====================
    # TABLE (CLEAN)
    # =====================
    st.subheader("📊 Run History")

    df_display = df.copy()
    df_display["transcription"] = df_display["transcription"].str[:100] + "..."
    df_display["cleaned_text"] = df_display["cleaned_text"].str[:100] + "..."

    st.dataframe(df_display, use_container_width=True)

    st.divider()

    # =====================
    # SELECT RUN
    # =====================
    st.subheader("🔍 Inspect Run")

    selected_index = st.selectbox(
        "Choose Run",
        df.index,
        format_func=lambda x: f"Run {x+1} | {df.loc[x, 'filename']}"
    )

    selected = df.loc[selected_index]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧾 Raw Transcription")
        st.text_area("", selected["transcription"], height=250)

    with col2:
        st.markdown("### ✨ Cleaned Output")
        st.text_area("", selected["cleaned_text"], height=250)

    # =====================
    # DIFF VIEW 🔥
    # =====================
    def highlight_diff(a, b):
        diff = list(ndiff(a.split(), b.split()))
        result = []

        for word in diff:
            if word.startswith("- "):
                result.append(f"<span style='color:red'>{word[2:]}</span>")
            elif word.startswith("+ "):
                result.append(f"<span style='color:green'>{word[2:]}</span>")
            elif word.startswith("  "):
                result.append(word[2:])

        return " ".join(result)

    st.subheader("🔍 Difference View")
    st.markdown(
        highlight_diff(selected["transcription"], selected["cleaned_text"]),
        unsafe_allow_html=True
    )

    # =====================
    # AUDIO 🔥
    # =====================
    st.subheader("🎧 Audio Playback")
    st.audio(selected["filename"])

    # =====================
    # QUALITY STATUS
    # =====================
    acc = selected["accuracy"]

    if acc > 0.9:
        st.success("🔥 Excellent transcription quality")
    elif acc > 0.8:
        st.info("👍 Good transcription quality")
    else:
        st.warning("⚠️ Needs improvement")

    st.divider()

    # =====================
    # BEST RUN
    # =====================
    st.subheader("🏆 Best Performing Run")

    best = df.loc[df["accuracy"].idxmax()]

    st.success(f"""
    📁 File: {best['filename']}  
    🎯 Accuracy: {best['accuracy']:.3f}  
    🕒 Timestamp: {best['timestamp']}
    """)

conn.close()