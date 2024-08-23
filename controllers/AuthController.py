# controllers/AuthController.py

from flask import Blueprint, request, jsonify
from services.AuthService import AuthService
from common.errror import get_error_message

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = AuthService.register(data)
    
    if result['status_code'] >= 400:
        message = get_error_message(result['status_code'])
        return jsonify({'message': message}), result['status_code']
    
    return jsonify(result), result['status_code']

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = AuthService.login(data)
    
    if result['status_code'] >= 400:
        message = get_error_message(result['status_code'])
        return jsonify({'message': message}), result['status_code']
    
    return jsonify(result), result['status_code']

@auth_bp.route('/user', methods=['GET'])
def get_user_info():
    email = request.args.get('email')
    result = AuthService.get_user_info(email)
    
    if result['status_code'] >= 400:
        message = get_error_message(result['status_code'])
        return jsonify({'message': message}), result['status_code']
    
    return jsonify(result), result['status_code']
