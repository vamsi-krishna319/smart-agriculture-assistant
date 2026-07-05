from app.services.groq_service import ask_groq

response = ask_groq(
    "What disease causes yellow spots on rice leaves? Give a short answer."
)

print(response)