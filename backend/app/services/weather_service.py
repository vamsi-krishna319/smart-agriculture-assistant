import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(location: str):

        params = {
            "q": location,
            "appid": os.getenv("OPENWEATHER_API_KEY"),
            "units": "metric"
        }

        response = requests.get(
            WeatherService.BASE_URL,
            params=params
        )

        response.raise_for_status()

        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }