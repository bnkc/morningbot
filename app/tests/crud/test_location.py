from app.crud import city_and_coord


def test_city_and_coord():
    """
    Tests for IndexError if city is not found.
    """

    assert city_and_coord("this is not a city") is None
