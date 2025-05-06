from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import logging
import traceback
import os
import time
from .components import render_navbar  # Import the navbar function

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')

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

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for dynamic changes