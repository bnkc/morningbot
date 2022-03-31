import pytest
import src
from src import Weather, CurrentWeather
from typing import Optional
from schemas import WeatherData


def test_current():
    weather = CurrentWeather()
    assert isinstance(weather.current(WeatherData.default_data)["max"], float)
    assert isinstance(weather.current(WeatherData.default_data)["min"], float)
    assert isinstance(weather.current(WeatherData.default_data)["feels like"], float)
    assert isinstance(weather.current(WeatherData.default_data)["wind"], float)
    assert isinstance(weather.current(WeatherData.default_data)["rain"], Optional[dict])
    assert isinstance(weather.current(WeatherData.default_data)["snow"], Optional[dict])
    assert isinstance(weather.current(WeatherData.default_data)["location"], str)


def test_current_raises_exception():
    weather = CurrentWeather()
    with pytest.raises(Exception):
        weather.current(WeatherData.raise_exception_data)
