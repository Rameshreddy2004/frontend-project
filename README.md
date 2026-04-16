# 🚀 AI Prompt Management System

A full-stack backend system for managing AI prompts, built using **Django, PostgreSQL, Redis, and Docker**.
This project provides REST APIs for creating, retrieving, and deleting prompts, along with a real-time view counter using Redis.

---

## 🧠 Features

* 📌 Create AI prompts
* 📄 Retrieve all prompts
* 🔍 Retrieve a single prompt
* ❌ Delete prompts
* ⚡ Real-time view counter using Redis
* 🐳 Dockerized multi-container setup

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **Database:** PostgreSQL
* **Cache:** Redis
* **Containerization:** Docker & Docker Compose

---

## 📂 Project Structure

```
ai_prompt_pro_ready/
│
├── backend/
│   ├── prompts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   ├── backend/
│   │   └── settings.py
│   └── manage.py
│
├── frontend/
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd ai_prompt_pro_ready
```

---

### 2️⃣ Run with Docker

```
docker compose up --build
```

---

### 3️⃣ Run migrations

```
docker exec -it ai_prompt_pro_ready-backend-1 bash
python manage.py migrate
```

---

## 🌐 API Endpoints

### 🔹 Get all prompts

```
GET /prompts/
```

---

### 🔹 Create a prompt

```
POST /prompts/
```

**Body:**

```json
{
  "title": "Cyberpunk City",
  "content": "A futuristic neon-lit city with flying cars and AI robots.",
  "complexity": 5
}
```

---

### 🔹 Get single prompt (with views counter)

```
GET /prompts/<id>/
```

**Response:**

```json
{
  "id": "...",
  "title": "...",
  "views": 1
}
```

---

### 🔹 Delete prompt

```
DELETE /prompts/<id>/delete/
```

---

## ⚡ Redis View Counter

Each time a prompt is accessed:

* View count is incremented in Redis
* No database load is added
* Provides fast, real-time tracking

---

## 🐳 Docker Services

* **backend** → Django API
* **db** → PostgreSQL database
* **redis** → caching & counters
* **frontend** → UI (optional)

---

## 🧪 Testing

You can test APIs using:

* Postman
* Browser (GET requests)

---

## 💼 Resume Description

> Developed a Dockerized backend system using Django, PostgreSQL, and Redis. Implemented REST APIs with full CRUD functionality and optimized performance using Redis-based view tracking.

---

## 🚀 Future Improvements

* ✏️ Update API
* 🔐 Authentication (JWT)
* 🌍 Deployment (Render / AWS)
* 🎨 Frontend integration

---

## 👨‍💻 Author

**Ramesh Reddy**

---

## 📌 License

This project is for learning and demonstration purposes.
