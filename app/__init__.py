from flask import Flask
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='./templates')
    bootstrap = Bootstrap5(app)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    return app