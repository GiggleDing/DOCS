import functools

from flask import (
    Blueprint, g, request, session, jsonify
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
    print(username)
    password = request.json.get('password')
    print(password)
    db = get_db()

    user = db.execute(
        'SELECT * FROM user WHERE username = ?',
        (username,)
    ).fetchone()

    if user is None:
        return jsonify({'error': 'Incorrect username.'}), 401
    elif not check_password_hash(user['password'], password):
        return jsonify({'error': 'Incorrect password.'}), 401
    
    session.clear()
    session['user_id'] = user['id']

    return jsonify({'message': 'User logged successfully.', 'session_id': session}), 200

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?',
            (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return jsonify({'message': 'User logout successfully.'}), 200

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return jsonify({'message': 'User not logged in.'}), 401
    return wrapped_view

@bp.route('/check_login')
def check_login():
    if g.user is not None:
        return jsonify({'logged_in': True})
    else:
        return jsonify({'logged_in': False})