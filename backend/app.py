from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import timedelta  # Import timedelta for token expiration

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for your app if needed

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Replace with your database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'skrky'  # Replace with your secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Set token expiration time (adjust as needed)

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Initialize JWT (JSON Web Tokens) for authentication
jwt = JWTManager(app)

# Import your models here
from models import User, Pet  # Import your User and Pet models

# Define your routes here

# Example route to create a new user

# Create a new pet listing
@app.route('/pets', methods=['POST'])
@jwt_required()  # Secure this route, requires authentication
def create_pet_listing():
    data = request.get_json()
    name = data['name']
    type = data['type']
    breed = data['breed']
    age = data['age']
    description = data['description']

    # Get the user ID from the token
    owner_id = get_jwt_identity()

    # Create a new pet with the owner's ID
    new_pet = Pet(name=name, type=type, breed=breed, age=age, description=description, owner_id=owner_id)

    db.session.add(new_pet)
    db.session.commit()

    return jsonify(message='Pet listing created successfully'), 201

# Route to get user data
@app.route('/api/user', methods=['GET'])
@jwt_required()
def get_user_data():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify(error='User not found'), 404

    user_data = {
        'username': user.username,
        'email': user.email,
        # Add more user-specific fields as needed
    }

    return jsonify(user_data), 200

@app.route('/pets', methods=['GET'])
def get_all_pets():
    pets = Pet.query.all()

    pet_list = []
    for pet in pets:
        pet_details = {
            'id': pet.id,
            'name': pet.name,
            'type': pet.type,
            'breed': pet.breed,
            'age': pet.age,
            'description': pet.description,
            'is_adopted': pet.is_adopted,
            'created_at': pet.created_at,
            'owner_id': pet.owner_id,
        }
        pet_list.append(pet_details)

    return jsonify(pet_list), 200

# Get details of a specific pet
@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet_details(pet_id):
    pet = Pet.query.get(pet_id)

    if not pet:
        return jsonify(message='Pet not found'), 404

    pet_details = {
        'id': pet.id,
        'name': pet.name,
        'type': pet.type,
        'breed': pet.breed,
        'age': pet.age,
        'description': pet.description,
    }

    return jsonify(pet_details), 200

# Route for user profile editing
@app.route('/profile/edit', methods=['PUT'])
@jwt_required()
def edit_profile():
    data = request.get_json()
    user_id = get_jwt_identity()  # Get the user ID from the token

    # You can add more fields to update here, such as username, email, etc.
    # Example: username = data.get('username')

    if user_id is None:
        return jsonify(message='User ID is missing'), 400

    user = User.query.get(user_id)

    if not user:
        return jsonify(message='User not found'), 404

    # Update user profile fields here
    # Example: user.username = username

    # Save the changes to the database
    db.session.commit()

    return jsonify(message='Profile updated successfully'), 200

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    # Check if the user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message='Email address is already in use'), 400

    # Create a new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Generate an access token on successful registration
    access_token = create_access_token(identity=new_user.id)

    return jsonify(message='User registered successfully', access_token=access_token), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(message='Username and password are required'), 400

    try:
        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify(message='Invalid username or password'), 401

        # Generate an access token on successful login
        access_token = create_access_token(identity=user.id)

        return jsonify(access_token=access_token), 200

    except Exception as e:
        # Handle exceptions or database errors gracefully
        return jsonify(message='An error occurred while processing your request'), 500

if __name__ == '__main__':
    app.run(debug=True)
