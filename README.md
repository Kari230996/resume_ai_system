## 📄 Resume AI System

A resume processing service for HR specialists using microservices architecture, Kafka, and FastAPI. Users upload resumes and receive automatic recommendations based on text analysis.

---

### 🧠 Features

* 📤 Resume upload via API (`resume_service`)
* 📦 Data publishing to Kafka topic `resumes`
* 🤖 Resume processing and analysis (`match_service`)
* 📊 Recommendation generation based on key skills
* 🛠 Extensible architecture for AI agents

---

### ⚙️ Technologies

* Python 3.10
* FastAPI
* Kafka (`confluentinc/cp-kafka`)
* PostgreSQL
* Docker & Docker Compose
* kafka-python

---

### 🏗 Microservice Structure

```
resume_ai_system/
│
├── resume_service/      # Resume upload
├── match_service/       # Processing and analysis
├── jd_service/          # (Stub) Job description processing
├── docker-compose.yml   # Run the whole system
```

---

### 🚀 Running the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kari230996/resume_ai_system.git
   cd resume_ai_system
   ```

2. **Create `.env` for PostgreSQL**

   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=resume_db
   ```

3. **Build and start services**

   ```bash
   docker-compose up --build
   ```

---

### 🧪 API Request Examples

#### 📤 Upload a Resume

```bash
curl -X POST http://localhost:8001/upload-resume/ \
  -H "accept: application/json" \
  -F "file=@example_resume.txt"
```

---

### 🔄 Kafka Flow

1. `resume_service` publishes data to Kafka (`resumes`)
2. `match_service` consumes and processes incoming resumes
3. Results are displayed in the console

---

### 🗃 Example Output

```
🚀 match_service started!
✅ Waiting for messages on topic 'resumes'...
📥 New resume received:
ID: d950c24d-9c3f-47c9-9efb-c31f6eda5a5c
🧹 Cleaned Text (first 100 chars): "...Python, Kafka, SQL..."
✅ Skills matched: Python, Kafka, SQL
------------------------------------------------------------
```

---

### 📌 Extension Possibilities

* Adding AI module (e.g., LLM)
* Connecting job descriptions for matching
* Storing in PostgreSQL with analytics

---

### 📬 Contacts

**Karina Apaeva**
Email: [karina.apaeva96@gmail.com](mailto:karina.apaeva96@gmail.com)

---
