from typing import List
from datetime import datetime as dt

import geocoder
from geotext import GeoText

from app.db import IncomingNumbers, db


class User:
    def __init__(self) -> None:
        pass

    def add_number(self, number: str, time: dt) -> None:
        user = IncomingNumbers(number, time)
        db.session.add(user)
        db.session.commit()
        return user

    def get_city(self, message: str) -> str:
        if GeoText(message).cities:
            return GeoText(message).cities[0]
        else:
            raise ValueError("Invalid location")

    def get_coords(self, message: str) -> List[float]:
        coordinates = geocoder.osm(message).latlng
        if coordinates:
            return coordinates
        else:
            raise ValueError("Invalid location")

    def is_first_time_user(self, number: str) -> bool:
        return IncomingNumbers.query.filter_by(number=number).count() <= 1

    def is_daily_limit_reached(self, number: str) -> bool:
        MAX_INTERACTIONS = 3
        today = dt.today().date()
        return (
            IncomingNumbers.query.filter(IncomingNumbers.number == number)
            .filter(IncomingNumbers.created_at == today)
            .count()
            > MAX_INTERACTIONS
        )
