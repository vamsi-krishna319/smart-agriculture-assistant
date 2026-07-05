import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

# llm = LLM(
#     model="groq/llama-3.3-70b-versatile",
#     api_key=os.getenv("GROQ_API_KEY"),
#     temperature=0.2,
# )

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.2,
)