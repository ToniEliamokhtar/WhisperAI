from fastapi import FastAPI, UploadFile, File
import whisper
import tempfile
import os

app = FastAPI()

model = whisper.load_model("base")

@app.get("/")
def root():
    return {"message": "Backend Whisper OK"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # On crée un fichier temporaire pour stocker l'audio uploadé
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(await file.read())
        temp_path = temp_audio.name

    # Transcription
    result = model.transcribe(temp_path)

    # Nettoyage pour la gestion de mémoire
    os.remove(temp_path)

    return {
        "filename": file.filename,
        "text": result["text"]
    }