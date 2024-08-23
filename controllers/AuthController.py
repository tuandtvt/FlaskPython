# controllers/AuthController.py

from flask import Blueprint, request, jsonify
from services.AuthService import AuthService
from common.error import generate_error_response 

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = AuthService.register(data)

    return jsonify(result), result['status_code']

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = AuthService.login(data)

    return jsonify(result), result['status_code']

@auth_bp.route('/verify', methods=['GET'])
def verify_email():
    token = request.args.get('token')
    result = AuthService.verify_email(token)

    return jsonify(result), result['status_code']

@auth_bp.route('/user', methods=['GET'])
def get_user_info():
    email = request.args.get('email')
    result = AuthService.get_user_info(email)

    return jsonify(result), result['status_code']
