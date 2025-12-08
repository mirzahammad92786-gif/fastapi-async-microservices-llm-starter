# FastAPI + AsyncIO Microservices LLM Starter 🚀

A production-grade backend starter template built with **FastAPI**, **AsyncIO**, **PostgreSQL**, **Celery**, **Docker**, and optional **OpenAI/LLM integration**.  
Designed for scalable, high-performance systems with clean architecture and real-world patterns.

This boilerplate gives you:
- ⚡ High-speed APIs using FastAPI
- 🔄 Async processing using AsyncIO
- 🗃 PostgreSQL + SQLAlchemy for reliable data storage
- 🧵 Background processing with Celery + Redis
- 🔐 JWT authentication and role-based access
- 🤖 Optional OpenAI LLM workflows (embeddings, function-calling)
- 🐳 Full Docker Compose setup
- 🧱 Clean, production-ready folder structure

---

## 🚀 Features

### **1. FastAPI Microservices Architecture**
- Separate modules for auth, users, tasks, AI, and integrations  
- Dependency injection and router-level modularity  
- Automatic validation with Pydantic models  

### **2. Async-Powered Backend**
- Fully async FastAPI routes  
- Async SQL queries  
- Async external API calls  
- Async background pipelines  

### **3. PostgreSQL + SQLAlchemy**
- Models, migrations, and database session management  
- Query optimization patterns  
- Indexing and schema best practices  

### **4. Celery Task Queues**
- Background tasks for emails, analytics, data processing  
- Retries + structured logging  
- Async pipelines integrated with Redis/Broker  

### **5. Authentication**
- Secure JWT token system  
- Login, refresh tokens, password hashing  
- Role-based access control  

### **6. LLM / OpenAI Integration (Optional)**
- Function-calling API wrapper  
- Embeddings-based search using FAISS/Chroma  
- Prompt-based automation utilities  

---

## 🧱 Project Structure

fastapi-app/
│── app/
│ ├── api/
│ │ ├── auth/
│ │ ├── users/
│ │ ├── tasks/
│ │ └── ai/
│ ├── core/
│ │ ├── config.py
│ │ ├── security.py
│ │ └── logging.py
│ ├── db/
│ │ ├── session.py
│ │ ├── models.py
│ │ └── migrations/
│ ├── services/
│ ├── utils/
│ └── main.py
│── celery_worker/
│── docker-compose.yml
│── requirements.txt

yaml
Copy code

---

## 🐳 Docker Setup

docker-compose up --build

yaml
Copy code

This launches:
- FastAPI server  
- PostgreSQL  
- Redis  
- Celery worker  
- Celery beat (scheduled tasks)  

---

## ▶️ Running Locally

### Install dependencies
pip install -r requirements.txt

shell
Copy code

### Run API server
uvicorn app.main:app --reload

yaml
Copy code

---

## 🔬 LLM Integration Example (OpenAI)

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Summarize this text"}]
)

print(response.choices[0].message["content"])
