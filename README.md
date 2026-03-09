# VoxScribe – AutoEIT Transcription Pipeline

This repository contains my evaluation test implementation for the **HumanAI GSoC 2026 AutoEIT project**.

## Objective

The goal of this project is to develop a pipeline that converts audio recordings from Spanish Elicited Imitation Tasks (EIT) into usable text transcriptions for linguistic analysis.

Non-native learner speech presents challenges for automatic speech recognition systems because of:

* varying accents
* disfluencies
* phonological transfer
* incomplete sentence reproduction

This implementation demonstrates a baseline transcription pipeline using **OpenAI Whisper**.

## Approach

The system performs the following steps:

1. Load audio recordings from the dataset.
2. Use Whisper ASR to transcribe Spanish learner speech.
3. Store generated transcriptions in a structured CSV file.
4. Prepare outputs suitable for linguistic analysis and scoring.

## Repository Structure

```
voxscribe-autoEIT
│
├── data
│   └── sample EIT audio recordings
│
├── notebooks
│   └── transcription_analysis.ipynb
│
├── results
│   └── transcriptions.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Tools Used

* Python
* OpenAI Whisper
* Pandas
* Librosa
* Jupyter / Google Colab

## Output

The pipeline produces a CSV file containing:

* audio filename
* generated transcription

These outputs can be used for downstream **automatic scoring or linguistic evaluation**.

## Future Improvements

Potential improvements include:

* fine-tuning ASR models on learner speech
* noise reduction and preprocessing
* post-processing to correct predictable learner transcription errors
* integration with automated scoring systems

## Author

Khushi Sawalkar
B.Tech Electronics & Telecommunications Engineering
