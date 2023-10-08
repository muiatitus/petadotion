from flask import Blueprint, request, jsonify
from models import Pet, User
from flask_jwt_extended import jwt_required, get_jwt_identity

pets_bp = Blueprint('pets', __name__)

# Get a list of all available pets
@pets_bp.route('/pets', methods=['GET'])
def get_all_pets():
    pets = Pet.query.filter_by(is_adopted=0).all()
    pet_list = []

    for pet in pets:
        pet_list.append({
            'id': pet.id,
            'name': pet.name,
            'type': pet.type,
            'breed': pet.breed,
            'age': pet.age,
            'description': pet.description,
        })

    return jsonify(pet_list), 200

# Get details of a specific pet
@pets_bp.route('/pets/<int:pet_id>', methods=['GET'])
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
        'is_adopted': pet.is_adopted,
    }

    return jsonify(pet_details), 200

# Create a new pet listing
@pets_bp.route('/pets', methods=['POST'])
@jwt_required()
def create_pet_listing():
    data = request.get_json()
    name = data['name']
    type = data['type']
    breed = data['breed']
    age = data['age']
    description = data['description']

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify(message='User not found'), 404

    new_pet = Pet(name=name, type=type, breed=breed, age=age, description=description, owner_id=current_user_id)
    db.session.add(new_pet)
    db.session.commit()

    return jsonify(message='Pet listing created successfully'), 201

# Update pet listing details
@pets_bp.route('/pets/<int:pet_id>', methods=['PUT'])
@jwt_required()
def update_pet_listing(pet_id):
    data = request.get_json()
    name = data['name']
    type = data['type']
    breed = data['breed']
    age = data['age']
    description = data['description']

    pet = Pet.query.get(pet_id)

    if not pet:
        return jsonify(message='Pet not found'), 404

    # Check if the current user is the owner of the pet
    current_user_id = get_jwt_identity()
    if pet.owner_id != current_user_id:
        return jsonify(message='Permission denied. You are not the owner of this pet.'), 403

    # Update pet details
    pet.name = name
    pet.type = type
    pet.breed = breed
    pet.age = age
    pet.description = description
    db.session.commit()

    return jsonify(message='Pet listing updated successfully'), 200

# Other routes for managing pets, such as adoption requests, can be added as needed
