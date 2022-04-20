from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


from app.crud import is_body_valid
from app.messages import Message


app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms():

    status = is_body_valid(request.form["Body"])
    resp = MessagingResponse()
    if not status:
        error_msg = Message.error_msg()
        resp.message(error_msg)
    else:
        inbound_sms = Message.get_message(request.form["Body"])
        resp.message(Message(inbound_sms).create_msg())

    return str(resp)


if __name__ == "__main__":
    app.run()
