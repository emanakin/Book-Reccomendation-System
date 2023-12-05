from flask import Blueprint, request, jsonify
from services import AuthService

auth_blueprint = Blueprint('auth', __name__)

auth_service = AuthService()

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = str(data.get('password'))
    location = data.get('Location')
    age = data.get('Age')

    if not all([username, password, location, age]):
        return jsonify({'message': 'Missing data'}), 400

    try:
        user = auth_service.create_user(username, password, location, age)
        token = auth_service.generate_token(user)

        return jsonify({'token': token, 'message': 'User successfully created'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    try:
        token = auth_service.login_user(username, password)
        return jsonify({'token': token}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 401  
