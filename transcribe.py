import whisper

# 1. Charger le modèle Whisper
model = whisper.load_model("base")

# 2. Transcrire le fichier audio
result = model.transcribe("audio/normalEnglish.wav")

# 3. Afficher le texte transcrit
print(result["text"])