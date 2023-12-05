from models import User
from models.base import Base
from sqlalchemy.orm import Session

class UserDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create_user(self, **kwargs):
        user = User(**kwargs)
        self.session.add(user)
        self.session.commit()
        return user

    # Add other necessary methods for user operations
