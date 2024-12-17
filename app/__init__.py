from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from .routes import main  # Import the routes/blueprint

# Initialize the MongoDB and SocketIO instances here
mongo = PyMongo()  # MongoDB will be initialized later in create_app
socketio = SocketIO()  # SocketIO will be initialized later in create_app

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # MongoDB URI configuration
    app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"  # Replace with your MongoDB URI
    app.config['SECRET_KEY'] = 'secret!'  # Secret key for sessions

    # Initialize the MongoDB extension (this is done inside create_app)
    mongo.init_app(app)

    # Initialize the SocketIO extension (this is done inside create_app)
    socketio.init_app(app)

    # Register the blueprint for routes
    app.register_blueprint(main)

    # Store the mongo instance to access in routes.py
    app.mongo = mongo

    # Store the socketio instance to access in routes.py
    app.socketio = socketio

    return app
