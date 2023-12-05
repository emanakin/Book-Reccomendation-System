import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask
from api.auth.routes import auth_blueprint
from api.author.routes import author_blueprint
from api.books.routes import books_blueprint
from api.publisher.routes import publisher_blueprint
from api.user.routes import user_blueprint

load_dotenv()

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
app.register_blueprint(author_blueprint, url_prefix='/api/author')
app.register_blueprint(books_blueprint, url_prefix='/api/books')
app.register_blueprint(publisher_blueprint, url_prefix='/api/publisher')
app.register_blueprint(user_blueprint, url_prefix='/api/user')


url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get('/')
def home():
    return 'Hello, World!'

