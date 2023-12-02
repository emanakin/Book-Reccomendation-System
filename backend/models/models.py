from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    location = Column(String(64))
    age = Column(Integer)
    user_details = Column(JSON)

    # Relationships
    ratings = relationship('Rating', back_populates='user')
    books = relationship('Book', secondary='user_books')

class Book(Base):
    __tablename__ = 'books'
    isbn = Column(String(12), primary_key=True)
    title = Column(String(256), nullable=False)
    year_of_publisher = Column(Integer)
    publisher = Column(String(256))
    image_url = Column(String(256))

    # Relationships
    ratings = relationship('Rating', back_populates='book')

class Rating(Base):
    __tablename__ = 'ratings'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    isbn = Column(String(12), ForeignKey('books.isbn'), primary_key=True)
    book_rating = Column(Integer)

    # Relationships
    user = relationship('User', back_populates='ratings')
    book = relationship('Book', back_populates='ratings')

class UserBooks(Base):
    __tablename__ = 'user_books'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    isbn = Column(String(12), ForeignKey('books.isbn'), primary_key=True)
