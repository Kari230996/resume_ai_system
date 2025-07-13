
---

## 📄 Resume AI System

Сервис обработки резюме для HR-специалистов с использованием микросервисной архитектуры, Kafka и FastAPI. Пользователь загружает резюме и получает автоматические рекомендации на основе анализа текста.

---

### 🧠 Функциональность

* 📤 Загрузка резюме через API (`resume_service`)
* 📦 Передача данных в Kafka-топик `resumes`
* 🤖 Обработка и анализ резюме (`match_service`)
* 📊 Подготовка рекомендаций на основе ключевых навыков
* 🛠 Расширяемая архитектура под AI-агентов

---

### ⚙️ Технологии

* Python 3.10
* FastAPI
* Kafka (`confluentinc/cp-kafka`)
* PostgreSQL
* Docker & Docker Compose
* kafka-python

---

### 🏗 Структура микросервисов

```
resume_ai_system/
│
├── resume_service/      # Загрузка резюме
├── match_service/       # Обработка и анализ
├── jd_service/          # (Заглушка) обработка job description
├── docker-compose.yml   # Запуск всей системы
```

---

### 🚀 Запуск проекта

1. **Клонировать репозиторий**

   ```bash
   git clone https://github.com/Kari230996/resume_ai_system.git
   cd resume_ai_system
   ```

2. **Создать `.env` для PostgreSQL**

   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=resume_db
   ```

3. **Собрать и запустить**

   ```bash
   docker-compose up --build
   ```

---

### 🧪 Примеры запросов

#### 📤 Загрузка резюме

```bash
curl -X POST http://localhost:8001/upload-resume/ \
  -H "accept: application/json" \
  -F "file=@example_resume.txt"
```

---

### 🔄 Kafka-поток

1. `resume_service` публикует данные в Kafka (`resumes`)
2. `match_service` подписан и обрабатывает входящие резюме
3. В консоли выводится результат анализа

---

### 🗃 Пример вывода

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

### 📌 Возможности для расширения

* Добавление AI-модуля (например, LLM)
* Подключение job description и сравнение
* Хранение в PostgreSQL и аналитика

---

### 📬 Контакты

**Карина Апаева**
Email: [karina.apaeva96@gmail.com](mailto:karina.apaeva96@gmail.com)

---


