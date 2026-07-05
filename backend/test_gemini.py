from app.services.gemini_service import GeminiService

result = GeminiService.detect_disease(
    "uploads/images.jpg"
)

print(result)