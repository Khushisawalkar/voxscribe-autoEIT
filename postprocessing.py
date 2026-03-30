import re


def clean_text(text):
    # 🔥 LIGHT CLEANING ONLY (important)
    
    # remove weird unicode junk
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    # normalize spacing
    text = re.sub(r'\s+', ' ', text)

    return text.strip()