from datetime import datetime

from .crud_location import get_city, get_coords
from app.db import IncomingNumbers, db


class User:
    """
    This method adds a user to the database as well as checks if the user has reached the daily limit.
    It also checks if the user is a new user or if the message body is valid.
    """

    def add_number(number, time):
        user = IncomingNumbers(number, time)
        db.session.add(user)
        db.session.commit()
        return user

    def is_body_valid(body):
        if get_city(body) and get_coords(body):
            return True
        return False

    def is_first_time_user(number):
        ONE_INTERACTION = 1
        if IncomingNumbers.query.filter_by(number=number).count() <= ONE_INTERACTION:
            return True
        return False

    def is_daily_limit_reached(number):
        MAX_INTERACTIONS = 3
        today = datetime.today().date()
        if (
            IncomingNumbers.query.filter(IncomingNumbers.number == number)
            .filter(IncomingNumbers.created_at == today)
            .count()
            > MAX_INTERACTIONS
        ):
            return True
        return False
