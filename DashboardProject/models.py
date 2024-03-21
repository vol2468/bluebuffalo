from . import db
from flask_login import UserMixin


class City(db.Model):
    __tablename__ = 'city'
    cityId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cityName = db.Column(db.String(50))
    population = db.Column(db.Integer)
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))


class Pollutant(db.Model):
    __tablename__ = 'pollutant'
    cityId = db.Column(db.Integer, db.ForeignKey('city.cityId'), primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    O3Mean = db.Column(db.Float)
    O3AQI = db.Column(db.Integer)
    COMean = db.Column(db.Float)
    COAQI = db.Column(db.Integer)
    SO2Mean = db.Column(db.Float)
    SO2AQI = db.Column(db.Integer)
    NO2Mean = db.Column(db.Float)
    NO2AQI = db.Column(db.Integer)


class Comment(db.Model):
    __tablename__ = 'comment'
    commentId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pageType = db.Column(db.String(10))
    commentText = db.Column(db.String(2000))
    graphDate = db.Column(db.Date)
    commentDate = db.Column(db.Date)
    userId = db.Column(db.Integer, db.ForeignKey('user.userId'))
    cityId = db.Column(db.Integer, db.ForeignKey('city.cityId'))

