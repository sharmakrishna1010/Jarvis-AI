import os
import requests

def fetch_live_weather(city_name):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return False, "Sir, my OpenWeather API key is missing."

    try:
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
        geo_data = requests.get(geo_url).json()
        
        if not geo_data:
            return False, f"I couldn't locate {city_name} on the map, Sir."
            
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        actual_city = geo_data[0]['name']

        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_data = requests.get(weather_url).json()

        temp = round(weather_data['main']['temp'])
        desc = weather_data['weather'][0]['description']

        report = f"The current weather in {actual_city} is {desc} at {temp} degrees Celsius."
        return True, report

    except Exception as e:
        return False, "I lost connection to the weather satellite, Sir."