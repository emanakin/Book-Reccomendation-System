from dao import BookDAO, UserDAO, RatingDAO
from services.auth_service import AuthService

class UserService:
    @staticmethod
    def register_user(username, email, password):
        hashed_password = AuthService.hash_password(password)
        return UserDAO.create_user(username, email, hashed_password)
