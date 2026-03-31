import pandas as pd
from core.matcher import find_best_match
from core.preprocessing import normalize
from core.scoring import compute_score

def evaluate(precomputed_results, references):
    all_rows = []
    summary = {}

    for participant, data in precomputed_results.items():
        total_wer, total_sim = 0, 0

        for ref in references:
            ref_clean = normalize(ref)
            best = find_best_match(ref_clean, data["sentences"])

            score = compute_score(best["wer"], best["sim"])

            total_wer += best["wer"]
            total_sim += best["sim"]

            all_rows.append({
                "Participant": participant,
                "Reference": ref,
                "Prediction": best["text"],
                "WER": best["wer"],
                "Similarity": best["sim"],
                "Score": score
            })

        avg_wer = total_wer / len(references)
        avg_sim = total_sim / len(references)
        summary[participant] = compute_score(avg_wer, avg_sim)

    return pd.DataFrame(all_rows), summary