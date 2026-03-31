import os

def preprocess_audio(file_path):
    """
    Validates and prepares audio file for transcription.
    Future: noise reduction, normalization, resampling.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    return file_path