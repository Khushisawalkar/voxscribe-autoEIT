from jiwer import wer

def calculate_wer(reference, prediction):
    return wer(reference, prediction)