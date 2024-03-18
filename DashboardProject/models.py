# from . import db
# from flask_login import UserMixin


# class User(db.Model, UserMixin):
#     email = db.Column(db.String(100), primary_key=True, unique=True)
#     firstname = db.Column(db.String(100))
#     lastname = db.Column(db.String(100))
#     password = db.Column(db.String(100))
#     city = db.Column(db.String(100))

# class City(db.Model):
#     name = db.Column(db.String(100), primary_key=True, unique=True)
#     population = db.Column(db.Integer())
#     latitude = db.Column(db.String(100))
#     longitude = db.Column(db.String(100))
#     graphId = db.Column(db.Integer)
#     graphDescription = db.Column(db.String(10000))

# class Comment(db.Model):
#     commentId = db.Column(db.String(100), primary_key=True, unique=True)
#     email = db.Column(db.String(100))
#     commentText = db.Column(db.String(10000))
#     commentDate = db.Column(db.Date)