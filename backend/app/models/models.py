from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

# Association Table for the Many-to-Many relationship between Users and Books
user_books = Table('user_books', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('book_id', String(100), ForeignKey('books.isbn'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(256), unique=True)
    password = Column(String(256))
    location = Column(String(256))
    age = Column(Integer)
    user_details = Column(JSON)

    # Relationships
    ratings = relationship('Rating', back_populates='user')
    # 'books' relationship is defined through the association table 'user_books'
    books = relationship('Book', secondary=user_books, back_populates='users')

class Rating(Base):
    __tablename__ = 'ratings'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    book_isbn = Column(String(100), ForeignKey('books.isbn'), primary_key=True)
    book_rating = Column(Integer)

    # Relationships
    user = relationship('User', back_populates='ratings')
    book = relationship('Book', back_populates='ratings')

class Book(Base):
    __tablename__ = 'books'
    isbn = Column(String(100), primary_key=True)
    title = Column(String(256), nullable=False)
    year_of_publication = Column(Integer)
    publisher = Column(String(256))
    image_url = Column(String(256))
    author = Column(String(256))

    # Relationships
    ratings = relationship('Rating', back_populates='book')
    # 'users' relationship is defined through the association table 'user_books'
    users = relationship('User', secondary=user_books, back_populates='books')
