import requests, os

def get_weather(city: str) -> str:
    api_key = os.getenv("002027d12056457382391908251612")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()

    return f"""
    Temperature: {data['main']['temp']}°C
    Weather: {data['weather'][0]['main']}
    Humidity: {data['main']['humidity']}%
    """
