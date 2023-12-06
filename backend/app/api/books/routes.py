from flask import Blueprint, jsonify, request
from services import BookService, RecommendationService

books_blueprint = Blueprint('books', __name__)
book_service = BookService()
recommendation_service = RecommendationService()

@books_blueprint.route('/publishers', methods=['GET'])
def get_publishers():
    page = request.args.get('page', 1, type=int)
    publishers = book_service.get_publishers(page)
    return jsonify(publishers)

@books_blueprint.route('/authors', methods=['GET'])
def get_authors():
    page = request.args.get('page', 1, type=int)
    authors = book_service.get_authors(page)
    return jsonify(authors)

@books_blueprint.route('/sample', methods=['GET'])
def get_sample_books():
    user_id = request.args.get('user_id', type=int)  
    page = request.args.get('page', 1, type=int)
    sample_books = book_service.get_sample_books(user_id, page)
    return jsonify(sample_books)

# RECOMENDATION ALGO 
@books_blueprint.route('/similar-users', methods=['GET'])
def get_books_based_on_similar_users():
    user_id = request.args.get('user_id', type=int)
    recommended_book_ids = recommendation_service.get_books_based_on_similar_users(user_id)
    books = book_service.get_list_of_books(recommended_book_ids)
    return jsonify(books)

@books_blueprint.route('/recommendations', methods=['GET'])
def get_books_based_on_preferences():
    user_id = request.args.get('user_id', type=int)
    page = request.args.get('page', 1, type=int)
    recommended_books = recommendation_service.get_books_based_on_user_preferences(user_id, page)
    return jsonify(recommended_books)

@books_blueprint.route('/popular', methods=['GET'])
def get_popular_books():
    user_id = request.args.get('user_id', type=int)
    page = request.args.get('page', 1, type=int)
    popular_books = recommendation_service.get_popular_books(user_id, page)
    return jsonify(popular_books)


