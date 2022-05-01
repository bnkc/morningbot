from app.crud import get_city, get_coords


def test_city_get_city():
    """
    Test get_city function.
    """
    passing_message = "I am in New York"
    failing_message = "I am not at home"
    assert get_city(passing_message) == "New York"
    assert get_city(failing_message) is None


def test_coords_get_coords():
    """
    Test get_coords function.
    """
    passing_message = "I am in New York"
    failing_message = "I am not at home"
    assert get_coords(passing_message) is None
    assert get_coords(failing_message) is None
