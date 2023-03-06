import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from DOCX.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    db = get_db()

    if not username:
        return jsonify({'error': 'Username is required.'}), 400
    elif not password:
        return jsonify({'error': 'Password is required.'}), 400
    try:
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db.commit()
    except db.IntegrityError:
        return jsonify({'error': f"User {username} is already registered."}), 400
    return jsonify({'message': 'User registered successfully.'}), 201

@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    db = get_db()

    user = db.execute(
        'SELECT * FROM user WHERE username = ?',
        (username,)
    ).fetchone()

    if user is None:
        return jsonify({'error': 'Incorrect username.'}), 401
    elif not check_password_hash(user['password'], password):
        return jsonify({'error': 'Incorrect password.'}), 401
    
    session['username'] = username
    session['logged_in'] = True

    return jsonify({'message': 'User logged successfully.'}), 200