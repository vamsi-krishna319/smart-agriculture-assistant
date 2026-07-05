import os
import json
from PIL import Image
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiService:

    @staticmethod
    def detect_disease(image_path: str,crop_name: str):

        image = Image.open(image_path)

        prompt = """
You are an expert agricultural plant pathologist.
The farmer has identified this crop as:

Crop:
{crop_name}

Analyze the uploaded image.

If the image matches the crop,
continue the analysis.

If it does not,
mention that the uploaded image
doesn't appear to match the crop.

Return ONLY valid JSON.

Schema:

{
    "crop": "",
    "disease": "",
    "confidence": 0,
    "is_healthy": false,
    "symptoms": [],
    "severity": ""
}

Rules:

- confidence must be between 0 and 100
- symptoms must be a JSON array
- severity must be Low, Medium or High
- Return JSON only.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, image]
        )

        text = response.text.strip()

        # Remove markdown code fences if Gemini returns them
        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)