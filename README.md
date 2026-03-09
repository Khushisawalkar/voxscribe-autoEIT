# VoxScribe — AutoEIT Speech Transcription Pipeline

Evaluation submission for the **HumanAI Google Summer of Code 2026 – AutoEIT Project**.

This repository implements a speech-to-text pipeline for **Spanish Elicited Imitation Task (EIT)** recordings using OpenAI Whisper.

The goal is to automatically transcribe learner speech data to support linguistic analysis and automated scoring of language proficiency.

---

## Motivation

The **Elicited Imitation Task (EIT)** is widely used in second-language research to measure global language proficiency.

However, transcription of learner responses is typically done manually, which is:

* time-consuming
* expensive
* prone to human inconsistency

This project explores the use of **automatic speech recognition (ASR)** to generate transcriptions that can accelerate linguistic analysis.

Learner speech presents additional challenges:

* pronunciation variation
* grammatical deviations
* hesitations and pauses
* partial sentence reproduction

---

## Project Pipeline

Audio Files
↓
Preprocessing
↓
Whisper Speech Recognition
↓
Transcription Extraction
↓
Structured CSV Output

---

## Repository Structure

```
voxscribe-autoEIT
│
├── data
│   └── sample EIT recordings
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

## Technologies Used

* Python
* OpenAI Whisper
* Pandas
* NumPy
* Librosa
* Jupyter / Google Colab

---

## Output

The pipeline generates a CSV file containing:

* audio file name
* generated transcription
* model metadata

These outputs can be used for:

* linguistic analysis
* automated scoring of EIT responses
* evaluation of speech recognition accuracy

---

## Evaluation

Word Error Rate (WER) is used to estimate transcription quality by comparing predicted text with reference sentences.

---

## Author

**Khushi Sawalkar**

B.Tech Electronics & Telecommunications Engineering
Minor in Information Technology

Technical Interests:

* Machine Learning
* Signal Processing
* Embedded Systems
* Data Analysis

Projects:

* Arduino MP3 Player
* Occupancy Dependent Power Conservation System

---

## License

This project is released under the MIT License.
