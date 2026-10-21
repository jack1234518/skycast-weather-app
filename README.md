# 🌦️ SkyCast Weather App

A responsive weather dashboard built with **Python and Flask** that provides current weather conditions and a five-day forecast. SkyCast uses the Open-Meteo API to retrieve weather and geocoding data, with no API key required.

## 🌐 Live Demo

**[Open SkyCast Weather App](https://skycast-weather-app-5dob.onrender.com/)**

## ✨ Features

- **Current Weather:** View current weather conditions for a searched city.
- **Five-Day Forecast:** Explore upcoming weather conditions.
- **City Search:** Search for locations using geocoding data.
- **Dynamic Weather Icons:** Display weather icons based on weather conditions.
- **Temperature Conversion:** Switch between Celsius and Fahrenheit.
- **Responsive Design:** Access the dashboard on desktop and mobile screens.
- **Live Weather Data:** Retrieve weather information from Open-Meteo.
- **Cloud Deployment:** Access the application online through Render.

## 🛠️ Technologies Used

- **Python 3.10+** — application logic
- **Flask** — web framework
- **Requests** — HTTP requests to weather services
- **Open-Meteo API** — weather forecasts and geocoding
- **HTML and CSS** — dashboard structure and styling
- **Git and GitHub** — version control and source code hosting
- **Gunicorn** — production WSGI server
- **Render** — cloud hosting and deployment

## 📁 Project Structure

```text
skycast-weather-app/
├── app.py
├── weather_service.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## ⚙️ Requirements

- Python 3.10 or newer
- Git
- An internet connection

No Open-Meteo API key is required.

## 💻 Run Locally on Windows

### 1. Clone the repository

Open PowerShell and run:

```powershell
git clone https://github.com/jack1234518/skycast-weather-app.git
cd skycast-weather-app
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can activate the environment using Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Start the application

```powershell
python app.py
```

Open your browser and visit:

**http://127.0.0.1:5000**

To stop the development server, press `Ctrl + C` in the terminal.

## 🚀 Deployment

SkyCast is deployed on Render and connected to its GitHub repository.

- **Live application:** https://skycast-weather-app-5dob.onrender.com/
- **Production start command:** `gunicorn app:app`
- **Dependency installation:** `pip install -r requirements.txt`

Render can automatically deploy new changes pushed to the connected branch when automatic deployments are enabled.

> Note: Render's free web services may spin down after inactivity, so the first request after a quiet period can take longer.

## 📡 Weather Data

SkyCast uses Open-Meteo for weather forecasts and geocoding.

- **Weather API:** https://open-meteo.com/
- **Geocoding API:** https://open-meteo.com/en/docs/geocoding-api

The application does not require an API key for these services under their applicable usage terms.

## 🔧 Development Notes

- Keep `app.py`, `weather_service.py`, `templates/`, and `static/` in the same project directory.
- The original `weather_app.py` command-line project can remain in the repository, but the Flask dashboard uses `app.py`.
- Flask debug mode should only be enabled during local development. For public deployment, use Gunicorn and disable debug mode.
- Keep dependencies documented in `requirements.txt` so the application can be reproduced on another machine.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python web development using Flask.
- Integrating external REST APIs.
- Retrieving weather and geocoding data.
- Organizing application logic into separate modules.
- Building a responsive web interface.
- Managing code with Git and GitHub.
- Deploying a Python application to a cloud hosting platform.

## 👨‍💻 Author

**Jackson Kenyanya**

Information Technology Student | Aspiring Software Developer

## 🔗 Project Links

- **Live Demo:** https://skycast-weather-app-5dob.onrender.com/
- **GitHub Repository:** https://github.com/jack1234518/skycast-weather-app
