from crewai import Task

from app.crew.agents import (
    disease_agent,
    soil_agent,
    weather_agent,
    fertilizer_agent,
    irrigation_agent,
    report_agent,
)


def create_tasks(
    crop_name: str,
    disease_name: str,
    confidence: float,
    location: str,
    weather_data: dict,
):
    disease = Task(
        description=f"""
Crop: {crop_name}

Detected Disease: {disease_name}

Confidence: {confidence:.2f}%

Explain:

- Disease Summary
- Symptoms
- Causes
- Severity
""",
        expected_output="""
A detailed disease explanation in markdown.
""",
        agent=disease_agent(),
    )

    soil = Task(
        description=f"""
Crop: {crop_name}

Location: {location}

Recommend:

- Suitable soil
- Nutrient deficiencies
- Soil improvement techniques
""",
        expected_output="""
Detailed soil recommendations.
""",
        agent=soil_agent(),
    )

    weather = Task(
    description=f"""
You are analyzing the current weather conditions for agricultural planning.

Crop: {crop_name}

Location: {location}

Current Weather:

Temperature: {weather_data.get("temperature")} °C

Humidity: {weather_data.get("humidity")} %

Pressure: {weather_data.get("pressure")} hPa

Weather Condition: {weather_data.get("weather")}

Description: {weather_data.get("description")}

Wind Speed: {weather_data.get("wind_speed")} m/s

Based on the above weather conditions, provide:

1. Is the current weather suitable for growing {crop_name}?
2. Possible risks to the crop.
3. Recommended farming precautions.
4. Expected impact on disease spread.
5. Irrigation considerations.
6. Best farming practices for the next few days.

Keep the explanation simple and practical for farmers.
""",
    expected_output="""
A detailed weather analysis including crop suitability,
possible risks, irrigation advice and farming recommendations.
""",
    agent=weather_agent(),
)

    fertilizer = Task(
        description=f"""
Crop: {crop_name}

Disease: {disease_name}

Recommend:

- Fertilizers
- Quantity
- Application timing
""",
        expected_output="""
Fertilizer recommendation.
""",
        agent=fertilizer_agent(),
    )

    irrigation = Task(
        description=f"""
Crop: {crop_name}

Weather:

Temperature: {weather_data.get("temperature")}

Rain Chance: {weather_data.get("rain")}

Recommend irrigation schedule.
""",
        expected_output="""
Watering schedule.
""",
        agent=irrigation_agent(),
    )

    report = Task(
    description="""
You are the final agriculture report generator.

Your job is to combine the outputs from all previous agents into ONE structured JSON object.

Return ONLY valid JSON.

Use the following schema exactly:

{
    "disease": "",
    "confidence": 0,
    "severity": "",
    "weather_advice": "",
    "soil_recommendation": "",
    "fertilizer": "",
    "irrigation": "",
    "prevention": "",
    "organic_treatment": "",
    "chemical_treatment": "",
    "report": ""
}

Rules:

1. report should be a detailed farmer-friendly markdown report.

2. confidence must be a number.

3. Return ONLY JSON.

4. Do NOT wrap JSON inside ```json blocks.

5. Do NOT add any explanation outside JSON.
""",
    expected_output="""
A valid JSON object containing the complete agriculture report.
""",
    agent=report_agent(),
    context=[
        disease,
        soil,
        weather,
        fertilizer,
        irrigation
    ]
)

    return [
        disease,
        soil,
        weather,
        fertilizer,
        irrigation,
        report,
    ]