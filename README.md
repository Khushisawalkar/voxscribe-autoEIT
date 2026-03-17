# 🎙️ VoxScribe — AutoEIT Learner Speech Transcription Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/MachineLearning-ASR-green?style=for-the-badge)
![Whisper](https://img.shields.io/badge/Model-OpenAI%20Whisper-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

Evaluation submission for **HumanAI – Google Summer of Code 2026**

**Project:** AutoEIT
**Focus:** Automatic transcription of learner speech recordings.

---

# 🌍 Project Motivation

The **Elicited Imitation Task (EIT)** is widely used in second-language research to evaluate global language proficiency.

Participants listen to sentences and attempt to reproduce them.
These recordings contain valuable linguistic information but require **manual transcription**, which is:

⚠️ Time-consuming
⚠️ Difficult to scale
⚠️ Expensive for large datasets

This project explores how **modern speech recognition models** can assist researchers by automatically generating transcriptions of learner speech.

---

# 🧠 Key Challenge

Learner speech is significantly harder for automatic systems than native speech.

Common challenges include:

• pronunciation variation
• grammatical deviations
• hesitations and pauses
• partial sentence reproduction

Handling these issues is essential for reliable automatic transcription.

---

# ⚙️ System Pipeline

```text
Audio Recordings
       ↓
Audio Processing
       ↓
Whisper Speech Recognition
       ↓
Transcription Extraction
       ↓
Structured CSV Dataset
```

The resulting dataset can support:

✔ linguistic research
✔ automated scoring systems
✔ large-scale learner speech analysis

---

# 🛠️ Technologies Used

| Tool            | Purpose                     |
| --------------- | --------------------------- |
| Python          | Core programming language   |
| OpenAI Whisper  | Speech recognition          |
| Pandas          | Data processing             |
| Librosa         | Audio handling              |
| Jupyter / Colab | Experimentation environment |

---

# 📁 Repository Structure

```
voxscribe-autoEIT
│
├── data
│   └── sample EIT audio recordings
│
├── notebooks
│   └── autoEIT_transcription_pipeline.ipynb
│
├── results
│   └── transcriptions.csv
│
├── src
│   ├── transcription_pipeline.py
│   └── evaluation.py
│
├── docs
│   └── pipeline.png
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 📊 Example Output

| Audio File        | Predicted Transcription             |
| ----------------- | ----------------------------------- |
| 038010_EIT-2A.mp3 | la niña fue al mercado con su madre |
| 038011_EIT-1A.mp3 | el hombre caminó por el parque      |

The generated CSV file can be used for **further analysis or automated scoring**.

---

# 📈 Evaluation Approach

Transcription quality can be measured using **Word Error Rate (WER)**.

WER measures differences between predicted and reference sentences by counting:

• insertions
• deletions
• substitutions

Lower values indicate more accurate transcriptions.

---

# 🔎 Observations

Initial experiments show that Whisper can produce useful baseline transcriptions for learner speech.

However, some errors occur due to:

• pronunciation differences
• sentence truncation
• speech disfluencies

These observations highlight opportunities for **future research improvements**.

---

# 🚀 Future Work

Possible extensions of this work include:

• fine-tuning ASR models on learner speech datasets
• automated scoring of EIT responses
• phonetic error correction pipelines
• large-scale learner speech transcription systems

These directions could significantly improve transcription quality and usability.

---

# 🔁 Reproducibility

To reproduce the transcription pipeline:

### Install dependencies

```
pip install -r requirements.txt
```

### Run the pipeline

```
python src/transcription_pipeline.py
```

Results will be generated inside the **results/** folder.

---

# 👩‍💻 Author

- Khushi Sawalkar

B.Tech — Electronics & Telecommunications Engineering
Minor in Information Technology

Technical interests:
• Machine Learning
• Signal Processing
• Data Analysis
• Embedded Systems

Projects:
• Arduino MP3 Player
• Occupancy-Dependent Domestic Power Conservation System

---

# 📜 License

This project is released under the **MIT License**.

---

⭐ If you find this repository useful for learner-speech research, feel free to explore and build upon it.
