from typing import List
from dotenv import load_dotenv

load_dotenv()

from app.schemas import ConfigWeather, WeatherData
from .location import city_and_coord


class Weather:
    def __init__(self, location: str) -> None:
        self.manager = ConfigWeather.manager
        self.location: str = city_and_coord(location)[0]
        self.coordinates: List[float] = city_and_coord(location)[1]
        self.metric_temp: str = ConfigWeather.metric_temp
        self.metric_wind: str = ConfigWeather.metric_wind
        self.one_call = self.manager.one_call(
            self.coordinates[0], self.coordinates[1]
        ).forecast_daily[0]

    def get_weather(self, weather: dict) -> dict:
        weather = self.one_call.temperature(self.metric_temp)
        wind = self.one_call.wind(self.metric_wind)

        temp = WeatherData(
            max_temp=weather["max"],
            day_temp=weather["day"],
            min_temp=weather["min"],
            feels_like_temp=weather["feels_like_morn"],
            wind_speed=wind["speed"],
            detailed_status=self.one_call.detailed_status,
        )

        return {
            "max": temp.max_temp,
            "day": temp.day_temp,
            "min": temp.min_temp,
            "feels like": temp.feels_like_temp,
            "wind": temp.wind_speed,
            "detailed_status": temp.detailed_status,
        }

    def get_weather_by_location(self, get_data=None) -> dict:
        """
        Get current weather data for a location.
        Using location or default to add optional location parameter.
        """

        observation = self.manager.weather_at_place(self.location)
        weather = observation.weather
        result = get_data(weather)
        result[
            "location"
        ] = f"{observation.location.name} {observation.location.country}"

        for key, val in result.items():
            if type(val) is float:
                result[key] = int(val)
            elif val is None:
                raise Exception(f"Error: {key} is None")

        return result
