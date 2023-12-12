from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# Initialize the database
db = SQLAlchemy()

#from .app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(255), nullable=False)

class UserReq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    sqft_price = db.Column(db.Float, nullable=False)
    min_sqft = db.Column(db.Float, nullable=False)

class Auction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auid = db.Column(db.Integer, nullable=False)
    zip_code = db.Column(db.String(10), nullable=True)
    market_price = db.Column(db.Float, nullable=True)
    price = db.Column(db.Float, nullable=True)
    state = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(255))
    description = db.Column(db.String(255), nullable=False)
    sqft = db.Column(db.Float, nullable=True)
    fetch_page = db.Column(db.Boolean)
    date_start = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_end = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    city = db.Column(db.String(255), nullable=False)