from flask import Flask, jsonify, request, session
from flask_cors import CORS
from db import get_db
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import os
import json
import docx
import re

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './upload/folder' if 'UPLOAD_FOLDER' not in app.config else app.config['UPLOAD_FOLDER']

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def hello():
    result = []
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    cursor = c.execute("""
        SELECT id, style
        FROM paragraphs
    """)
    conn.commit()
    for row in cursor:
        result.append({
            'paragraph': select_runs(row[0]),
            'style': row[1]
        })
    conn.close()
    return jsonify(result)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        parse_docx(filepath, 'example.db')
        return 'file uploaded sucessfully!'
    else:
        return 'no file uploaded!'

def select_runs(paragraph_id):
    text = []
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    cursor = c.execute("""
        SELECT text, style, bold, color, paragraph_id
        FROM runs
        WHERE paragraph_id = (?)""", 
        (str(paragraph_id),))
    conn.commit()
    for row in cursor:
        text.append({
            'text': row[0],
            'style': row[1],
            'bold': row[2],
            'color': row[3]
        })
    conn.close()
    return text

def parse_docx(docx_file_path, db_file_path):
    doc = docx.Document(docx_file_path)

    conn = sqlite3.connect(db_file_path)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS paragraphs
        (id INTEGER PRIMARY KEY,
        style TEXT)""")
    c.execute("""
        CREATE TABLE IF NOT EXISTS runs
        (id INTEGER PRIMARY KEY,
        text TEXT,
        style TEXT,
        bold INTEGER,
        color TEXT,
        paragraph_id INTEGER,
        FOREIGN KEY (paragraph_id)REFERENCES paragraphs(id))""")

    for para in doc.paragraphs:
        para_text = []
        if re.match(r'\d(\.\d)*\s\S*', str(para.text)):
            c.execute('INSERT INTO paragraphs (style) VALUES (?)', (para.style.name,))
            paragraph_id = c.lastrowid
            for run in para.runs:
                c.execute('INSERT INTO runs (text, style, bold, color, paragraph_id) VALUES (?, ?, ?, ?, ?)', (run.text, run.style.name, run.bold, str(run.font.color.rgb) if run.font.color.rgb else None, paragraph_id))
    
    conn.commit()
    conn.close()

@app.route('/auth/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    db = get_db()

    if not username:
        return jsonify({'error': 'Username is required.'}), 400
    elif not password:
        return jsonify({'error': 'Password is required.'}), 400
    try:
        db.execute(
            "INSERT INTO (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password))
        )
        db.commit()
    except db.IntegrityError:
        return jsonify({'error': f"User {username} is already registered."}), 400
    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = get_db()

    user = db.execute(
        'SELECT * FROM user WHERE username = ?',
        (username,)
    ).fetchone()

    if user in None:
        return jsonify({'error': 'Incorrect username.'}), 401
    elif not check_password_hash(user['password'], password):
        return jsonify({'error': 'Incorrect password.'}), 401
    
    session['username'] = username
    session['logged_in'] = True

    return jsonify({'message': 'User logged successfully.'}), 200

@app.route('/auth/logout')
def logout():
    session.clear()