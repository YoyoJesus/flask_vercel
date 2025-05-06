import sqlite3

# Connect to SQLite database
sqlite_db_path = "/tmp/meditrack.db"  # Ensure this matches your Flask app's SQLite path
conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()

# Create tables
cursor.executescript("""
-- Table: patient
CREATE TABLE IF NOT EXISTS patient (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone TEXT,
    email TEXT,
    address TEXT
);

-- Table: doctor
CREATE TABLE IF NOT EXISTS doctor (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    speciality INTEGER,
    phone TEXT,
    email TEXT
);

-- Table: insurance_provider
CREATE TABLE IF NOT EXISTS insurance_provider (
    insurance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    insurance_name TEXT,
    contact_number TEXT,
    insurance_type INTEGER
);

-- Table: appointment
CREATE TABLE IF NOT EXISTS appointment (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    time TEXT,
    status TEXT,
    notes TEXT,
    patient_id INTEGER,
    doctor_id INTEGER,
    hospital_id INTEGER
);
""")

# Insert data into tables
cursor.executemany("""
INSERT INTO patient (patient_id, first_name, last_name, phone, email, address)
VALUES (?, ?, ?, ?, ?, ?);
""", [
    (1, 'Michael', 'Johnson', '555-1111', 'mjohnson@email.com', '123 Oak St, New York, NY'),
    (2, 'Sarah', 'Williams', '555-2222', 'swilliams@email.com', '456 Pine St, Los Angeles, CA'),
    (12, 'Paige', 'Ogden', '123-456-7890', 'paige@kent.edu', 'Kent, Ohio 44243')
])

cursor.executemany("""
INSERT INTO doctor (doctor_id, first_name, last_name, speciality, phone, email)
VALUES (?, ?, ?, ?, ?, ?);
""", [
    (1, 'John', 'Doe', 1, '555-1234', 'jdoe@medcity.com'),
    (2, 'Jane', 'Smith', 2, '555-5678', 'jsmith@carewell.com'),
    (3, 'Emily', 'Jones', 3, '555-8765', 'ejones@medcity.com')
])

cursor.executemany("""
INSERT INTO insurance_provider (insurance_id, insurance_name, contact_number, insurance_type)
VALUES (?, ?, ?, ?);
""", [
    (1, 'HealthPlus', '555-8888', 1),
    (2, 'CareFirst', '555-9999', 2),
    (3, 'SecureCare', '555-1234', 1),
    (4, 'OptiHealth', '555-5678', 3)
])

cursor.executemany("""
INSERT INTO appointment (appointment_id, date, time, status, notes, patient_id, doctor_id, hospital_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
""", [
    (1, '2025-05-01', '09:00:00', 'Scheduled', 'Regular checkup', 1, 1, 1),
    (2, '2025-05-02', '14:00:00', 'Scheduled', 'Routine dental checkup', 2, 2, 2),
    (3, '2025-05-03', '10:00:00', 'Scheduled', 'Follow-up visit', 1, 1, 1),
    (4, '2025-05-04', '11:00:00', 'Scheduled', 'Consultation for teeth cleaning', 2, 2, 2)
])

# Commit changes and close connection
conn.commit()
conn.close()

print("Data migrated successfully to SQLite!")
