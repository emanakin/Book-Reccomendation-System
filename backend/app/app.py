import os
from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import create_engine
from flask import Flask, g
from sqlalchemy.orm import sessionmaker
from api.auth.routes import auth_blueprint
from api.books.routes import books_blueprint
from api.user.routes import user_blueprint

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
KEY = os.getenv("KEY")

app = Flask(__name__)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.before_request
def create_session():
    g.session = Session()

@app.teardown_request
def close_session(exception=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()

app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
app.register_blueprint(books_blueprint, url_prefix='/api/books')
app.register_blueprint(user_blueprint, url_prefix='/api/user')

@app.get('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

app.config['SECRET_KEY'] = KEY
