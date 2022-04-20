from datetime import datetime

from .location import city_and_coord
from app.db import User, db


class Requests:
    def add_user(number, time):
        user = User(number, time)
        db.session.add(user)
        db.session.commit()
        return user

    def is_body_valid(body):
        if city_and_coord(body) is None:
            return False
        return True

    def is_first_time_user(number_):
        if User.query.filter_by(number=number_).count() <= 1:
            return True
        return False

    def is_daily_limit_reached(number_):
        today = datetime.today().date()
        if (
            User.query.filter(User.number == number_)
            .filter(User.created_at == today)
            .count()
            > 3
        ):
            return True
        return False
