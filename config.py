from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import app

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:test.db"

db = SQLAlchemy(app)


# create a user class
class User(db.Model):
    first_name = db.Column()


