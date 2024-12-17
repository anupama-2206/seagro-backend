from flask import Blueprint, render_template, current_app
from flask_socketio import emit

# Create a blueprint for the main routes
main = Blueprint('main', __name__)

# Route to render the chat page
@main.route('/chat')
def chat():
    return render_template('chat.html')  # Assuming you have a chat.html template

# Event to handle receiving a message and broadcasting it to other users
@main.after_app_request
def setup_socketio(app):
    socketio = app.socketio  # Access the socketio instance initialized in __init__.py

@socketio.on('send_message')
def handle_message(data):
    print(f"Message received: {data['message']}")
    
    # Broadcast message to all connected clients (including the sender)
    emit('receive_message', data, broadcast=True)

    # Example MongoDB operation: Insert the message into the 'messages' collection
    mongo = current_app.mongo  # Access the app's mongo instance
    messages_collection = mongo.db.messages  # Access the 'messages' collection

    # Insert the message into MongoDB
    messages_collection.insert_one({"message": data['message']})
