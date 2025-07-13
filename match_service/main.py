from kafka_utils.consumer import get_kafka_consumer
import re

print("🚀 match_service started!")
consumer = get_kafka_consumer("resumes")

print("✅ Waiting for messages on topic 'resumes'...")


def clean_text(text: str) -> str:
    text = text.strip()

    text = re.sub(r'[^\x00-\x7Fа-яА-ЯёЁ\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text


skills_to_check = ["Python", "Kafka", "SQL", "FastAPI", "Django", "PostgreSQL"]

for msg in consumer:
    data = msg.value
    raw_text = data.get('text', '')
    clean = clean_text(raw_text)

    print("📥 New resume received:")
    print(f"ID: {data.get('resume_id')}")
    print(f"🧹 Cleaned Text (first 100 chars): {clean[:100]}...\n")

    found_skills = []
    for skill in skills_to_check:
        if skill.lower() in clean.lower():
            found_skills.append(skill)

    if found_skills:
        print("✅ Skills matched:", ", ".join(found_skills))
    else:
        print("⚠️ No matching skills found.")
    print("-" * 60)
