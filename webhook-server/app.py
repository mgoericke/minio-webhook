from flask import Flask, request
from minio import Minio
from minio.commonconfig import CopySource
import logging

app = Flask(__name__)

# MinIO-Client initialisieren
client = Minio(
    "minio:9000",  # Ersetzen Sie dies durch Ihren MinIO-Server-Endpunkt
    access_key="aumpB204wspLZO3w2RND",
    secret_key="mHXwzhY5ZziL33qqYPuAaHdTkh56Oms2WHeDU5Ay",
    secure=False  # Setzen Sie dies auf True, wenn Sie HTTPS verwenden
)
# Log-Level auf INFO setzen
app.logger.setLevel(logging.INFO)

@app.route('/webhook', methods=['POST'])
def handle_minio_event():
    event = request.json
    app.logger.info("MinIO Event empfangen: %s", event)

    # Extrahieren der relevanten Informationen aus dem Event
    bucket = event['Records'][0]['s3']['bucket']['name']
    #object_key = event['Records'][0]['s3']['object']['key']
    object_key = event['Records'][0]['s3']['object']['key']    
    new_object_key = "zweiter-pfad/" + object_key.split("/")[-1]

    app.logger.info("bucket: %s", bucket)
    app.logger.info("object_key: %s", object_key)
    app.logger.info("new_object_key: %s", new_object_key)

    # Kopieren des Objekts mit dem MinIO Python SDK
    try:
        copy_source = CopySource(bucket, object_key)
        client.copy_object(bucket, new_object_key, copy_source)
        print(f"Objekt erfolgreich von {object_key} nach {new_object_key} kopiert.")
    except Exception as err:
        print(f"Fehler beim Kopieren des Objekts: {err}")
        app.logger.error("Fehler beim Kopieren des Objekts: %s", err)
        return "Fehler", 500

    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)