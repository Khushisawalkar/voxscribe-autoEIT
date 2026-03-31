import whisper

# Load model once
model = whisper.load_model("base")

def transcribe_audio(file_path):
    result = model.transcribe(file_path, language='es')
    return result['text']