from app.crud import Weather


def create_custom_msg(location: str) -> str:
    weather = Weather().get_weather_by_location(location)
    return f"""
Good mornin' 🌳
Here's the weather for {weather["location"]}:\n
🌡️ Max: {weather["max temp"]}°F
🌡️ Min: {weather["min temp"]}°F
🌡️ Feels like: {weather["feels like"]}°F
💨 Wind: {weather["wind speed"]} mph
🌬️ Status: {weather["detailed status"]}
🌞 UV Index: {weather["uv index"]}
    """


###################################################################################################
#### Was wondering why if I dont have the docstring all the way back it formats my text weird #####
###################################################################################################


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
