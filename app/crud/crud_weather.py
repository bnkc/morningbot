from typing import List, Optional, cast
from dotenv import load_dotenv

load_dotenv()

from config import Config
from app.schemas import WeatherData
from .crud_location import get_city, get_coords


class Weather:
    def __init__(self) -> None:
        self.manager = Config.manager
        self.metric_temp: str = Config.metric_temp
        self.metric_wind: str = Config.metric_wind

    def get_weather(
        self, weather: dict[str, str], location: str
    ) -> dict[str, float | str]:
        """
        Return a dictionary of weather data.
        """
        coords = cast(List[float], get_coords(location))
        one_call: WeatherData = self.manager.one_call(
            coords[0], coords[1]
        ).forecast_daily[0]
        weather = one_call.temperature(self.metric_temp)
        wind = one_call.wind(self.metric_wind)

        temp = WeatherData(
            max_temp=weather["max"],
            min_temp=weather["min"],
            feels_like_temp=weather["feels_like_morn"],
            wind_speed=wind["speed"],
            detailed_status=one_call.detailed_status,
            uv_index=one_call.uvi,
        )
        return {
            "max temp": temp.max_temp,
            "min temp": temp.min_temp,
            "feels like": temp.feels_like_temp,
            "wind speed": temp.wind_speed,
            "detailed status": temp.detailed_status,
            "uv index": temp.uv_index,
        }

    def get_weather_by_location(self, location: str) -> dict[str, int | str]:
        """
        Get current weather data for a location
        """
        city: Optional[str] = get_city(location)
        observation = self.manager.weather_at_place(city)
        weather = observation.weather
        result = self.get_weather(weather, location)
        result[
            "location"
        ] = f"{observation.location.name} {observation.location.country}"

        return self.coerce_floats(result)

    def coerce_floats(self, weather: dict[str, float | str]) -> dict[str, int | str]:
        """
        Coerce all float data to ints.
        """
        ###################################################################
        #### ask sergey why the return type is not dict[str, int|str] #####
        ###################################################################

        for key, value in weather.items():
            if isinstance(value, float):
                weather[key] = int(value)
            elif value is None:
                raise Exception(f"Error: {key} is None")

        return weather
