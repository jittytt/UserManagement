from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(120), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    mobile = db.Column(db.String(15), unique = True, nullable = False)
    city = db.Column(db.String(50), unique = False, nullable = False)
    designation = db.Column(db.String(50), unique = False, nullable = False)