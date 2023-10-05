from app import db
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from models import User, Pet, Breed, FavoritePet, Administrator, PostedPet, PetStatus, AdoptionApplication

auth_routes = Blueprint('auth_routes', __name__)
pet_routes = Blueprint('pet_routes', __name__)
favorite_routes = Blueprint('favorite_routes', __name__)
application_routes = Blueprint('application_routes', __name__)
breed_routes = Blueprint('breed_routes', __name__)
admin_routes = Blueprint('admin_routes', __name__)
posted_pet_routes = Blueprint('posted_pet_routes', __name__)
pet_status_routes = Blueprint('pet_status_routes', __name__)

# Authentication Routes
@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone = data.get('phone')
    address = data.get('address')

    # Check if the email is already registered
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message='Email already registered'), 409

    # Create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address,
        created_at=datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message='User registered successfully'), 201


@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if the email exists in the database
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify(message='Invalid email or password'), 401

    # Check if the password is correct
    if not check_password_hash(user.password, password):
        return jsonify(message='Invalid email or password'), 401

    # Generate a welcome message
    welcome_message = f'Welcome, {user.username}'

    return jsonify(message=welcome_message), 200


# Pet Routes
@pet_routes.route('/pet', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    pet_list = []
    for pet in pets:
        pet_data = {
            'id': pet.id,
            'name': pet.name,
            'breed': pet.breed.breed_name,
            'age': pet.age,
            'description': pet.description,
            'image_url': pet.image_url,
            'adoption_status': pet.adoption_status,
            'price': pet.price
        }
        pet_list.append(pet_data)

    return jsonify(pet_list)

# Favorite Routes
@favorite_routes.route('/favorites', methods=['GET'])
def get_favorites():
    user_id = request.args.get('user_id')
    favorites = FavoritePet.query.filter_by(user_id=user_id).all()
    favorite_list = []
    for favorite in favorites:
        favorite_data = {
            'id': favorite.id,
            'user_id': favorite.user_id,
            'pet_id': favorite.pet_id,
            'favorite_date': favorite.favorite_date
        }
        favorite_list.append(favorite_data)

    return jsonify(favorite_list)


# Application Routes
@application_routes.route('/applications', methods=['POST'])
def submit_application():
    data = request.get_json()
    user_id = data.get('user_id')
    pet_id = data.get('pet_id')
    submission_date = datetime.now()

    # Check if the user has already submitted an application for the pet
    existing_application = AdoptionApplication.query.filter_by(user_id=user_id, pet_id=pet_id).first()
    if existing_application:
        return jsonify(message='Application already submitted'), 409

    # Create a new application
    new_application = AdoptionApplication(
        user_id=user_id,
        pet_id=pet_id,
        status='Pending',
        submission_date=submission_date
    )
    db.session.add(new_application)
    db.session.commit()

    return jsonify(message='Application submitted successfully'),

# Breed Routes
@breed_routes.route('/breeds', methods=['GET'])
def get_breeds():
    breeds = Breed.query.all()
    breed_list = []
    for breed in breeds:
        breed_data = {
            'id': breed.id,
            'breed_name': breed.breed_name
        }
        breed_list.append(breed_data)

    return jsonify(breed_list)

# Administrator Routes
@admin_routes.route('/administrators', methods=['GET'])
def get_administrators():
    administrators = Administrator.query.all()
    admin_list = []
    for admin in administrators:
        admin_data = {
            'id': admin.id,
            'username': admin.username,
            'email': admin.email,
            'created_at': admin.created_at
        }
        admin_list.append(admin_data)

    return jsonify(admin_list)

@admin_routes.route('/administrators', methods=['POST'])
def create_administrator():
    # Get the data from the request
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if the required fields are provided
    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if an administrator with the same email already exists
    existing_admin = Administrator.query.filter_by(email=email).first()
    if existing_admin:
        return jsonify({'error': 'An administrator with the same email already exists'}), 409

    # Create a new Administrator instance
    new_admin = Administrator(
        username=username,
        email=email,
        password=generate_password_hash(password)
    )

    # Add the new administrator to the database
    db.session.add(new_admin)
    db.session.commit()

    # Return a success message
    return jsonify({'message': 'Administrator created successfully'}), 201

# PostedPet Routes
@posted_pet_routes.route('/posted-pets', methods=['GET'])
def get_posted_pets():
    posted_pets = PostedPet.query.all()
    posted_pet_list = []
    for posted_pet in posted_pets:
        posted_pet_data = {
            'id': posted_pet.id,
            'admin_id': posted_pet.admin_id,
            'pet_id': posted_pet.pet_id,
            'posting_date': posted_pet.posting_date,
            'status_id': posted_pet.status_id
        }
        posted_pet_list.append(posted_pet_data)

    return jsonify(posted_pet_list)

# PetStatus Routes
@pet_status_routes.route('/pet-status', methods=['GET'])
def get_pet_status():
    pet_statuses = PetStatus.query.all()
    pet_status_list = []
    for pet_status in pet_statuses:
        pet_status_data = {
            'id': pet_status.id,
            'status_name': pet_status.status_name
        }
        pet_status_list.append(pet_status_data)

    return jsonify(pet_status_list)