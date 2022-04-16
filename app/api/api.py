from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from app.crud import Message


app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms():
    msg = Message(request.form["Body"])
    resp = MessagingResponse()
    resp.message(msg.create_msg())
    return str(resp)


if __name__ == "__main__":
    app.run()
