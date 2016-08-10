from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import app

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:test.db"

db = SQLAlchemy(app)


# create a user class
class User(db.Model):
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(80), unique=True)
    date_of_birth = db.Column(db.Integer(80), unique=True)

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth



