from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define models for the database tables
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    age = db.Column(db.Integer)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    role = db.Column(db.String(50))

class Doctor(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    speciality = db.Column(db.String(100))
    phone = db.Column(db.String(20))

class InsuranceProvider(db.Model):
    insurance_id = db.Column(db.Integer, primary_key=True)
    insurance_name = db.Column(db.String(100))
    insurance_type = db.Column(db.String(50))
    contact_number = db.Column(db.String(20))
