import whisper

model = whisper.load_model("base")


def transcribe_audio(audio_path):
    result = model.transcribe(
        audio_path,
        fp16=False,
        language="en",
        temperature=0.2,       # 🔥 more stable output
        beam_size=5            # 🔥 better decoding
    )

    return result["text"]