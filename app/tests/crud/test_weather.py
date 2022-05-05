import pytest
from dataclasses import asdict

from app.crud import Weather, coerce_floats
from app.tests.data import user_3, user_2


def test_coerce_floats():
    assert coerce_floats(asdict(user_2()))


def test_coerce_floats_edge_case():
    with pytest.raises(Exception):
        coerce_floats(asdict(user_3()))
