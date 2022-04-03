from .helper import format_data


class Message:
    def __init__(self, weather=None):
        self.data: dict = weather
        self.feels_like: float = self.data["feels like"]
        self.rain: float = self.data["rain"]
        self.snow: float = self.data["snow"]
        self.wind: float = self.data["wind"]
        self.status: str = self.data["detailed_status"]

    @classmethod
    def from_current(cls):
        return cls(format_data())

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

    def rain_set_rules(self) -> str:
        rain = self.rain
        if rain > 0:
            rain_status = "raining 🌧️"
        else:
            rain_status = "not raining"
        if rain < 0:
            raise Exception("Error: out of range")
        return rain_status

    def snow_set_rules(self) -> str:
        snow = self.snow
        if snow > 0:
            snow_status = "is snowing 🌨️"
        else:
            snow_status = "not snowing 🌻"
        if snow < 0:
            raise Exception("Error: out of range")
        return snow_status

    def wind_set_rules(self) -> str:
        wind = self.wind
        if wind > 20:
            wind_status = "windy 💨 "
        else:
            wind_status = "calm 😌"
        if wind < 0:
            raise Exception("Error: out of range")
        return wind_status

    def create_message(self) -> str:
        message = f"Good morning! Today it will be {self.temp_set_rules()} with {self.status}, feeling like {self.data['feels like']}°F. The High of the day is {self.data['max']}°F and the Low at {self.data['min']}°F. It might be {self.wind_set_rules()} with wind speeds of {self.data['wind']}mph. Lastly, it is {self.rain_set_rules()} and {self.snow_set_rules()} in {self.data['location']}."
        return message


# from app.schemas import TestData
# from app.weather import CurrentWeather


# if __name__ == "__main__":
#     test = TestData()
#     # print(test.default_data())
#     print(Message.temp_set_rules(Message(test.default_data())))
