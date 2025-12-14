from fastapi import FastAPI, UploadFile, File
import whisper
import tempfile
import os
from fastapi.responses import FileResponse

app = FastAPI()

model = whisper.load_model("base")

@app.get("/")
def root():
    return FileResponse("index.html")


@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_path = None

    try:
        # 1) Sauvegarder l'audio dans un fichier temporaire
        suffix = os.path.splitext(file.filename)[1] if file.filename else ".tmp"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_audio:
            temp_audio.write(await file.read())
            temp_path = temp_audio.name

        # 2) Transcription (langue d'origine)
        result = model.transcribe(temp_path)
        original_text = result["text"]
        detected_language = result["language"]

        # 3) Traduction en anglais
        translated = model.transcribe(temp_path, task="translate")
        translated_text = translated["text"]

        # 4) Réponse JSON
        return {
            "filename": file.filename,
            "language": detected_language,
            "text_original": original_text,
            "text_english": translated_text
        }

    finally:
        # 5) Nettoyage (même si ça plante)
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)