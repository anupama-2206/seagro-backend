from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from .routes import main  # Import the routes/blueprint
from .routes import jboard  # Import the jboard blueprint

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

    # Check if the app is connected to the MongoDB
    try:
        # This will try to ping the database to verify the connection
        mongo.cx.admin.command('ping')
        print("MongoDB connected successfully!")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

    # Initialize the SocketIO extension (this is done inside create_app)
    socketio.init_app(app)

    # Register the blueprint for routes
    app.register_blueprint(main)
    app.register_blueprint(jboard)

    # Store the mongo instance to access in routes.py
    app.mongo = mongo

    # Store the socketio instance to access in routes.py
    app.socketio = socketio

    return app
