import requests
from datetime import datetime

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def find_city(city):
    response = requests.get(
        GEOCODING_URL,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    results = data.get("results") or []

    if not results:
        return None

    result = results[0]
    return {
        "name": result.get("name", city),
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "timezone": result.get("timezone", "auto"),
    }


def describe_weather(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Severe thunderstorm with hail",
    }
    return descriptions.get(code, "Conditions unavailable")


def get_weather_icon(code):
    if code == 0:
        return "☀️"
    if code == 1:
        return "🌤️"
    if code == 2:
        return "⛅"
    if code == 3:
        return "☁️"
    if code in (45, 48):
        return "🌫️"
    if code in (51, 53, 55, 56, 57):
        return "🌦️"
    if code in (61, 63, 65, 66, 67, 80, 81, 82):
        return "🌧️"
    if code in (71, 73, 75, 77, 85, 86):
        return "❄️"
    if code in (95, 96, 99):
        return "⛈️"
    return "🌡️"


def fetch_weather(latitude, longitude, timezone="auto"):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,relative_humidity_2m,apparent_temperature,"
            "wind_speed_10m,weather_code,is_day"
        ),
        "daily": "weather_code,temperature_2m_max,temperature_2m_min",
        "forecast_days": 5,
        "timezone": timezone or "auto",
    }
    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if not isinstance(data.get("current"), dict):
        raise ValueError("Current weather data is missing.")
    if not isinstance(data.get("daily"), dict):
        raise ValueError("Forecast data is missing.")
    return data


def get_weather_data(city):
    location = find_city(city)
    if location is None:
        return None

    data = fetch_weather(
        location["latitude"],
        location["longitude"],
        location.get("timezone", "auto"),
    )
    current = data["current"]
    daily = data["daily"]

    forecast = []
    dates = daily.get("time", [])
    codes = daily.get("weather_code", [])
    highs = daily.get("temperature_2m_max", [])
    lows = daily.get("temperature_2m_min", [])

    if not dates or not (len(dates) == len(codes) == len(highs) == len(lows)):
        raise ValueError("Forecast data is incomplete.")

    for i, date in enumerate(dates):
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        forecast.append({
            "date": parsed_date.strftime("%A, %b %d"),
            "is_today": i == 0,
            "description": describe_weather(codes[i]),
            "icon": get_weather_icon(codes[i]),
            "max_temp": highs[i],
            "min_temp": lows[i],
        })

    code = current.get("weather_code")
    current_time = current.get("time", "")
    return {
        "location": location,
        "current": current,
        "description": describe_weather(code),
        "icon": get_weather_icon(code),
        "forecast": forecast,
        "is_day": current.get("is_day", 1),
        "current_time_display": current_time.replace("T", " ") if current_time else "Unavailable",
    }
