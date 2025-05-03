from flask import Flask, render_template
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')

# MySQL database configuration
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DB')
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/datacheck')
def show_patients():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Fetch patients
        cursor.execute("SELECT * FROM patient")
        patients = cursor.fetchall()

        # Fetch users
        cursor.execute("SELECT id, username, role FROM users")
        users = cursor.fetchall()

        # Fetch doctors
        cursor.execute("SELECT doctor_id, first_name, last_name, speciality, phone FROM doctor")
        doctors = cursor.fetchall()

        # Fetch insurance providers
        cursor.execute("SELECT insurance_id, insurance_name, insurance_type, contact_number FROM insurance_provider")
        insurances = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template(
            'check.html',
            patients=patients,
            users=users,
            doctors=doctors,
            insurances=insurances
        )
    except Exception as e:
        return f"Error fetching data: {e}"