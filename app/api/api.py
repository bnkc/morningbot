from datetime import datetime as dt

from flask import request
from twilio.twiml.messaging_response import MessagingResponse

from app.crud import User
from app.messages import create_custom_msg, DAILY_LIMIT_MSG, ERROR_MSG, WELCOME_MSG
from app.db import app


@app.route("/sms", methods=["POST"])
def sms() -> str:
    """
    Respond to incoming messages with a weather update.
    """
    body = request.form.get("Body")
    inbound_number = request.form.get("From")
    created_at = dt.today().date()

    user = User()
    user.add_number(inbound_number, created_at)

    resp = MessagingResponse()
    if user.is_daily_limit_reached(inbound_number):
        resp.message(DAILY_LIMIT_MSG)
        return str(resp)

    if user.is_first_time_user(inbound_number):
        resp.message(WELCOME_MSG)
        return str(resp)

    if user.is_body_valid(body):
        resp.message(create_custom_msg(body))
        return str(resp)

    else:
        resp.message(ERROR_MSG)
        return str(resp)


if __name__ == "__main__":
    app.run()
