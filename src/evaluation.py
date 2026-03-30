from jiwer import wer
from rapidfuzz import fuzz


def evaluate_eit(sentences):
    """
    Improved evaluation using:
    - WER (professional metric)
    - Fuzzy matching (handles learner variation)
    """

    reference_sentences = [
        "we drove to the park",
        "i will call her tomorrow night",
        "we can buy meat at the butcher shop",
        "my brother just bought a brand new computer",
        "sometimes they take their dog for a walk in the park",
        "we are going to play volleyball at the gym that i told you about",
        "i want to cut my hair",
        "the book is on the table"
    ]

    total_wer = 0
    total_similarity = 0

    print("\n📊 Sentence-level Evaluation:\n")

    for ref in reference_sentences:
        best_wer = 1.0
        best_pred = ""
        best_sim = 0

        for pred in sentences:
            current_wer = wer(ref, pred)
            similarity = fuzz.ratio(ref, pred) / 100

            # choose best based on similarity + wer
            if similarity > best_sim:
                best_sim = similarity
                best_wer = current_wer
                best_pred = pred

        total_wer += best_wer
        total_similarity += best_sim

        print(f"REF : {ref}")
        print(f"PRED: {best_pred}")
        print(f"WER : {best_wer:.2f}")
        print(f"SIM : {best_sim:.2f}\n")

    avg_wer = total_wer / len(reference_sentences)
    avg_sim = total_similarity / len(reference_sentences)

    # 🔥 FINAL ACCURACY (HYBRID)
    accuracy = ((1 - avg_wer) * 0.7 + avg_sim * 0.3) * 100

    print(f"📉 Average WER: {avg_wer:.2f}")
    print(f"📊 Avg Similarity: {avg_sim:.2f}")
    print(f"🎯 Final Accuracy: {accuracy:.2f}%")

    return accuracy