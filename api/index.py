from flask import Flask, render_template
from dotenv import load_dotenv
from api.models import db, Patient, User, Doctor, InsuranceProvider  # Import db and models
from api.populate_data import populate_database  # Import the function to populate data
import logging
import traceback
import os

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')

# Ensure the database path is in the writable /tmp directory
db_path = os.path.join('/tmp', 'meditrack.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/datacheck')
def show_patients():
    try:
        # Fetch data from the database
        patients = Patient.query.all()
        users = User.query.all()
        doctors = Doctor.query.all()
        insurances = InsuranceProvider.query.all()

        return render_template(
            'check.html',
            patients=patients,
            users=users,
            doctors=doctors,
            insurances=insurances
        )
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        logging.error(traceback.format_exc())
        return f"Error fetching data: {e}"

# Recreate database tables and populate data
try:
    with app.app_context():
        # Ensure the /tmp directory exists
        if not os.path.exists('/tmp'):
            os.makedirs('/tmp')

        db.drop_all()  # Drop existing tables
        db.create_all()  # Create tables with updated schema
        populate_database()  # Populate the database
except Exception as e:
    logging.error(f"Error during database setup: {e}")