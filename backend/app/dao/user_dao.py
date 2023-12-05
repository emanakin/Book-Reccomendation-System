from models import User, Rating, Book
from sqlalchemy import func

class UserDAO:
    def get_user_by_username(self, session, username):
        return session.query(User).filter(User.username == username).first()

    def create_user(self, session, username, password, location, age, user_details={}):
        highest_id = session.query(func.max(User.id)).scalar()
        next_id = highest_id + 1 if highest_id is not None else 1

        user = User(id=next_id, username=username, password=password, location=location, age=age, user_details=user_details)
        session.add(user)
        session.commit()
        return user
    
    def update_preferred_publishers(self, session, user_id, publishers):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        
        if user.user_details is None:
            user.user_details = {}
            
        user.user_details['preferred_publishers'] = publishers
        
        try:
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            return False
   
    def update_preferred_authors(self, session, user_id, authors):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        
        if user.user_details is None:
            user.user_details = {}
            
        user.user_details['preferred_authors'] = authors
        
        try:
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            return False
        
    def rate_book(self, session, user_id, book_isbn, rating):
        existing_rating = session.query(Rating).filter_by(user_id=user_id, book_isbn=book_isbn).first()

        if existing_rating:
            existing_rating.book_rating = rating
        else:
            new_rating = Rating(user_id=user_id, book_isbn=book_isbn, book_rating=rating)
            session.add(new_rating)
        
        session.commit()
        return True

    def fetch_user_rated_books(self, session, user_id, page):
        offset = (page - 1) * 10

        rated_books_query = session.query(Book).join(Rating, Rating.book_isbn == Book.isbn).filter(Rating.user_id == user_id)

        rated_books = rated_books_query.offset(offset).limit(10).all()
        return rated_books
