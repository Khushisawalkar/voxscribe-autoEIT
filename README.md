# VoxScribe – AutoEIT Transcription Pipeline

This repository contains my evaluation test implementation for the HumanAI GSoC 2026 AutoEIT project.

## Goal

Develop a pipeline to transcribe Spanish Elicited Imitation Task (EIT) recordings using automatic speech recognition.

The goal is to produce accurate transcripts while preserving learner disfluencies and grammatical errors.

## Approach

The pipeline uses Whisper ASR to process Spanish learner speech recordings.

Steps:

1. Load audio files
2. Run Whisper transcription
3. Preserve learner speech patterns
4. Store transcripts in structured format

## Repository Structure

voxscribe-autoEIT  
│  
├── data  
├── notebooks  
│ └── transcription_analysis.ipynb  
├── README.md  
├── requirements.txt  
└── .gitignore  

## Tools Used

- Python
- Whisper ASR
- Pandas
- Jupyter Notebook

## Challenges

- Non-native pronunciation variation
- Disfluencies and hesitations
- Partial sentence repetition
- Accent variability

## Future Work

- Improve ASR accuracy for learner speech
- Automatic EIT scoring
- Error pattern detection
