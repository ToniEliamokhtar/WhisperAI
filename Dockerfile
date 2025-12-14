FROM python:3.10-slim

# 1. Dépendances système (ffmpeg = obligatoire pour Whisper)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
 && rm -rf /var/lib/apt/lists/*

# 2. Dossier de travail
WORKDIR /app

# 3. Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. On laisse le container démarrer dans /app avec un shell
CMD ["bash"]