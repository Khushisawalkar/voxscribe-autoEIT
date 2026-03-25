import os
import librosa
import soundfile as sf

def split_audio(file_path, chunk_length=10):
    y, sr = librosa.load(file_path, sr=16000)

    chunk_samples = chunk_length * sr
    chunks = []

    output_dir = "data/chunks"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(0, len(y), chunk_samples):
        chunk = y[i:i + chunk_samples]
        filename = f"{output_dir}/chunk_{i}.wav"
        sf.write(filename, chunk, sr)
        chunks.append(filename)

    return chunks