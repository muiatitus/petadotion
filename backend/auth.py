from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt
from models import User
from validators import validate_email, validate_password

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate email and password
    if not validate_email(email) or not validate_password(password):
        return jsonify(message='Invalid email or password'), 400

    # Check if the user exists
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify(message='Invalid email or password'), 401

    # Generate JWT token
    token = jwt.encode(
        {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=1)
        },
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )

    return jsonify(token=token.decode('utf-8'))

@auth_routes.route('/logout', methods=['POST'])
def logout():
    # Perform logout logic here
    return jsonify(message='Logged out successfully')