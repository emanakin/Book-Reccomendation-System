from models import Rating
from models.base import Base
from sqlalchemy.orm import Session

class RatingDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_ratings_by_user_id(self, user_id):
        return self.session.query(Rating).filter(Rating.user_id == user_id).all()

    def create_rating(self, **kwargs):
        rating = Rating(**kwargs)
        self.session.add(rating)
        self.session.commit()
        return rating

    # Add other necessary methods for rating operations
