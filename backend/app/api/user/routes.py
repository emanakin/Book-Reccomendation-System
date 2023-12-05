from flask import Blueprint, jsonify, request
from dao import BookDAO, UserDAO, RatingDAO

user_blueprint = Blueprint('publisher', __name__)

@user_blueprint.route('/publishers', methods=['POST'])
def set_preferred_publishers():
    # Implement preferred publishers logic here
    pass

@user_blueprint.route('/books/rating', methods=['POST'])
def rate_books():
    data = request.json
    user_id = data.get('user_id')  # Replace with actual user identification logic, e.g., from token
    ratings = data.get('ratings')
    success = RatingDAO.save_ratings(user_id, ratings)
    return jsonify({'success': success}), 200 if success else 400

@user_blueprint.route('/books', methods=['GET'])
def get_user_rated_books():
    user_id = request.args.get('user_id')  # Replace with actual user identification logic
    user_books = RatingDAO.get_user_rated_books(user_id)
    return jsonify(user_books), 200