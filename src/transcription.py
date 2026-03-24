import whisper

def load_model(model_size="base"):
    return whisper.load_model(model_size)

def transcribe_audio(model, file_path):
    result = model.transcribe(
        file_path,
        language="en",   # 🔥 force English
        task="transcribe"
    )
    return result["text"]