from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from yourapp import db
import jwt
import datetime
from flask import current_app
from dao import BookDAO, UserDAO, RatingDAO


class AuthService:
    @staticmethod
    def generate_token(user):
        try:
            # Set up a payload with an expiration time
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.id
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
