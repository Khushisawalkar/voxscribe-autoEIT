from core.preprocessing import normalize
from core.scoring import compute_metrics
from core.config import SIM_THRESHOLD, WER_THRESHOLD
import langid

def safe_detect(text):
    try:
        return langid.classify(text)[0]
    except:
        return "unknown"

def find_best_match(reference, predictions):
    best = {"wer":1, "sim":0, "text":"", "score":0}
    ref_lang = safe_detect(reference)

    for pred in predictions:
        p = normalize(pred)

        if safe_detect(p) != ref_lang:
            continue

        w, s = compute_metrics(reference, p)

        if s < SIM_THRESHOLD or w > WER_THRESHOLD:
            continue

        combined = (1 - w)*0.6 + s*0.4

        if combined > best["score"]:
            best = {"wer":w, "sim":s, "text":pred, "score":combined}

    if best["text"] == "":
        return {"wer":1, "sim":0, "text":"[NO MATCH]"}

    return best