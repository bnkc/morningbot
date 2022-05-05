from dataclasses import dataclass
from app.schemas import WeatherData


def user_1() -> WeatherData:
    user_1 = WeatherData(
        max_temp=70,
        min_temp=10,
        feels_like=20,
        wind_speed=10,
        detailed_status="Clear",
        uv_index=5,
    )
    return user_1


def user_2() -> WeatherData:
    user_2 = WeatherData(
        max_temp=170,
        min_temp=10,
        feels_like=20,
        wind_speed=10,
        detailed_status="Clear",
        uv_index=5,
    )
    return user_2


def user_3() -> WeatherData:
    user_2 = WeatherData(
        max_temp=100,
        min_temp=None,
        feels_like=20,
        wind_speed=10,
        detailed_status="Clear",
        uv_index=5,
    )
    return user_2
