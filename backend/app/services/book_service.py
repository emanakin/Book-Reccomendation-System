from dao import BookDAO
from flask import g

class BookService:
    def __init__(self):
        self.book_dao = BookDAO()

    def get_publishers(self, page):
        return self.book_dao.fetch_publishers(g.session, page)
    
    def get_authors(self, page):
        return self.book_dao.fetch_authors(g.session, page)
    
    def get_sample_books(self, user_id, page):
        return self.book_dao.fetch_sample_books(g.session, user_id, page)

