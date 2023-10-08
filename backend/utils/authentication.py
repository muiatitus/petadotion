from flask import jsonify
from models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import datetime, timedelta

bcrypt = Bcrypt()

# User registration function
def register_user(username, email, password):
    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify(message='Username already exists'), 400

    # Create a new user
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User registered successfully'), 201

# User login function
def login_user(username, password):
    # Find the user by username
    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify(message='Invalid username or password'), 401

    # Generate an access token
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))

    return jsonify(access_token=access_token), 200

# User authentication middleware
def authenticate_user():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return jsonify(message='User not found'), 404

        return user

    except Exception as e:
        return jsonify(message='Authentication failed'), 401

# Other authentication-related functions can be added as needed
