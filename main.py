import os
import re
from src.preprocessing import preprocess_audio
from src.transcription import transcribe_audio
from src.postprocessing import clean_text
from src.database import init_db, save_run


def process_audio(audio_path):
    print(f"\n🎧 Processing: {audio_path}")

    processed_audio = preprocess_audio(audio_path)

    print("⚙️ Transcribing audio...")

    # 🔥 FULL AUDIO (NO CHUNKS)
    full_text = transcribe_audio(processed_audio)

    # Light cleaning only
    cleaned = clean_text(full_text)

    # 🔥 REALISTIC SENTENCE SPLIT
    raw_sentences = re.split(r'[.!?]+', cleaned)
    sentences = []

    for s in raw_sentences:
        s = s.strip()

        # keep realistic sentences
        if len(s) < 5:
            continue
        if len(s.split()) < 3:
            continue

        # remove extreme garbage only
        if len(s) > 150:
            continue

        sentences.append(s)

    # limit to 30 (test requirement)
    sentences = sentences[:30]

    print("\n📜 Realistic Transcription:\n")
    for i, s in enumerate(sentences):
        print(f"{i+1}. {s}")

    # 🔥 SIMPLE MATCH-BASED EVALUATION
    reference = [
        "we drove to the park",
        "i will call her tomorrow night",
        "we can buy meat at the butcher shop",
        "my brother just bought a brand new computer",
        "sometimes they take their dog for a walk in the park",
        "we are going to play volleyball",
        "i want to cut my hair",
        "the book is on the table"
    ]

    matches = 0

    for ref in reference:
        for pred in sentences:
            if ref.lower() in pred.lower():
                matches += 1
                break

    accuracy = matches / len(reference)

    print(f"\n🎯 Accuracy: {accuracy:.2f}")

    save_run(audio_path, accuracy, full_text, cleaned)

    return accuracy


if __name__ == "__main__":
    init_db()

    data_folder = "data"
    results = []

    for file in os.listdir(data_folder):
        if file.endswith(".mp3") or file.endswith(".wav"):
            path = os.path.join(data_folder, file)
            acc = process_audio(path)
            results.append((file, acc))

    print("\n🔥 FINAL SUMMARY:")
    for r in results:
        print(r)