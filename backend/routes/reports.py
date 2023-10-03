from flask import Blueprint, jsonify
from models import Pet, PetStatus

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/available_pets_report', methods=['GET'])
def available_pets_report():
    available_pets = Pet.query.filter_by(status_id=1).count()  # Assuming status_id 1 means available
    return jsonify({'available_pets_count': available_pets})
