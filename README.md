# 🌾 AgriIntel AI

### AI-Powered Multi-Agent Agricultural Advisory Platform

AgriIntel AI is an intelligent agricultural advisory platform built using **CrewAI** and **Google Gemini**. It leverages a multi-agent architecture to analyze crop images, identify plant diseases, evaluate environmental conditions, and provide personalized recommendations to support farmers in making informed decisions.

---

## ✨ Key Features

- 👨‍🌾 Farmer Registration
- 📷 Crop Image Upload
- 🤖 AI-Based Crop Disease Detection
- 🌦 Weather Analysis & Advisory
- 🌱 Soil Recommendations
- 🌿 Fertilizer Suggestions
- 💧 Irrigation Planning
- 🛡 Disease Prevention Tips
- 🌿 Organic Treatment Recommendations
- 🧪 Chemical Treatment Suggestions
- 📄 AI-Generated PDF Reports

---

# 🏗️ Architecture

```text
                Farmer
                   │
                   ▼
         Streamlit Frontend
                   │
                   ▼
           FastAPI Backend
                   │
                   ▼
          CrewAI Orchestrator
                   │
    ┌──────────────┼──────────────┐
    │              │              │
 Disease      Weather         Soil
  Agent        Agent          Agent
    │              │              │
 Fertilizer   Irrigation    Treatment
    Agent        Agent         Agent
                   │
                   ▼
           Report Generator
                   │
                   ▼
            Google Gemini
```

---

# 🤖 AI Agents

| Agent | Responsibility |
|-------|----------------|
| 🦠 Disease Detection Agent | Identifies crop diseases from uploaded images |
| 🌦 Weather Agent | Analyzes weather conditions |
| 🌱 Soil Agent | Recommends soil improvements |
| 🌿 Fertilizer Agent | Suggests suitable fertilizers |
| 💧 Irrigation Agent | Provides irrigation advice |
| 🛡 Treatment Agent | Recommends prevention and treatments |
| 📄 Report Agent | Generates the final AI report |

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI, Uvicorn |
| **AI Framework** | CrewAI, CrewAI Tools |
| **LLM** | Google Gemini |
| **Database** | SQLAlchemy |
| **Libraries** | OpenCV, Pillow, Pandas, ReportLab, ChromaDB |
| **Deployment** | Render |

---

# 📂 Project Structure

```text
AgriIntel-AI
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── pages/
│   ├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── uploads/
├── reports/
├── README.md
└── LICENSE
```

---

# 🎯 What I Learned

- Designing Multi-Agent AI workflows with CrewAI
- Building REST APIs using FastAPI
- Integrating Google Gemini into production applications
- Developing interactive interfaces with Streamlit
- Deploying AI applications on Render
- Managing environment variables securely
- Debugging deployment and API integration issues

---

# 🚀 Future Enhancements

- 🌍 Multi-language Support
- 🔐 User Authentication
- 📈 Crop Yield Prediction
- 🐛 Pest Detection
- 💹 Market Price Forecasting
- 🛰 Satellite Image Integration
- 🎙 Voice-Based Farmer Assistance
- 📱 Mobile Application
- 📊 Historical Analytics Dashboard

---



---

## ⭐ If you found this project useful, consider giving it a Star!
