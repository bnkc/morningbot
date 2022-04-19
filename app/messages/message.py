from typing import Optional
from app.crud import Weather


class Message:
    def __init__(self, data=None) -> None:
        self.data: dict = data
        self.max: int = self.data["max temp"]
        self.min: int = self.data["min temp"]
        self.feels_like: int = self.data["feels like"]
        self.wind: int = self.data["wind speed"]
        self.status: str = self.data["detailed_status"]
        self.uv: int = self.data["uv index"]
        self.location: str = self.data["location"]

    @classmethod
    def get_message(cls, location: str) -> Optional[dict]:
        data = Weather(location).get_weather_by_location(Weather(location).get_weather)
        return data

    @classmethod
    def error_msg(cls) -> str:
        message = "Sorry, I couldn't find that location. Please try again."
        return message

    def welcome_msg(self) -> str:
        message = (
            "Welcome to Morning Bot! 🤖\n\n"
            "This message is generated the first time you use me. "
            "If you ever get tired of me, just remove your shortcut. "
            "You can always add me back with the same shortcut.\n\n"
            "Here is your first weather update!\n"
        )
        return message

    def create_msg(self) -> str:
        message = (
            f"Good mornin' 🌳\n\n"
            f"Here's the weather for {self.location}:\n\n"
            f"🌡️ Max: {self.max}°F\n"
            f"🌡️ Min: {self.min}°F\n"
            f"🌡️ Feels like: {self.feels_like}°F\n"
            f"💨 Wind: {self.wind} mph\n"
            f"🌬️ Status: {self.status}\n"
            f"🌞 UV Index: {self.uv}"
        )
        return message
