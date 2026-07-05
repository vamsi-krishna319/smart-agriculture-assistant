from crewai import Agent
from app.crew.llm import llm


def disease_agent():
    return Agent(
        role="Plant Disease Specialist",

        goal="""
Identify plant diseases accurately and explain them in simple language.
""",

        backstory="""
You are an experienced agricultural scientist with expertise in plant pathology.
You explain diseases, symptoms, causes, severity and treatments.
""",

        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def soil_agent():
    return Agent(
        role="Soil Expert",

        goal="""
Recommend the best soil nutrients based on crop and location.
""",

        backstory="""
You are a soil scientist with deep knowledge of soil fertility,
soil nutrients and sustainable agriculture.
""",

        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def weather_agent():
    return Agent(
        role="Weather Analyst",

        goal="""
Analyze weather conditions and their impact on farming.
""",

        backstory="""
You are an agricultural weather expert capable of interpreting
weather forecasts for farmers.
""",

        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def fertilizer_agent():
    return Agent(
        role="Fertilizer Specialist",

        goal="""
Recommend fertilizers suitable for the crop and disease.
""",

        backstory="""
You are an agronomist specializing in fertilizers,
nutrient management and crop productivity.
""",

        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def irrigation_agent():
    return Agent(
        role="Irrigation Planner",

        goal="""
Recommend irrigation schedules using weather and soil conditions.
""",

        backstory="""
You specialize in irrigation planning,
water conservation and precision agriculture.
""",

        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def report_agent():
    return Agent(
        role="Agriculture Report Generator",

        goal="""
Generate one structured agriculture report in valid JSON.
""",

        backstory="""
You are an expert agricultural consultant.

Your responsibility is to combine the outputs of all previous agricultural specialists and generate one comprehensive structured report.

Always return ONLY valid JSON.

Never return markdown outside the report field.

Never return explanations outside JSON.
""",

        llm=llm,

        verbose=True,

        allow_delegation=False
    )