from flask import json


from . import db
import flask_login
import enum

class UserRole(enum.Enum):
    customer = 1
    manager = 2


class User(flask_login.UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), unique=False, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    role = db.Column(db.Enum(UserRole), unique=False, nullable=False)

    booked = db.relationship('Reservation', backref='user', lazy=True)
    

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=False, nullable=False)
    director = db.Column(db.String(60), unique=False, nullable=False)
    duration = db.Column(db.Integer, unique=False, nullable=False)
    main_cast = db.Column(db.String(512), unique=False, nullable=False)
    synopsis = db.Column(db.String(512), unique=False, nullable=False)
    img = db.Column(db.String(512))

    projected = db.relationship('Projection', backref='movie', lazy=True)

class Screen(db.Model):
    __tablename__ = "screen"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    num_total_seats = db.Column(db.Integer, unique=False, nullable=False)

    projected = db.relationship('Projection', backref='screen', lazy=True)

class Projection(db.Model):
    __tablename__ = "projection"
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date(), unique=False, nullable=False)
    time = db.Column(db.Time(), unique=False, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'))

    movie_booked = db.relationship('Reservation', backref='projection', lazy=True)
  

class Reservation(db.Model):
    __tablename__ = "reservation"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    projection_id = db.Column(db.Integer, db.ForeignKey('projection.id'), nullable=False)
    num_seats = db.Column(db.Integer, unique=False, nullable=False)
    date_time = db.Column(db.DateTime(), unique=False, nullable=False)

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

class UserRole:
    manager = 'manager'
    user = 'user'

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
