from flask import Blueprint, request, jsonify
from models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)

bcrypt = Bcrypt()

# User registration route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify(message='Username already exists'), 400

    # Create a new user
    new_user = User(username=username, email=email, password=bcrypt.generate_password_hash(password).decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User registered successfully'), 201

# User login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Find the user by username
    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify(message='Invalid username or password'), 401

    # Generate an access token
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))

    return jsonify(access_token=access_token), 200

# Example protected route that requires authentication
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify(message='User not found'), 404

    return jsonify(message=f'Hello, {user.username}! This is a protected route.'), 200

# Logout route (if needed)
# You can implement token revocation logic here

# Other authentication-related routes and functions can be added as needed
