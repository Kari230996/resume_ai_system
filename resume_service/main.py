from fastapi import FastAPI, UploadFile, File
from kafka import KafkaProducer
import json
import uuid

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    resume_id = str(uuid.uuid4())
    text = content.decode("utf-8", errors="ignore")

    resume_data = {
        "resume_id": resume_id,
        "text": text
    }

    producer.send("resumes", resume_data)
    producer.flush()

    return {"message": "Resume uploaded", "resume_id": resume_id}
