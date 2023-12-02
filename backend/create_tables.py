from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://", 1)

from sqlalchemy import create_engine
from models.models import Base  

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
