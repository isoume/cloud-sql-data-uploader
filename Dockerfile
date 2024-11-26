# Utiliser une image de base
FROM python:3.8-slim

# Copier les fichiers du site dans le conteneur
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY main.py /app/main.py
CMD ["python", "main.py"]