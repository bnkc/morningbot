import os
import geocoder


class WeatherApi:
    # Weather API
    WX_API_KEY = os.getenv("WX_API_KEY")
    WX_LOCATION = geocoder.ip("me").city
    WX_METRIC_TEMP = os.environ.get("WX_METRIC_TEMP", "fahrenheit")
    WX_METRIC_WIND = os.environ.get("WX_METRIC_WIND", "miles_hour")
    WX_METRIC_RAIN = os.environ.get("WX_FEELS_LIKE", "fahrenheit")
