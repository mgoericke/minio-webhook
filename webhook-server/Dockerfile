FROM python:3.9-slim

# Installiere notwendige Pakete
RUN apt-get update && apt-get install -y wget

# Installiere MinIO Client (mc)
RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc \
    && chmod +x mc \
    && mv mc /usr/local/bin/

# Erstelle Arbeitsverzeichnis
WORKDIR /app

# Kopiere Applikationscode
COPY app.py /app

# Installiere Python-Abhängigkeiten
RUN pip install flask  minio

# Exponiere Port für den Webhook-Service
EXPOSE 5000

# Starte die Flask-Anwendung
CMD ["python", "app.py"]