from jiwer import wer
from rapidfuzz import fuzz
from core.config import WER_WEIGHT, SIM_WEIGHT

def compute_metrics(ref, pred):
    return wer(ref, pred), fuzz.ratio(ref, pred) / 100

def compute_score(w, s):
    return max(0, ((1 - w) * WER_WEIGHT + s * SIM_WEIGHT)) * 100