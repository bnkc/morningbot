from app.crud import Weather
from app.crud import User


def create_custom_msg(location: str) -> str:
    weather = Weather()
    user = User()
    weather = weather.get_weather_by_location(location)
    city = user.get_area(location)
    return f"""
Good mornin' 🌳
Here's the weather for {city}:\n
🌡️ Max: {weather.max_temp}°F
🌡️ Min: {weather.min_temp}°F
🌡️ Feels like: {weather.feels_like}°F
💨 Wind: {weather.wind_speed} mph
🌬️ Status: {weather.detailed_status}
🌞 UV Index: {weather.uv_index}
    """


DAILY_LIMIT_MSG = "Sorry, you've reached your daily limit. Please try again tomorrow."
ERROR_MSG = "Sorry, I couldn't find that location. Please try again."
WELCOME_MSG = """
Welcome to Morning Bot! 👾\n
I am currently in beta. If you have any questions or ideas please reach out to @levostatnigrosh. \n
Here's your first weather update!
"""
