from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from dotenv import load_dotenv
import logging
import traceback
import os
import time
import json  # Import JSON module for reading config.json
from .components import render_navbar  # Import the navbar function

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Set a secret key for sessions

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('index.html', navbar=render_navbar())

@app.route('/about')
def about():
    return render_template('about.html', navbar=render_navbar())

@app.route('/projects')
def projects():
    return render_template('projects.html', navbar=render_navbar())


@app.route('/resume')
def resume():
    return render_template('resume.html', navbar=render_navbar())

@app.route('/contact')
def contact():
    return render_template('contact.html', navbar=render_navbar())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == os.getenv("ADMIN_USERNAME") and password == os.getenv("ADMIN_PASSWORD"):
            session['logged_in'] = True
            logging.info(f"Successful login attempt by user: {username}")
            return redirect(url_for('admin'))
        else:
            logging.warning(f"Failed login attempt with username: {username}")
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            posts = request.json
            config_path = os.path.join(os.path.dirname(__file__), '../social_posts.json')  # Absolute path
            with open(config_path, 'w') as file:
                json.dump(posts, file, indent=4)
            return jsonify({"success": True})
        except Exception as e:
            logging.error("Error saving posts: %s", traceback.format_exc())
            return jsonify({"error": "Failed to save posts"}), 500
    return render_template('admin.html', navbar=render_navbar())

@app.route('/api/social-posts', methods=['GET'])
def get_social_posts():
    try:
        config_path = os.path.join(os.path.dirname(__file__), '../social_posts.json')  # Absolute path
        with open(config_path) as file:
            posts = json.load(file)
        return jsonify(posts)
    except Exception as e:
        logging.error("Error loading posts: %s", traceback.format_exc())
        return jsonify({"error": "Failed to load posts"}), 500

@app.route('/typing-effect')
def typing_effect():
    roles = [
        "Cybersecurity Enthusiast",
        "Hackathon Coordinator",
        "Researcher",
        "Hobbyist Web Developer",
        "Tech Enthusiast",
        "Student",
        "Battlebots Enthusiast",
        "Board Game Enthusiast",
        "D&D Player",
        "Problem Solver",
        "Science Fiction Fan",
        "All Around Nerd",
    ]
    role_index = int(time.time() / 5) % len(roles)  # Change role every 5 seconds
    current_role = roles[role_index]
    return jsonify(role=current_role)

@app.route('/api/credentials', methods=['GET'])
def get_credentials():
    try:
        config_path = os.path.join(os.path.dirname(__file__), '../config.json')  # Path to config.json
        with open(config_path) as config_file:
            credentials = json.load(config_file)
        return jsonify({
            "publicKey": credentials["publicKey"],
            "serviceID": credentials["serviceID"],
            "templateID": credentials["templateID"]
        })
    except Exception as e:
        logging.error("Error loading credentials: %s", traceback.format_exc())
        return jsonify({"error": "Failed to load credentials"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for dynamic changes