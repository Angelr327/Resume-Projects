import requests

API_KEY = "7848047dd03c207d6f0c73b61120179c"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {   
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "description": data["weather"][0]["description"]
    }

