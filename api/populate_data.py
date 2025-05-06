from api.models import db, Patient, User, Doctor, InsuranceProvider, Appointment

def populate_database():
    # Check if the database is already populated
    if Patient.query.first() or User.query.first() or Doctor.query.first() or InsuranceProvider.query.first():
        print("Database already populated.")
        return

    # Populate the Patient table
    patients = [
        Patient(patient_id=1, first_name="Michael", last_name="Johnson", phone="555-1111", email="mjohnson@email.com", address="123 Oak St, New York, NY"),
        Patient(patient_id=2, first_name="Sarah", last_name="Williams", phone="555-2222", email="swilliams@email.com", address="456 Pine St, Los Angeles, CA"),
        Patient(patient_id=12, first_name="Paige", last_name="Ogden", phone="123-456-7890", email="paige@kent.edu", address="Kent, Ohio 44243")
    ]

    # Populate the User table
    users = [
        User(username="admin", role="Administrator"),
        User(username="doctor1", role="Doctor"),
        User(username="patient1", role="Patient")
    ]

    # Populate the Doctor table
    doctors = [
        Doctor(doctor_id=1, first_name="John", last_name="Doe", speciality=1, phone="555-1234", email="jdoe@medcity.com"),
        Doctor(doctor_id=2, first_name="Jane", last_name="Smith", speciality=2, phone="555-5678", email="jsmith@carewell.com"),
        Doctor(doctor_id=3, first_name="Emily", last_name="Jones", speciality=3, phone="555-8765", email="ejones@medcity.com")
    ]

    # Populate the InsuranceProvider table
    insurances = [
        InsuranceProvider(insurance_id=1, insurance_name="HealthPlus", contact_number="555-8888", insurance_type=1),
        InsuranceProvider(insurance_id=2, insurance_name="CareFirst", contact_number="555-9999", insurance_type=2),
        InsuranceProvider(insurance_id=3, insurance_name="SecureCare", contact_number="555-1234", insurance_type=1),
        InsuranceProvider(insurance_id=4, insurance_name="OptiHealth", contact_number="555-5678", insurance_type=3)
    ]

    # Populate the Appointment table
    appointments = [
        Appointment(appointment_id=1, date="2025-05-01", time="09:00:00", status="Scheduled", notes="Regular checkup", patient_id=1, doctor_id=1, hospital_id=1),
        Appointment(appointment_id=2, date="2025-05-02", time="14:00:00", status="Scheduled", notes="Routine dental checkup", patient_id=2, doctor_id=2, hospital_id=2),
        Appointment(appointment_id=3, date="2025-05-03", time="10:00:00", status="Scheduled", notes="Follow-up visit", patient_id=1, doctor_id=1, hospital_id=1),
        Appointment(appointment_id=4, date="2025-05-04", time="11:00:00", status="Scheduled", notes="Consultation for teeth cleaning", patient_id=2, doctor_id=2, hospital_id=2)
    ]

    # Add the data to the session and commit
    db.session.add_all(patients)
    db.session.add_all(users)
    db.session.add_all(doctors)
    db.session.add_all(insurances)
    db.session.add_all(appointments)
    db.session.commit()

    print("Database populated with sample data.")
