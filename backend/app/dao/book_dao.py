from sqlalchemy import func
from models import Book, User, Rating

class BookDAO:
    def get_book_by_isbn(self, session, isbn):
        return session.query(Book).filter(Book.isbn == isbn).first()

    def fetch_publishers(self, session, page, per_page=10):
        offset = (page - 1) * per_page
        publishers = session.query(Book.publisher).distinct().order_by(Book.publisher).offset(offset).limit(per_page).all()
        return [publisher[0] for publisher in publishers]

    def fetch_authors(self, session, page, per_page=10):
        offset = (page - 1) * per_page
        authors = session.query(Book.author).distinct().order_by(Book.author).offset(offset).limit(per_page).all()
        return [author[0] for author in authors]

    def fetch_sample_books(self, session, user_id, page):
        user = session.query(User).filter(User.id == user_id).first()

        if not user:
            print("No user found with ID:", user_id)
            return []

        preferred_authors = user.user_details.get('preferred_authors', [])
        preferred_publishers = user.user_details.get('preferred_publishers', [])
        print(preferred_authors)
        if preferred_authors:
            query = session.query(Book).filter(Book.author.in_(preferred_authors))
        if preferred_publishers:
            query = session.query(Book).filter(Book.publisher.in_(preferred_publishers))

        # Sort by average rating
        query = query.outerjoin(Rating, Rating.book_isbn == Book.isbn) \
                    .group_by(Book.isbn) \
                    .order_by(func.avg(Rating.book_rating).desc())

        offset = (page - 1) * 10
        books = query.offset(offset).limit(10).all()

        return ([self.serialize_book(book) for book in books])

    def bulk_fetch_books(self, session, list_of_isbns):
        books_query = session.query(Book).filter(Book.isbn.in_(list_of_isbns)).all()
        return ([self.serialize_book(book) for book in books_query])
    
    def fetch_popular_books(self, session, user_preferences, page):
        offset = (page - 1) * 10
        limit = 10  

        # Apply filters based on user's preferred authors and publishers
        if user_preferences.get('preferred_authors'):
            query = session.query(Book, func.avg(Rating.book_rating).label('average_rating')) \
                            .join(Rating, Rating.book_isbn == Book.isbn) \
                            .group_by(Book.isbn).filter(Book.author.in_(user_preferences['preferred_authors']))
            
        if user_preferences.get('preferred_publishers'):
            query = session.query(Book, func.avg(Rating.book_rating).label('average_rating')) \
                            .join(Rating, Rating.book_isbn == Book.isbn) \
                            .group_by(Book.isbn).filter(Book.publisher.in_(user_preferences['preferred_publishers']))

        # Sort the result by average rating in descending order
        query = query.order_by(func.avg(Rating.book_rating).desc())
        popular_books = query.offset(offset).limit(limit).all()

        return [self.serialize_book(result[0]) for result in popular_books]

    def fetch_books_by_preferences(self, session, user_preferences, user_rated_books, page):
        offset = (page - 1) * 10
        limit = 10  

        if user_preferences.get('preferred_authors'):
            query = session.query(Book).filter(Book.author.in_(user_preferences['preferred_authors']))
        if user_preferences.get('preferred_publishers'):
            query = session.query(Book).filter(Book.publisher.in_(user_preferences['preferred_publishers']))

        query = query.filter(Book.isbn.notin_(user_rated_books))

        books = query.offset(offset).limit(limit).all()
        return ([self.serialize_book(book) for book in books])

    @staticmethod
    def serialize_book(book):
        return {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "publisher": book.publisher,
            "year_of_publication": book.year_of_publication,
            "image_url": book.image_url
        }