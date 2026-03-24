from jiwer import wer

def evaluate_eit(reference_sentences, hypothesis):
    hypothesis_sentences = hypothesis.split(".")

    results = []

    for ref in reference_sentences:
        best_error = 1.0

        for hyp in hypothesis_sentences:
            hyp = hyp.strip()
            if hyp:
                error = wer(ref, hyp)
                best_error = min(best_error, error)

        results.append((ref, best_error))

    return results