from dao import BookDAO, UserDAO, RatingDAO

class BookService:
    @staticmethod
    def get_all_books():
        return BookDAO.get_all_books()

    # Business logic for book recommendations, etc.
