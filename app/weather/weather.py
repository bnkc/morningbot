from pyowm import OWM
from dotenv import load_dotenv

load_dotenv()

from app.docs import WeatherApi


class Weather:
    def __init__(self, metric_temp=None, metric_wind=None) -> None:
        self.manager = OWM(WeatherApi.WX_API_KEY).weather_manager()
        self.default_location = WeatherApi.WX_LOCATION
        self.metric_temp = metric_temp or WeatherApi.WX_METRIC_TEMP
        self.metric_wind = metric_wind or WeatherApi.WX_METRIC_WIND

    def get_weather_data(self, weather) -> dict:
        return {
            "max": weather.temperature(self.metric_temp)["temp_max"],
            "min": weather.temperature(self.metric_temp)["temp_min"],
            "feels like": weather.temperature(self.metric_temp)["feels_like"],
            "wind": weather.wind(self.metric_wind)["speed"],
            "rain": weather.rain,
            "snow": weather.snow,
            "detailed_status": weather.detailed_status,
        }


class CurrentWeather(Weather):
    def __init__(self):
        super().__init__()

    def current(self, get_data=None, location=None) -> dict:
        """
        Get current weather data for a location.
        Using location or default to add optional location parameter.
        """
        observation = self.manager.weather_at_place(location or self.default_location)
        weather = observation.weather
        result = get_data(weather)
        result[
            "location"
        ] = f"{observation.location.name} {observation.location.country}"

        for key, val in result.items():
            if val is None:
                raise Exception(f"Error: {key} is None")

        return result


# if __name__ == "__main__":
#     weather = CurrentWeather()
#     print(weather.current(weather.get_weather_data))