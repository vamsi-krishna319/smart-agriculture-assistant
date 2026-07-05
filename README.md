AgriIntel AI 🌾
A Multi-Agent Agricultural Advisory Platform

AgriIntel AI is an AI-powered agricultural advisory platform that helps farmers make informed decisions by combining crop disease detection with intelligent, multi-agent analysis. Built using CrewAI, the system coordinates multiple specialized AI agents to analyze crop images, evaluate environmental conditions, and generate practical recommendations for disease management and crop care.

The platform provides a seamless workflow where farmers can register, upload crop images, receive AI-powered insights, and download detailed reports containing personalized recommendations.

🚀 Features
👨‍🌾 Farmer Registration
📷 Crop Image Upload
🤖 AI-Powered Crop Disease Detection
🌦 Weather-Based Crop Advisory
🌱 Soil Recommendation
🌿 Fertilizer Recommendation
💧 Irrigation Recommendation
🛡 Disease Prevention Suggestions
🌿 Organic Treatment Recommendations
🧪 Chemical Treatment Recommendations
📄 AI-Generated PDF Reports



🏗️ System Architecture
AgriIntel AI follows a multi-agent architecture powered by CrewAI.
Each agent specializes in a specific agricultural task and collaborates to generate a comprehensive advisory report.
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
   ├── Disease Detection Agent
   ├── Weather Analysis Agent
   ├── Soil Recommendation Agent
   ├── Fertilizer Recommendation Agent
   ├── Irrigation Recommendation Agent
   ├── Treatment Recommendation Agent
   └── Report Generation Agent
   │
   ▼
Google Gemini


🤖 AI Agents
The platform consists of multiple specialized AI agents:
| Agent                   | Responsibility                                     |
| ----------------------- | -------------------------------------------------- |
| Disease Detection Agent | Identifies crop diseases from uploaded images      |
| Weather Agent           | Analyzes weather conditions affecting crop health  |
| Soil Agent              | Provides soil improvement recommendations          |
| Fertilizer Agent        | Suggests suitable fertilizers                      |
| Irrigation Agent        | Generates irrigation recommendations               |
| Treatment Agent         | Recommends organic and chemical treatments         |
| Report Agent            | Generates the final AI-powered agricultural report |


🛠 Tech Stack
Frontend
Streamlit
Backend
FastAPI
Uvicorn
AI Framework
CrewAI
CrewAI Tools
Large Language Model
Google Gemini
Database
SQLAlchemy
Additional Libraries
OpenCV
Pandas
Pillow
ReportLab
ChromaDB
Deployment
Render


📂 Project Structure
AgriIntel-AI/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── crew/
│   │   ├── agents/
│   │   ├── tasks/
│   │   ├── services/
│   │   ├── database/
│   │   ├── models/
│   │   └── main.py
│   │
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



🎯 Learning Outcomes
This project provided practical experience in:
Designing Multi-Agent AI Systems using CrewAI
Building REST APIs with FastAPI
Integrating Google Gemini into production workflows
Developing interactive web applications with Streamlit
Managing environment variables securely
Deploying full-stack AI applications on Render
Building real-world AI solutions for agriculture


🔮 Future Enhancements
Multi-language support
User authentication
Crop yield prediction
Pest detection
Market price forecasting
Satellite image integration
Voice-based farmer interaction
Mobile application
Historical analysis dashboard


