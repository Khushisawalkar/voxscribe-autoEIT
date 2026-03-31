🎙️ Voxscribe AutoEIT: Robust Audio-to-Text Transcription Pipeline for Spanish Elicited Imitation Tasks

Voxscribe AutoEIT: Robust Audio-to-Text Transcription Pipeline for Spanish Elicited Imitation Tasks is an AI-assisted audio transcription and editing tool designed to convert spoken audio into structured, readable text. Unlike basic transcription tools, this project focuses on improving the usability of generated text through segmentation and light post-processing.

The goal of this project is to reduce manual effort when working with audio content such as lectures, podcasts, meetings, and voice notes.

📌 Problem Statement

Most transcription tools generate raw text output that requires additional manual cleaning and formatting. This becomes time-consuming, especially for long audio files.

There is a need for a system that:

Automates transcription
Structures the output
Reduces post-processing effort
🎯 Objectives
Convert audio input into accurate text
Segment long audio into meaningful parts
Improve readability of transcripts
Build a simple, modular, and extensible system
🚀 Features
🎧 Audio-to-text transcription using Whisper
✂️ Automatic segmentation of long audio
🧠 Basic post-processing for cleaner output
⚡ Lightweight command-line interface
📄 Organized output storage
🛠️ Tech Stack
Language: Python
Model: Whisper
Libraries: NumPy, audio processing libraries
🧩 System Architecture

The system follows a pipeline-based approach:

Audio Input
Preprocessing
Transcription (Whisper)
Segmentation
Post-processing
Output Generation
⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/voxscribe-autoedit.git

cd voxscribe-autoedit

Install dependencies:

pip install -r requirements.txt

Install Whisper:

pip install openai-whisper

▶️ Usage

Run the project using:

python main.py --input <audio_file>

Example:

python main.py --input sample.mp3

Output will be stored in the outputs/ directory.

📊 Output Description

The generated output includes:

Transcribed text
Segmented content
Improved readability compared to raw output
💡 Design Decisions
CLI-based design: Simple, fast, and easy to test
Whisper integration: Reliable transcription performance
Modular structure: Easy to extend and maintain
⚠️ Limitations
Accuracy depends on audio quality
Limited post-processing features
No graphical interface yet
🔮 Future Scope
Text summarization
Multi-language support
Real-time transcription
GUI / Web interface
Subtitle export (SRT, VTT)
Integration with content platforms
🧪 Testing
Tested with short and long audio samples
Performs best with clear speech and minimal noise
📈 Roadmap
 Improve segmentation logic
 Add summarization module
 Enhance formatting of transcripts
 Add multi-language support
 Build UI for better usability
🤝 Contributing

Contributions are welcome.

Steps:

Fork the repository
Create a new branch (feature/your-feature-name)
Make your changes
Commit with clear messages
Submit a pull request
📜 License

This project is licensed under the MIT License.
