import re

def clean_text(text):
    """
    Cleans ASR output.
    Corrects only ASR errors — preserves learner grammar/vocabulary errors.
    """
    text = text.lower()
    # Remove non-ASCII unicode artifacts
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_sentences(result):
    """Extract clean sentences from Whisper result segments."""
    sentences = []
    for seg in result['segments']:
        text = seg['text'].strip()
        if text:
            sentences.append(text)
    return sentences