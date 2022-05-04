from typing import List, Optional
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

    def get_city(self, message: str) -> Optional[str]:
        city = GeoText(message).cities
        return city[0] if city else None

    def get_coords(self, message: str) -> Optional[List[float]]:
        coordinates = geocoder.osm(message).latlng
        return coordinates if coordinates else None

    def is_body_valid(self, body: str) -> bool:
        return True if self.get_city(body) and self.get_coords(body) else False

    def is_first_time_user(self, number: str) -> bool:
        if IncomingNumbers.query.filter_by(number=number).count() <= 1:
            return True
        return False

    def is_daily_limit_reached(self, number: str) -> bool:
        MAX_INTERACTIONS = 3
        today = dt.today().date()
        if (
            IncomingNumbers.query.filter(IncomingNumbers.number == number)
            .filter(IncomingNumbers.created_at == today)
            .count()
            > MAX_INTERACTIONS
        ):
            return True
        return False
