import json

from crewai import Crew, Process

from app.crew.agents import (
    disease_agent,
    soil_agent,
    weather_agent,
    fertilizer_agent,
    irrigation_agent,
    report_agent
)

from app.crew.tasks import create_tasks


def run_agriculture_crew(
    crop_name: str,
    disease_name: str,
    confidence: float,
    location: str,
    weather_data: dict
):

    agents = [
        disease_agent(),
        soil_agent(),
        weather_agent(),
        fertilizer_agent(),
        irrigation_agent(),
        report_agent()
    ]

    tasks = create_tasks(
        crop_name=crop_name,
        disease_name=disease_name,
        confidence=confidence,
        location=location,
        weather_data=weather_data
    )

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    result = str(result)

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)