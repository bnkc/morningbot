from datetime import datetime
from flask import request
from twilio.twiml.messaging_response import MessagingResponse

from app.crud import Requests
from app.messages import Message
from app.db import app


@app.route("/sms", methods=["POST"])
def sms():
    """
    Respond to incoming messages with a weather update.
    """
    created_at = datetime.today().date()
    msg_body = request.form.get("Body")
    inbound_number = request.form.get("From")
    Requests.add_user(inbound_number, created_at)
    resp = MessagingResponse()
    if not Requests.is_daily_limit_reached(inbound_number):
        if Requests.is_first_time_user(inbound_number):
            welcome_msg = Message.welcome_msg()
            resp.message(welcome_msg)
        if Requests.is_body_valid(msg_body):
            inbound_msg = Message.get_msg(msg_body)
            resp.message(Message(inbound_msg).create_msg())
        else:
            error_msg = Message.error_msg()
            resp.message(error_msg)
    else:
        daily_limit_msg = Message.daily_limit_msg()
        resp.message(daily_limit_msg)

    return str(resp)


if __name__ == "__main__":
    app.run()
