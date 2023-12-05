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

        if preferred_authors:
            query = session.query(Book).filter(Book.author.in_(preferred_authors))
        if preferred_publishers:
            query = session.query(Book).filter(Book.publisher.in_(preferred_publishers))

        filtered_books = query.limit(10).all()

        # Sort by average rating
        query = query.outerjoin(Rating, Rating.book_isbn == Book.isbn) \
                    .group_by(Book.isbn) \
                    .order_by(func.avg(Rating.book_rating).desc())

        # Pagination
        offset = (page - 1) * 10
        paginated_books = query.offset(offset).limit(10).all()

        return paginated_books

