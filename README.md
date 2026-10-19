# SkyCast Weather App

A Flask weather dashboard with current conditions, a five-day forecast, dynamic weather icons, responsive styling, and a Celsius/Fahrenheit switch.

## Requirements
- Python 3.10 or newer
- Internet connection

## Run on Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Project structure

```text
weather-app/
├── app.py
├── weather_service.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

Weather and geocoding data are provided by Open-Meteo. The app does not require an API key.

## Notes
- Keep `app.py`, `weather_service.py`, `templates/`, and `static/` in the same project directory.
- `weather_app.py` from your original command-line project can remain in the folder; this Flask version does not use it.
- `debug=True` is for local development only. Use a production WSGI server and disable debug mode before public deployment.
