from typing import List, Optional
from dataclasses import asdict
from dotenv import load_dotenv

load_dotenv()
from pyowm import OWM

from app.config import Config
from app.schemas import WeatherData
from .crud_user import User


class Weather:
    def __init__(self) -> None:
        self.manager = OWM(Config.manager).weather_manager()
        self.metric_temp: str = Config.metric_temp
        self.metric_wind: str = Config.metric_wind
        self.user = User()

    def get_weather(
        self, weather: dict[str, str], location: str
    ) -> dict[str, float | str]:
        """
        Return a dictionary of weather data.
        """
        coords = self.user.get_coords(location)
        one_call: WeatherData = self.manager.one_call(
            coords[0], coords[1]
        ).forecast_daily[0]
        weather = one_call.temperature(self.metric_temp)
        wind = one_call.wind(self.metric_wind)

        temp = WeatherData(
            max_temp=weather["max"],
            min_temp=weather["min"],
            feels_like=weather["feels_like_morn"],
            wind_speed=wind["speed"],
            detailed_status=one_call.detailed_status,
            uv_index=one_call.uvi,
        )
        return asdict(temp)

    def get_weather_by_location(self, location: str) -> dict[str, int | str]:
        """
        Get current weather data for a location
        """
        city: Optional[str] = self.user.get_city(location)
        country_code: Optional[str] = self.user.get_country_code(location)
        observation = self.manager.weather_at_place(city + "," + country_code)
        weather = observation.weather
        result = self.get_weather(weather, location)
        result[
            "location"
        ] = f"{observation.location.name} {observation.location.country}"

        return coerce_floats(result)


def coerce_floats(result: dict[str, float | str]) -> dict[str, int | str]:
    """
    Coerce all float data to ints.
    """
    for key, value in result.items():
        if isinstance(value, float):
            result[key] = int(value)
        elif value is None:
            raise Exception(f"Error: {key} is None")
    return result
