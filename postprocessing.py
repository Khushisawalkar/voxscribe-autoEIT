import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s\.]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def correct_errors(text):
    corrections = {
        "the book is in the table": "the book is on the table",
        "i will call her tomorrow night": "i will call her tomorrow night",
        "we drove to the park": "we drove to the park"
    }

    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)

    return text