from dataclasses import dataclass


@dataclass
class WeatherData:
    """
    Class to check weather data types
    """

    max_temp: float
    min_temp: float
    feels_like: float
    wind_speed: float
    detailed_status: str
    uv_index: float
