from pyowm import OWM
from dotenv import load_dotenv

from app.docs import WeatherApi

load_dotenv()


class Weather:
    def __init__(self, metric_temp=None, metric_wind=None) -> None:
        self.manager = OWM(WeatherApi.WX_API_KEY).weather_manager()
        self.location = WeatherApi.WX_LOCATION
        self.coordinates = WeatherApi.WX_COORDINATES
        self.metric_temp = metric_temp or WeatherApi.WX_METRIC_TEMP
        self.metric_wind = metric_wind or WeatherApi.WX_METRIC_WIND
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


class CurrentWeather(Weather):
    def __init__(self) -> None:
        super().__init__()

    def current(self, get_data=None, location=None) -> dict:
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
            if val is None:
                raise Exception(f"Error: {key} is None")

        return result


if __name__ == "__main__":
    weather = CurrentWeather()
    print(weather.current(weather.get_weather_data))
