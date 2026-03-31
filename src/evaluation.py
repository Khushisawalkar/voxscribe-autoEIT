from rapidfuzz import fuzz

REFERENCE_SENTENCES = [
    "we drove to the park",
    "i will call her tomorrow night",
    "we can buy meat at the butcher shop",
    "my brother just bought a brand new computer",
    "sometimes they take their dog for a walk in the park",
    "we are going to play volleyball at the gym that i told you about",
    "i want to cut my hair",
    "the book is on the table",
    "las calles de esta ciudad son muy anchas",
    "puede que llueva manana todo el dia",
    "las casas son muy bonitas pero caras",
    "me gustan las peliculas que acaban bien",
    "despues de cenar me fui a dormir tranquilo",
    "quiero una casa en la que vivan animales",
]

def evaluate_eit(sentences, participant_id=""):
    """
    Applies meaning-based rubric to EIT transcriptions.
    Scores each learner utterance against reference sentences.
    Returns accuracy score and per-sentence details.
    """
    total_sim = 0
    rows = []

    for ref in REFERENCE_SENTENCES:
        best_sim, best_pred = 0, ""
        for pred in sentences:
            p = pred.lower().strip()
            if not p:
                continue
            s = fuzz.ratio(ref, p) / 100
            if s > best_sim:
                best_sim, best_pred = s, pred

        total_sim += best_sim
        score = max(0, min(100, best_sim * 100))
        rows.append({
            "Participant": participant_id,
            "Reference Sentence": ref,
            "Learner Utterance": best_pred,
            "Similarity": round(best_sim, 3),
            "Score (%)": round(score, 2)
        })

    final_score = (total_sim / len(REFERENCE_SENTENCES)) * 100
    return round(final_score, 2), rows