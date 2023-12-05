from flask import Blueprint, jsonify, request
from dao import BookDAO, UserDAO, RatingDAO

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/sample', methods=['GET'])
def get_sample_books():
    sample_books = BookDAO.get_sample_books()  # Assuming you have a method for this in BookDAO
    return jsonify(sample_books), 200

@books_blueprint.route('/similar-users', methods=['GET'])
def get_books_based_on_similar_users():
    user_id = request.args.get('user_id')  # Replace with actual user identification logic
    similar_books = BookDAO.get_books_for_similar_users(user_id)
    return jsonify(similar_books), 200

@books_blueprint.route('/recommendations', methods=['GET'])
def get_books_based_on_preferences():
    user_id = request.args.get('user_id')  # Replace with actual user identification logic
    recommendations = BookDAO.get_user_recommendations(user_id)
    return jsonify(recommendations), 200

@books_blueprint.route('/popular', methods=['GET'])
def get_popular_books():
    popular_books = BookDAO.get_popular_books()
    return jsonify(popular_books), 200

