from flask import Flask
from flask_pymongo import PyMongo
from .routes import main  # Import the main Blueprint
from .routes import jboard  # Import the jboard Blueprint

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # MongoDB URI configuration
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # Replace with your MongoDB URI

    # Initialize the MongoDB extension and pass the app configuration
    mongo = PyMongo(app)

    # Register Blueprints
    app.register_blueprint(main)  # Register the main blueprint
    app.register_blueprint(jboard)  # Register the jboard blueprint

    # Store the mongo instance to access in routes.py
    app.mongo = mongo

    return app
