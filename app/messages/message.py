from app.crud import Weather


def create_custom_msg(location: str) -> str:
    weather = Weather()
    weather = weather.get_weather_by_location(location)
    return f"""
Good mornin' 🌳
Here's the weather for {weather["location"]}:\n
🌡️ Max: {weather["max_temp"]}°F
🌡️ Min: {weather["min_temp"]}°F
🌡️ Feels like: {weather["feels_like"]}°F
💨 Wind: {weather["wind_speed"]} mph
🌬️ Status: {weather["detailed_status"]}
🌞 UV Index: {weather["uv_index"]}
    """


DAILY_LIMIT_MSG = "Sorry, you've reached your daily limit. Please try again tomorrow."
ERROR_MSG = "Sorry, I couldn't find that location. Please try again."
WELCOME_MSG = """
Welcome to Morning Bot! 🤖\n
This message is generated the first time you use me and verifies your number.
Tomorrow will be your first weather update!
If you ever get tired of me, just remove your shortcut. 
You can always add me back with the same shortcut.\n
I am currently in beta. If you have any questions, please contact @levostatnigrosh.
"""
