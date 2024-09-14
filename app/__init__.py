from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes from routes.py
from app import routes
