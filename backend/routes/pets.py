from flask import Blueprint, jsonify
from models import Pet

pets_bp = Blueprint('pets', __name__)


@pets_bp.route('/pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    pet_list = []
    for pet in pets:
        pet_list.append({
            'id': pet.id,
            'name': pet.name,
            'age': pet.age,
            # Include other pet attributes here
        })
    return jsonify({'pets': pet_list})
