import whisper

model = None

def load_model(model_size="base"):
    global model
    print(f"Loading Whisper {model_size} model...")
    model = whisper.load_model(model_size)
    print("Model loaded!")
    return model

def transcribe_audio(audio_path, model_size="base"):
    global model
    if model is None:
        load_model(model_size)
    result = model.transcribe(
        audio_path,
        fp16=False,
        language="es",
        temperature=0.0,
        verbose=False
    )
    return result