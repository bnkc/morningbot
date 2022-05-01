from typing import Any
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true
import sqlalchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db: sqlalchemy = SQLAlchemy(app)


class IncomingNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.Date, nullable=False)

    def __init__(self, number, created_at):
        self.number = number
        self.created_at = created_at


####################################################################################
#### Turns out that you do need the __init__ otherwise flask app returns 500's #####
####################################################################################

if __name__ == "__main__":
    app.run(debug=True)
