import sys

from src.segmentation import split_audio
from src.transcription import load_model, transcribe_audio
from src.postprocessing import clean_text, correct_errors
from src.eit_analysis import evaluate_eit
from src.database import init_db, save_run


def main(audio_path):
    # 🔥 Ensure DB exists
    init_db()

    print("Splitting audio...")
    chunks = split_audio(audio_path)

    print("Loading model...")
    model = load_model("base")

    full_text = ""

    for chunk in chunks:
        print(f"Transcribing {chunk}...")
        text = transcribe_audio(model, chunk)
        full_text += text + " "

    print("Post-processing...")
    cleaned = clean_text(full_text)
    cleaned = correct_errors(cleaned)

    print("\nFinal Output:")
    print(cleaned)

    # 🔥 EIT Evaluation
    reference_sentences = [
        "we drove to the park",
        "i will call her tomorrow night",
        "the book is on the table"
    ]

    results = evaluate_eit(reference_sentences, cleaned)

    print("\nEIT Evaluation:")
    for r in results:
        print(r)

    avg_wer = sum([r[1] for r in results]) / len(results)
    accuracy = 1 - avg_wer

    print(f"\nAccuracy: {accuracy}")

    # 🔥 Save to DB
    save_run(audio_path, accuracy, full_text, cleaned)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file>")
    else:
        main(sys.argv[1])