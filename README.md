# \# 🎙️ VoxScribe — AutoEIT Pipeline

# \### GSoC 2026 Evaluation Test | HumanAI @ CERN

# \*\*Author:\*\* Khushi Sawalkar

# 

# \## What This Does

# \- \*\*Test I:\*\* Transcribes Spanish EIT audio files using OpenAI Whisper

# \- \*\*Test II:\*\* Scores learner utterances using WER + fuzzy matching rubric

# 

# \## Project Structure

# ```

# voxscribe-autoEIT/

# ├── src/

# │   ├── transcription.py    # Whisper ASR

# │   ├── preprocessing.py    # Audio prep

# │   ├── postprocessing.py   # Text cleaning

# │   ├── evaluation.py       # WER + scoring

# │   ├── segmentation.py     # Audio chunking

# │   └── database.py         # SQLite storage

# ├── data/

# │   ├── processed/          # 4 EIT wav files

# │   └── chunks/             # Segmented audio

# ├── results/                # Transcription outputs

# ├── notebooks/              # Jupyter notebook

# ├── app.py                  # Streamlit dashboard

# └── main.py

# ```

# 

# \## Run Locally

# ```bash

# pip install -r requirements.txt

# python main.py

# streamlit run app.py

# ```

# 

# \## Results

# | Participant | Accuracy |

# |-------------|----------|

# | 038010\_EIT-2A | see notebook |

# | 038011\_EIT-1A | see notebook |

# | 038012\_EIT-2A | see notebook |

# | 038015\_EIT-1A | see notebook |

