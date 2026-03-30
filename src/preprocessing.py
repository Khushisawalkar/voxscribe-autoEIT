from pydub import AudioSegment
import os


def preprocess_audio(input_path):
    """
    Convert audio to WAV format and normalize it.
    """

    os.makedirs("data/processed", exist_ok=True)

    audio = AudioSegment.from_file(input_path)

    # Normalize audio (optional improvement)
    audio = audio.set_frame_rate(16000).set_channels(1)

    output_path = os.path.join(
        "data/processed",
        os.path.basename(input_path).replace(".mp3", ".wav")
    )

    audio.export(output_path, format="wav")

    return output_path