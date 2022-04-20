from .location import city_and_coord


def is_body_valid(body):
    if city_and_coord(body) is None:
        return False
    return True
