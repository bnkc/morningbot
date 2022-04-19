from app.crud import Weather


class Message:
    def __init__(self, location: str) -> None:
        self.data: dict = Weather(location).get_weather_by_location(
            Weather(location).get_weather
        )
        self.feels_like: float = self.data["feels like"]
        self.wind: float = self.data["wind"]
        self.status: str = self.data["detailed_status"]

    def temp_set_rules(self) -> str:
        feels_like = self.feels_like
        if feels_like <= 30:
            temp_status = "freezing 🥶"
        elif feels_like > 30 and feels_like <= 45:
            temp_status = "pretty cold 🧊"
        elif feels_like > 45 and feels_like < 60:
            temp_status = "nippy 🧥"
        elif feels_like >= 60 and feels_like <= 80:
            temp_status = "warm 🌞"
        else:
            temp_status = "hot 🥵"
        if feels_like > 150 or feels_like < -50:
            raise Exception("Error: out of range")
        return temp_status

    def wind_set_rules(self) -> str:
        wind = self.wind
        if wind > 20:
            wind_status = "windy 💨 "
        else:
            wind_status = "calm 😌"
        if wind < 0:
            raise Exception("Error: out of range")
        return wind_status

    def create_msg(self) -> str:
        message = f"Good morning! Today it will be {self.temp_set_rules()} with {self.status}, feeling like {self.data['feels like']}°F. The High of the day is {self.data['max']}°F and the Low at {self.data['min']}°F. It might be {self.wind_set_rules()} with wind speeds of {self.data['wind']}mph in {self.data['location']}."
        return message
