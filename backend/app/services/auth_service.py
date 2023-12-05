from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask import g
from flask import current_app
from dao import UserDAO

class AuthService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, username, password, location, age):
        hashed_password = self.hash_password(password)
        try:
            user = self.user_dao.create_user(g.session, username, hashed_password, location, age)
            return user
        except Exception as e:
            raise e
        
    def login_user(self, username, password):
        user = self.user_dao.get_user_by_username(g.session, username)
        if user and self.check_password(user.password, str(password)):
            return self.generate_token(username)
        else:
            raise Exception('Invalid username or password')

    @staticmethod
    def generate_token(user):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.username
            }
            # Create the byte string token using the payload and the SECRET key
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            # Return an error in string format if an exception occurs
            return str(e)

    @staticmethod
    def verify_token(token):
        try:
            # Decode the token from the byte string
            payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # The token is expired, return an error string
            return "Expired token. Reauthentication required."
        except jwt.InvalidTokenError:
            # The token is invalid, return an error string
            return "Invalid token. Please log in again."

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hash, password):
        return check_password_hash(hash, password)