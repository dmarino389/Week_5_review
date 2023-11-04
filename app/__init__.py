# These are my Imports
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# This imorts routes.py from the app folder which initializes all my routes in the app
from app import routes