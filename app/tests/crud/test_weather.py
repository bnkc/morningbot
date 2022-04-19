import pytest

from app.crud import Weather
from app.schemas import DemoUser


def test_types():
    """
    Test types of weather data
    """
    weather_ = Weather("London, GB").get_weather_by_location(DemoUser.user_2)
    assert isinstance(weather_["max"], int)
    assert isinstance(weather_["day"], int)
    assert isinstance(weather_["min"], int)
    assert isinstance(weather_["feels like"], int)
    assert isinstance(weather_["wind"], int)
    assert isinstance(weather_["detailed_status"], str)
    assert isinstance(weather_["uv"], int)
    assert isinstance(weather_["location"], str)


def test_get_weather_by_location_raises():
    """
    Tests for exception if NoneType in dict
    """
    weather_ = Weather("London, GB")
    with pytest.raises(Exception):
        weather_.get_weather_by_location(DemoUser.user_1)
