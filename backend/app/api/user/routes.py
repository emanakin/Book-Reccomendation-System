from flask import Blueprint, jsonify, request
from services import UserService

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

@user_blueprint.route('/publishers', methods=['POST'])
def set_preferred_publishers():
    data = request.json
    publishers = data.get('publishers')
    user_id = request.args.get('user_id', type=int)
    if user_service.set_preferred_publishers(user_id, publishers):
        return jsonify({'message': 'Preferred publishers updated successfully'}), 200
    else:
        return jsonify({'message': 'Update failed'}), 400

@user_blueprint.route('/authors', methods=['POST'])
def set_preferred_authors():
    data = request.json
    authors = data.get('authors')
    user_id = request.args.get('user_id', type=int)
    if user_service.set_authors_publishers(user_id, authors):
        return jsonify({'message': 'Preferred authors updated successfully'}), 200
    else:
        return jsonify({'message': 'Update failed'}), 400

@user_blueprint.route('/book/rate', methods=['POST'])
def rate_books():
    data = request.json
    book_isbn = data.get('book_isbn')
    rating = data.get('rating')
    user_id = request.args.get('user_id')
    if user_service.rate_book(user_id, book_isbn, rating):
        return jsonify({'message': 'Book rated successfully'}), 200
    else:
        return jsonify({'message': 'Rating failed'}), 400

@user_blueprint.route('/books', methods=['GET'])
def get_user_rated_books():
    user_id = request.args.get('user_id', type=int)
    page = request.args.get('page', 1, type=int)
    rated_books = user_service.get_user_rated_books(user_id, page)
    return jsonify([serialize_book(book) for book in rated_books])

def serialize_book(book):
    return {
        "isbn": book.isbn,
        "title": book.title,
        "author": book.author,
        "publisher": book.publisher,
        "year_of_publication": book.year_of_publication,
        "image_url": book.image_url
    }