from pydantic import BaseModel


class WeatherData(BaseModel):
    """
    Class to check weather data types
    """

    location: str
    max_temp: int
    min_temp: int
    feels_like: int
    wind_speed: int
    detailed_status: str
    uv_index: int
