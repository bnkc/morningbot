from app.db import app


def test_request_route_returns_200():
    response = app.test_client().get("/sms")
    assert response.status_code == 200


def test_request_response_body_is_not_empty():
    response = app.test_client().get("/sms")
    assert response.data != ""
