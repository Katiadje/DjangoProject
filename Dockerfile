# Utiliser une image python officielle
FROM python:3.11-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier les fichiers requirements.txt (si tu en as un) et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de ton projet dans le container
COPY . /app/

# Exposer le port sur lequel Django va tourner (par défaut 8000)
EXPOSE 8000

# Commande pour lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    