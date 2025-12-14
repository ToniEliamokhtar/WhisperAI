from fastapi import FastAPI, UploadFile, File
import whisper
import tempfile
import os

app = FastAPI()

model = whisper.load_model("base")

@app.get("/", response_class=FileResponse)
def root():
    # Retourne le fichier index.html situé dans /app (racine du projet dans le container)
    return "index.html"

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # 1. Sauvegarder l'audio reçu dans un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(await file.read())
        temp_path = temp_audio.name

    # 2. Transcription normale (langue d'origine)
    result = model.transcribe(temp_path)  # ex: texte en français
    original_text = result["text"]
    detected_language = result["language"]

    # 3. Traduction en anglais
    translated = model.transcribe(temp_path, task="translate")
    translated_text = translated["text"]

    # 4. Nettoyage
    os.remove(temp_path)

    # 5. Réponse JSON
    return {
        "filename": file.filename,
        "language": detected_language,
        "text_original": original_text,
        "text_english": translated_text
    }