from flask_sqlalchemy import SQLAlchemy 
import datetime
from sqlalchemy import Column, Integer, DateTime
db=SQLAlchemy()
class Register(db.Model):
    __tablename__="Register"
    # id=db.Column(db.String,nullable=False)
    fname=db.Column(db.String,nullable=False)
    lname=db.Column(db.String,nullable=False)
    email=db.Column(db.String,primary_key=True)
    password=db.Column(db.String,nullable=False)
    time=db.Column(DateTime, default=datetime.datetime.utcnow)

class Book(db.Model):
    __tablename__="Book"
    isbn=db.Column(db.String,primary_key=True)
    name=db.Column(db.String,nullable=False)
    author=db.Column(db.String,nullable=False)
    year=db.Column(db.String,nullable=False)
