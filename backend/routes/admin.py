from flask import Blueprint, request, jsonify, current_app
from models import Administrator, Pet, PetStatus
from flask_login import login_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/add_pet', methods=['POST'])
@login_required  # Protect this route for administrators only
def add_pet():
    if current_user.role != 'admin':
        return jsonify({'message': 'Unauthorized'}, 401)

    data = request.get_json()
    name = data['name']
    age = data['age']
    # Add more pet details as needed

    # Create a new pet and set its initial status
    pet = Pet(name=name, age=age, status_id=1)  # Assuming status_id 1 means available
    db.session.add(pet)
    db.session.commit()

    return jsonify({'message': 'Pet added successfully'})
