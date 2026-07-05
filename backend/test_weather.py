from app.services.weather_service import WeatherService

weather = WeatherService.get_weather("Hyderabad")

print(weather)