from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define models for the database tables
class Patient(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    role = db.Column(db.String(50))

class Doctor(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    speciality = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

class InsuranceProvider(db.Model):
    insurance_id = db.Column(db.Integer, primary_key=True)
    insurance_name = db.Column(db.String(100))
    contact_number = db.Column(db.String(20))
    insurance_type = db.Column(db.Integer)

class Appointment(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    time = db.Column(db.String(8))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(200))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    hospital_id = db.Column(db.Integer)
