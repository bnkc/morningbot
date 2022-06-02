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

    def get_weather(self, weather: dict[str, str], location: str) -> WeatherData:
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
            location=location,
            max_temp=weather["max"],
            min_temp=weather["min"],
            feels_like=weather["feels_like_morn"],
            wind_speed=wind["speed"],
            detailed_status=one_call.detailed_status,
            uv_index=one_call.uvi,
        )
        return temp

    def get_weather_by_location(self, location: str) -> WeatherData:
        """
        Get current weather data for a location
        """
        coords = self.user.get_coords(location)
        observation = self.manager.weather_at_coords(coords[0], coords[1])
        result = self.get_weather(observation.weather, location)
        return result
