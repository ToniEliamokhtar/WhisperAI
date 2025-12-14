# Atelier Whisper AI

Ceci est l'atelier de Whisper AI, un réseau de neurones capable de faire de la reconnaissance vocale (transcription, traduction et détection de la langue), réalisé par moi, Toni Eliamokhtar. 

Dans cet atelier, je vais démontrer comment installer Whisper AI dans une application backend, puis frontend, et comment l'utiliser.

Info : J'avais fait l'application sans la mettre sur Git, ce pourquoi je la refais maintenant avec des branches et des commits pour la remettre proprement.
       Je ne vais rien changer à ce que j'avais fait dans le site, je vais la refaire exactement de la même façon.

Je vais refaire une autre application plus avancée que celle là, juste pour vous donner quelque chose de plus.





!!!!

docker run -it --rm -p 8000:8000 -v "$(pwd)":/app whisper-atelier \
uvicorn app:app --host 0.0.0.0 --port 8000

Par rapport à cette commande, il faut savoir que le \ avant uvicorn est seulement pour faire un "saut de ligne", ou en d'autre mots c'est pour dire qu'on continue la commande sur la deuxième ligne. La raison pourquoi je l'ai écrit comme ça partout dans l'atelier est que j'avais mon VSCode ouvert sur une demi page seulement, donc vscode mettait le \ automatiquement. De même sur le site, la commande n'entrait jamais sur une seule ligne, ce pourquoi je l'ai mis sur deux lignes.

Si vous voulez l'écrire sur une seule ligne, il faut enlever le \ et l'écrire de cette façon :
docker run -it --rm -p 8000:8000 -v "$(pwd)":/app whisper-atelier uvicorn app:app --host 0.0.0.0 --port 8000

!!!!