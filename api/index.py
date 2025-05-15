from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from dotenv import load_dotenv
import logging
import traceback
import os
import time
import json  # Import JSON module for reading config.json
from .components import render_navbar, render_footer  # Import the navbar and footer functions

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Set a secret key for sessions

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    return render_template('index.html', navbar=render_navbar(), footer=render_footer())

@app.route('/about')
def about():
    return render_template('about.html', navbar=render_navbar(), footer=render_footer())

@app.route('/projects')
def projects():
    return render_template('projects.html', navbar=render_navbar(), footer=render_footer())

@app.route('/resume')
def resume():
    return render_template('resume.html', navbar=render_navbar(), footer=render_footer())

@app.route('/contact')
def contact():
    return render_template('contact.html', navbar=render_navbar(), footer=render_footer())

@app.route('/movies')
def movies():
    # Load movies and tv_shows from movies.json
    movies_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(movies_path, encoding='utf-8') as f:
        data = json.load(f)
    return render_template('movies.html', navbar=render_navbar(), footer=render_footer(),
                           movies=data['movies'], tv_shows=data['tv_shows'])

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
            flash("Invalid credentials", "danger")
            return render_template('login.html')
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
        # Only handle JSON requests for social posts
        if request.is_json:
            try:
                posts = request.json
                config_path = os.path.join(os.path.dirname(__file__), '../social_posts.json')
                with open(config_path, 'w') as file:
                    json.dump(posts, file, indent=4)
                return jsonify({"success": True})
            except Exception as e:
                logging.error("Error saving posts: %s", traceback.format_exc())
                return jsonify({"error": "Failed to save posts"}), 500
        # If not JSON, ignore and fall through to render the page
        return redirect(url_for('admin'))
    # Load movies and tv_shows from movies.json
    movies_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(movies_path, encoding='utf-8') as f:
        data = json.load(f)
    return render_template('admin.html', navbar=render_navbar(), footer=render_footer(),
                           movies=data['movies'], tv_shows=data['tv_shows'])

@app.route('/admin/add_movie', methods=['POST'])
def add_movie():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    movie = request.form.get('movie')
    movies_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(movies_path, encoding='utf-8') as f:
        data = json.load(f)
    if movie and movie not in data['movies']:
        data['movies'].append(movie)
        with open(movies_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        flash(f"Added movie: {movie}", "success")
    else:
        flash("Movie already exists or invalid input.", "warning")
    return redirect(url_for('admin'))

@app.route('/admin/add_tv', methods=['POST'])
def add_tv():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tv_show = request.form.get('tv_show')
    movies_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(movies_path, encoding='utf-8') as f:
        data = json.load(f)
    if tv_show and tv_show not in data['tv_shows']:
        data['tv_shows'].append(tv_show)
        with open(movies_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        flash(f"Added TV show: {tv_show}", "success")
    else:
        flash("TV show already exists or invalid input.", "warning")
    return redirect(url_for('admin'))

@app.route('/admin/delete_movie', methods=['POST'])
def delete_movie():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    movie = request.form.get('movie')
    movies_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(movies_path, encoding='utf-8') as f:
        data = json.load(f)
    if movie in data['movies']:
        data['movies'].remove(movie)
        with open(movies_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        flash(f"Deleted movie: {movie}", "success")
    else:
        flash("Movie not found.", "warning")
    return redirect(url_for('admin'))

@app.route('/admin/delete_tv', methods=['POST'])
def delete_tv():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    tv_show = request.form.get('tv_show')
    movies_path = os.path.join(os.path.dirname(__file__), '../movies.json')
    with open(movies_path, encoding='utf-8') as f:
        data = json.load(f)
    if tv_show in data['tv_shows']:
        data['tv_shows'].remove(tv_show)
        with open(movies_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        flash(f"Deleted TV show: {tv_show}", "success")
    else:
        flash("TV show not found.", "warning")
    return redirect(url_for('admin'))

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
        credentials = {
            "publicKey": os.getenv("PUBLIC_KEY"),
            "serviceID": os.getenv("SERVICE_ID"),
            "templateID": os.getenv("TEMPLATE_ID")
        }
        return jsonify(credentials)
    except Exception as e:
        logging.error("Error loading credentials: %s", traceback.format_exc())
        return jsonify({"error": "Failed to load credentials"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for dynamic changes