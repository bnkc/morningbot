from typing import List
from datetime import datetime as dt


from app.db import IncomingNumbers, db
from app.config import Config


class User:
    def __init__(self) -> None:
        self.gmaps = Config.gmaps

    def add_number(self, number: str, time: dt) -> None:
        user = IncomingNumbers(number, time)
        db.session.add(user)
        db.session.commit()
        return user

    def get_area(self, message: str) -> str:
        geo_result = self.gmaps.geocode(message)
        if geo_result:
            return geo_result[0]["address_components"][2]["long_name"]
        else:
            raise ValueError("Invalid location")

    def get_coords(self, message: str) -> List[float]:
        geo_result = self.gmaps.geocode(message)
        if geo_result:
            lat = geo_result[0]["geometry"]["location"]["lat"]
            lng = geo_result[0]["geometry"]["location"]["lng"]
            return [lat, lng]
        else:
            raise ValueError("Invalid location")

    def is_first_time_user(self, number: str) -> bool:
        return IncomingNumbers.query.filter_by(number=number).count() <= 1

    def is_daily_limit_reached(self, number: str) -> bool:
        MAX_INTERACTIONS = 3  ###FIXME: Hardcoded value
        today = dt.today().date()
        return (
            IncomingNumbers.query.filter(IncomingNumbers.number == number)
            .filter(IncomingNumbers.created_at == today)
            .count()
            > MAX_INTERACTIONS
        )
