from jiwer import wer

def evaluate_eit(reference_sentences, predicted_text):
    results = []

    for ref in reference_sentences:
        score = wer(ref, predicted_text)
        results.append((ref, round(score * 100, 2)))

    return results