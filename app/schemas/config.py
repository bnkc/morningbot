import os
from dataclasses import dataclass

from pyowm import OWM


class ConfigWeather:
    """
    Class to store the configuration for crud weather app
    """

    manager = OWM(os.environ["WX_API_KEY"]).weather_manager()
    metric_temp = os.environ.get("WX_METRIC_TEMP", "fahrenheit")
    metric_wind = os.environ.get("WX_METRIC_WIND", "miles_hour")


@dataclass
class WeatherData:
    """
    Class to check weather data types
    """

    max_temp: float
    min_temp: float
    feels_like_temp: float
    wind_speed: float
    detailed_status: str
    uv_index: float
