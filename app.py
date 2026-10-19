from flask import Flask, render_template, request
import requests
from weather_service import get_weather_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        elif len(city) > 100:
            error = "Please enter a city name shorter than 100 characters."
        else:
            try:
                weather = get_weather_data(city)
                if weather is None:
                    error = "City not found. Check the spelling and try again."
            except requests.exceptions.Timeout:
                error = "The weather request timed out. Please try again."
            except requests.exceptions.ConnectionError:
                error = "Could not connect to the weather service. Check your internet connection."
            except requests.exceptions.HTTPError:
                error = "The weather service returned an error. Please try again shortly."
            except requests.exceptions.RequestException:
                error = "Could not retrieve weather data. Please try again."
            except (KeyError, TypeError, ValueError, IndexError):
                error = "The weather service returned incomplete data. Please try again."

    return render_template("index.html", weather=weather, error=error, city=city)


if __name__ == "__main__":
    # Debug is disabled by default; enable only while developing locally.
    app.run(debug=True)
