import os
import pandas as pd
from src.preprocessing import preprocess_audio
from src.segmentation import segment_audio
from src.transcription import transcribe_audio
from src.postprocessing import clean_text, extract_sentences
from src.evaluation import evaluate_eit
from src.database import init_db, save_run

AUDIO_DIR = "data/processed"
RESULTS_DIR = "results"

def main():
    init_db()
    os.makedirs(RESULTS_DIR, exist_ok=True)

    audio_files = [f for f in os.listdir(AUDIO_DIR)
                   if f.endswith(".wav") or f.endswith(".mp3")]

    all_rows = []
    all_scores = {}

    for audio_file in sorted(audio_files):
        audio_path = os.path.join(AUDIO_DIR, audio_file)
        name = audio_file.replace(".wav","").replace(".mp3","")

        print(f"\n{'='*55}")
        print(f"Processing: {name}")
        print('='*55)

        # Pipeline
        processed = preprocess_audio(audio_path)
        chunks = segment_audio(processed)
        result = transcribe_audio(chunks[0])
        sentences = extract_sentences(result)
        cleaned = clean_text(result["text"])

        # Evaluate
        accuracy, rows = evaluate_eit(sentences, participant_id=name)
        all_rows.extend(rows)
        all_scores[name] = accuracy

        # Save
        save_run(name, accuracy, result["text"], cleaned)

        out_path = os.path.join(RESULTS_DIR, f"{audio_file}_output.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            for i, s in enumerate(sentences, 1):
                f.write(f"{i}. {s}\n")

        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Saved: {out_path}")

    # Save scores CSV
    df = pd.DataFrame(all_rows)
    df.to_csv(os.path.join(RESULTS_DIR, "sentence_scores.csv"), index=False)

    print(f"\n{'='*55}")
    print("FINAL RESULTS")
    print('='*55)
    for name, score in all_scores.items():
        print(f"  {name:<25} -> {score:.2f}%")
    avg = sum(all_scores.values()) / len(all_scores)
    print(f"  {'AVERAGE':<25} -> {avg:.2f}%")
    print(f"\nAll results saved to {RESULTS_DIR}/")

if __name__ == "__main__":
    main()