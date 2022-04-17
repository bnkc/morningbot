from typing import List
from pyowm import OWM
from dotenv import load_dotenv
import os

from app.docs import inbound_location, coordinates

load_dotenv()


class Weather:
    def __init__(self, location: str, metric_temp=None, metric_wind=None) -> None:
        self.manager = OWM(os.environ["WX_API_KEY"]).weather_manager()
        self.location = inbound_location(location)
        self.coordinates = coordinates(location)
        self.metric_temp = metric_temp or os.environ.get("WX_METRIC_TEMP", "fahrenheit")
        self.metric_wind = metric_wind or os.environ.get("WX_METRIC_WIND", "miles_hour")
        self.onecall = self.manager.one_call(self.coordinates[0], self.coordinates[1])

    def get_weather_data(self, weather) -> dict:
        """Get weather data from OWM."""
        return {
            "max": self.onecall.forecast_daily[0].temperature(self.metric_temp)["max"],
            "min": self.onecall.forecast_daily[0].temperature(self.metric_temp)["min"],
            "feels like": self.onecall.forecast_daily[0].temperature(self.metric_temp)[
                "feels_like_morn"
            ],
            "wind": weather.wind(self.metric_wind)["speed"],
            "detailed_status": weather.detailed_status,
        }

    def weather_dict(self, get_data=None, location=None) -> dict:
        """
        Get current weather data for a location.
        Using location or default to add optional location parameter.
        """
        observation = self.manager.weather_at_place(location or self.location)
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
