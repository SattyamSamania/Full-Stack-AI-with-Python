import requests


def get_weather_message(temp):
    """Returns a simple weather message based on temperature."""
    if temp < 15:
        return "Very cold"
    elif 15 <= temp < 25:
        return "Normal"
    else:
        return "Hot"


def get_weather_data(city):
    """Fetches live weather data from wttr.in for the given city."""
    
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    data = response.json()
    temp_c = data["current_condition"][0]["temp_C"]

    return f"Current temperature in {city} is {temp_c}°C which is {get_weather_message(int(temp_c))}."
