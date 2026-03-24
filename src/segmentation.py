import librosa
import soundfile as sf
import os

def split_audio(input_path, output_dir="data/chunks"):
    os.makedirs(output_dir, exist_ok=True)

    audio, sr = librosa.load(input_path, sr=16000)

    chunk_length = 30 * sr   # 30 seconds

    chunks = []
    count = 0

    for i in range(0, len(audio), chunk_length):
        chunk = audio[i:i+chunk_length]
        filename = f"{output_dir}/chunk_{count}.wav"

        sf.write(filename, chunk, sr)
        chunks.append(filename)

        count += 1

    return chunks