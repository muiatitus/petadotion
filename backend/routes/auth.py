from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token # Import jwt from app
from models import User
from flask_login import login_user, logout_user, current_user, login_required
from forms.forms import RegistrationForm  # Import the form class
from flask_jwt_extended import create_access_token, create_refresh_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/profile', methods=['GET'])
@jwt_required
def profile():
    current_user_id = get_jwt_identity()
    # Fetch user data based on current_user_id
    user_data = {}  # Replace with actual user data retrieval logic
    return jsonify(user_data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({'message': 'Login successful', 'access_token': access_token, 'refresh_token': refresh_token})
    else:
        return jsonify({'message': 'Invalid credentials'}, 401)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = generate_password_hash(data['password'], method='sha256')

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/logout', methods=['POST'])
@jwt_required
def logout():
    logout_user()  # Use Flask-Login to log out the user
    return jsonify({'message': 'Logout successful'})

@auth_bp.route('/profile', methods=['GET'])
@jwt_required
def profile():
    current_user_id = get_jwt_identity()
    # Fetch user data based on current_user_id
    user_data = {}  # Replace with actual user data retrieval logic
    return jsonify(user_data)
