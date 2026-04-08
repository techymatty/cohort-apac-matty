# 🚀 Multi-Agent Productivity Assistant (Google ADK + Cloud)

## 📌 Overview

This project is a **Multi-Agent AI Productivity Assistant** built using **Google Agent Development Kit (ADK)** and **Google Cloud Datastore**.

It demonstrates how multiple AI agents can collaborate to manage:

* ✅ Tasks
* 📅 Calendar Events
* 📝 Notes

The system uses a **planner + sub-agent architecture** to handle real-world workflows.

---

## 🎯 Problem Statement

Build a multi-agent AI system that:

* Coordinates between multiple agents
* Stores and retrieves structured data
* Integrates tools (tasks, notes, calendar)
* Handles multi-step workflows
* Deploys as an API-based system

---

## 🧠 Architecture

```
User Input
   ↓
Root Agent
   ↓
Planner Agent (Decision Maker)
   ↓
-------------------------------------
| Task Agent | Notes Agent | Calendar Agent |
-------------------------------------
   ↓
Response Agent (Final Output)
   ↓
User Response
```

---

## ⚙️ Tech Stack

* **Google ADK (Agent Development Kit)**
* **Python 3.11**
* **Google Cloud Datastore**
* **Cloud Run (for deployment)**
* **FastAPI (optional API layer)**

---

## 🧩 Features

* 🧠 Multi-agent coordination
* 🛠 Tool-based execution
* ☁️ Cloud-native database (Datastore)
* 🔄 Multi-step workflow handling
* 📡 API-ready architecture

---

## 📂 Project Structure

```
project/
│── main.py
│── requirements.txt
│── Dockerfile
│── .env
```

---

## 🔧 Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/your-username/multi-agent-assistant.git
cd multi-agent-assistant
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment

Create `.env` file:

```env
MODEL=your-model-name
```

---

### 4. Enable Google Cloud Services

```bash
gcloud services enable datastore.googleapis.com
```

---

### 5. Run Locally

```bash
python main.py
```

---

## ☁️ Deployment (Cloud Run)

### Build Image

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ai-agent
```

### Deploy

```bash
gcloud run deploy productivity-agent \
  --image gcr.io/YOUR_PROJECT_ID/ai-agent \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated
```

---

## 🧪 Example Usage

### ➤ Create Task

```
add a task to finish report
```

### ➤ Schedule Event

```
schedule meeting at 4 PM Friday
```

### ➤ Add Note

```
note: buy groceries
```

### ➤ List Tasks

```
list tasks
```

---

## 🔄 Workflow Example

**Input:**

```
add a task to prepare slides and schedule meeting tomorrow
```

**Output:**

```
Task 'prepare slides' created successfully.
Event scheduled for tomorrow.
```

---

## 🚧 Challenges Faced

* Managing agent state (`USER_INPUT`)
* Handling missing context variables
* Correct response rendering in ADK UI
* Tool orchestration across multiple agents

---

## ✅ Key Learnings

* Multi-agent coordination design
* State management in ADK
* Tool-based execution patterns
* Cloud-native AI system deployment

---

## 🔥 Future Improvements

* 🔗 Google Calendar API integration
* 🧠 NLP-based time parsing ("tomorrow 5 PM")
* 👤 Multi-user authentication
* 📊 SaaS dashboard (Next.js)
* ⏰ Background reminder system

---

## 👨‍💻 Author

**MD Mati Uddin**
Senior Software Engineer | AI Builder

---

## ⭐ Contribute

Feel free to fork, improve, and submit PRs 🚀

---

## 📜 License

MIT License
