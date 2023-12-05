from models import Book
from models.base import Base
from sqlalchemy.orm import Session

class BookDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_book_by_isbn(self, isbn):
        return self.session.query(Book).filter(Book.isbn == isbn).first()

    def create_book(self, **kwargs):
        book = Book(**kwargs)
        self.session.add(book)
        self.session.commit()
        return book

    # Add other necessary methods for book operations
