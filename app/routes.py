from flask import Blueprint, render_template, current_app
from flask_socketio import emit

# Create a blueprint for the main routes
main = Blueprint('main', __name__)
jboard = Blueprint('jboard', __name__)

# Route to fetch job listings
@jboard.route('/api/jobs', methods=['GET'])
def get_jobs():
    print("Jobs")
    # Access the jobs collection
    jobs = mongo.db.jobs.find()  # 'jobs' is the name of the collection
    
    # Format the data into a list of dictionaries
    job_list = []
    for job in jobs:
        job_data = {
            'id': str(job['_id']),  # Convert ObjectId to string
            'title': job['title'],
            'description': job['description']
        }
        job_list.append(job_data)
    
    return jsonify(job_list)

@main.route('/chat')
def chat():
    # Insert a test document into the 'messages' collection
    mongo = current_app.mongo
    messages_collection = mongo.db.messages
    messages_collection.insert_one({"message": "Test message"})
    return render_template('chat.html')

# Event to handle receiving a message and broadcasting it to other users
@main.before_app_request
def setup_socketio():
    socketio = current_app.socketio  # Access socketio from the current app
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
