from dao import UserDAO 
from flask import g

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def set_preferred_publishers(self, user_id, publishers):
        return self.user_dao.update_preferred_publishers(g.session, user_id, publishers)
    
    def set_authors_publishers(self, user_id, authors):
        return self.user_dao.update_preferred_authors(g.session, user_id, authors)
    
    def rate_book(self, user_id, book_isbn, rating):
        return self.user_dao.rate_book(g.session, user_id, book_isbn, rating)
    
    def get_user_rated_books(self, user_id, page):
        return self.user_dao.fetch_user_rated_books(g.session, user_id, page)

