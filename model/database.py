from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    car_license = db.Column(db.String(20), nullable=False)
    car_engine = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Default to current time
    
    appointments = db.relationship("Appointment", back_populates="user")

class Mechanic(db.Model):
    __tablename__ = "mechanics"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    apt_number = db.Column(db.Integer, default=0)  # Changed default_value to default

    appointments = db.relationship("Appointment", back_populates="mechanic")

class Appointment(db.Model):
    __tablename__ = "appointments"
    __table_args__ = (
        UniqueConstraint('user_id', 'mechanic_id', name='_user_mechanic_unique'),
    )
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanics.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", back_populates="appointments", uselist=False)
    mechanic = db.relationship("Mechanic", back_populates="appointments", uselist=False)
