from flask import Blueprint, jsonify, request
from services import BookService

books_blueprint = Blueprint('books', __name__)
book_service = BookService()

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
    return jsonify([serialize_book(book) for book in sample_books])

# RECOMENDATION ALGO 
@books_blueprint.route('/similar-users', methods=['GET'])
def get_books_based_on_similar_users():
    pass

@books_blueprint.route('/recommendations', methods=['GET'])
def get_books_based_on_preferences():
    pass

@books_blueprint.route('/popular', methods=['GET'])
def get_popular_books():
    pass

def serialize_book(book):
    return {
        "isbn": book.isbn,
        "title": book.title,
        "author": book.author,
        "publisher": book.publisher,
        "year_of_publication": book.year_of_publication,
        "image_url": book.image_url
    }
