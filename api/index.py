from flask import Flask, render_template
from dotenv import load_dotenv
from api.models import db, Patient, User, Doctor, InsuranceProvider  # Import db and models
from api.populate_data import populate_database  # Import the function to populate data

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meditrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

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
        return f"Error fetching data: {e}"

# Recreate database tables and populate data
with app.app_context():
    db.drop_all()  # Drop existing tables
    db.create_all()  # Create tables with updated schema
    populate_database()  # Populate the database