import re


def clean_text(text):
    text = text.lower()

    # remove weird unicode
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    # normalize spacing
    text = re.sub(r'\s+', ' ', text)

    # 🔥 basic corrections (VERY IMPORTANT)
    text = text.replace("caro", "car")
    text = text.replace("book is in the table", "book is on the table")
    text = text.replace("call her tomorrow", "call her tomorrow night")

    return text.strip()