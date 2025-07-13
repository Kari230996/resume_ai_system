from fastapi import FastAPI, UploadFile, File
from kafka import KafkaProducer
import json
import uuid

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.post("/upload-jd/")
async def upload_jd(file: UploadFile = File(...)):
    content = await file.read()
    jd_id = str(uuid.uuid4())
    jd_text = content.decode("utf-8", errors="ignore")

    jd_data = {
        "jd_id": jd_id,
        "text": jd_text
    }

    producer.send("jds", jd_data)
    return {"message": "Job Description uploaded", "jd_id": jd_id}
