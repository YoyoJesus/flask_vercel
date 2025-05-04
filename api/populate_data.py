from api.models import db, Patient, User, Doctor, InsuranceProvider

def populate_database():
    # Check if the database is already populated
    if Patient.query.first() or User.query.first() or Doctor.query.first() or InsuranceProvider.query.first():
        print("Database already populated.")
        return

    # Populate the Patient table
    patients = [
        Patient(first_name="John", last_name="Doe", phone="123-456-7890", address="123 Elm Street", age=30),
        Patient(first_name="Jane", last_name="Smith", phone="987-654-3210", address="456 Oak Avenue", age=25),
        Patient(first_name="Alice", last_name="Johnson", phone="555-123-4567", address="789 Pine Road", age=40)
    ]

    # Populate the User table
    users = [
        User(username="admin", role="Administrator"),
        User(username="doctor1", role="Doctor"),
        User(username="patient1", role="Patient")
    ]

    # Populate the Doctor table
    doctors = [
        Doctor(first_name="Emily", last_name="Brown", speciality="Cardiology", phone="123-456-7890"),
        Doctor(first_name="Michael", last_name="Green", speciality="Neurology", phone="987-654-3210")
    ]

    # Populate the InsuranceProvider table
    insurances = [
        InsuranceProvider(insurance_name="HealthPlus", insurance_type="Health", contact_number="555-123-4567"),
        InsuranceProvider(insurance_name="LifeSecure", insurance_type="Life", contact_number="555-987-6543")
    ]

    # Add the data to the session and commit
    db.session.add_all(patients)
    db.session.add_all(users)
    db.session.add_all(doctors)
    db.session.add_all(insurances)
    db.session.commit()

    print("Database populated with sample data.")
