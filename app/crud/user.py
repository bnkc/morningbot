from datetime import datetime

from .location import city_and_coord
from app.db import User, db


class CheckUser:
    """
    This method adds a user to the database as well as checks if the user has reached the daily limit.
    It also checks if the user is a new user or if the message body is valid.
    """

    def add_user(number, time):
        user = User(number, time)
        db.session.add(user)
        db.session.commit()
        return user

    def is_body_valid(body):
        if city_and_coord(body) is None:
            return False
        return True

    def is_first_time_user(number):
        if User.query.filter_by(number=number).count() <= 1:
            return True
        return False

    def is_daily_limit_reached(number):
        today = datetime.today().date()
        if (
            User.query.filter(User.number == number)
            .filter(User.created_at == today)
            .count()
            > 3
        ):
            return True
        return False
