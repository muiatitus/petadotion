from app import db
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from models import User, Pet, Breed, FavoritePet, Administrator, PostedPet, PetStatus, AdoptionApplication


auth_routes = Blueprint('auth_routes', __name__)
pet_routes = Blueprint('pet_routes', __name__)
favorite_routes = Blueprint('favorite_routes', __name__)
application_routes = Blueprint('application_routes', __name__)


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


# Pet Routes
@pet_routes.route('/pets', methods=['GET'])
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

    return jsonify(message='Application submitted successfully'), 201