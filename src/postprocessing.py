def clean_text(text):
    text = text.lower()

    words = text.split()
    cleaned = []

    for i, w in enumerate(words):
        # remove duplicates
        if i > 0 and w == words[i-1]:
            continue

        # remove filler words
        if w in ["um", "uh", "ah"]:
            continue

        cleaned.append(w)

    return " ".join(cleaned)


COMMON_ERRORS = {
    "in the table": "on the table",
    "the baby have die": "the baby has died",
    "yo gusta": "me gusta",
}


def correct_errors(text):
    for wrong, correct in COMMON_ERRORS.items():
        text = text.replace(wrong, correct)
    return text