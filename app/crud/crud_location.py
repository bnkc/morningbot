from typing import List, Optional

import geocoder
from geotext import GeoText


def get_city(message: str) -> Optional[str]:
    """
    Returns the city of the message.
    """
    try:
        city = GeoText(message).cities[0]
        return city
    except IndexError:
        return None


def get_coords(message: str) -> Optional[List[float]]:
    """
    Returns the coordinates of the message.
    """
    try:
        coordinates = geocoder.osm(message).latlng
        return coordinates
    except IndexError:
        return None


print(get_coords("New York"))
