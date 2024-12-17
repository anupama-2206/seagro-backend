# app/routes.py
from flask import Blueprint, jsonify
from . import mongo  # Import the MongoDB connection from __init__.py

main = Blueprint('main', __name__)

# Route to get users from MongoDB
@main.route('/api/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    users_list = []
    for user in users:
        users_list.append({
            "id": str(user["_id"]),  # MongoDB uses _id as ObjectId
            "username": user.get("username", ""),
            "email": user.get("email", ""),
            "bio": user.get("bio", "")
        })
    return jsonify(users_list)

# Route to get courses from MongoDB
@main.route('/api/courses', methods=['GET'])
def get_courses():
    courses = mongo.db.courses.find()
    courses_list = []
    for course in courses:
        courses_list.append({
            "id": str(course["_id"]),
            "title": course.get("title", ""),
            "description": course.get("description", "")
        })
    return jsonify(courses_list)

# Route to get jobs from MongoDB
@main.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = mongo.db.jobs.find()
    jobs_list = []
    for job in jobs:
        jobs_list.append({
            "id": str(job["_id"]),
            "title": job.get("title", ""),
            "description": job.get("description", "")
        })
    return jsonify(jobs_list)

# Route to get todos from MongoDB
from flask import Blueprint, jsonify, request
from . import mongo  # Import MongoDB connection

main = Blueprint('main', __name__)

# Existing route to fetch todos
@main.route('/api/todos', methods=['GET'])
def get_todos():
    todos = mongo.db.todos.find()
    todos_list = []
    for todo in todos:
        todos_list.append({
            "id": str(todo["_id"]),
            "task": todo.get("task", ""),
            "user_id": todo.get("user_id", "")
        })
    return jsonify(todos_list)

# New route to add a todo
@main.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_todo = {
        "task": data["task"],
        "user_id": data.get("user_id", 1)  # Default user ID if not provided
    }

    result = mongo.db.todos.insert_one(new_todo)
    return jsonify({"message": "Task added successfully!", "id": str(result.inserted_id)}), 201


# Route to seed dummy data into MongoDB
@main.route('/api/seed-data', methods=['GET'])
def seed_data():
    # Insert dummy data into 'users' collection
    mongo.db.users.insert_many([
        {"username": "JohnDoe", "email": "john@example.com", "bio": "Love coding."},
        {"username": "JaneDoe", "email": "jane@example.com", "bio": "Tech enthusiast."}
    ])

    # Insert dummy data into 'courses' collection
    mongo.db.courses.insert_many([
        {"title": "Web Development", "description": "Learn HTML, CSS, and JavaScript."},
        {"title": "React Development", "description": "Master React and build UI."}
    ])

    # Insert dummy data into 'jobs' collection
    mongo.db.jobs.insert_many([
        {"title": "Frontend Developer", "description": "React developer needed."},
        {"title": "Backend Developer", "description": "Build REST APIs using Python."}
    ])

    # Insert dummy data into 'todos' collection
    mongo.db.todos.insert_many([
        {"task": "Finish project", "user_id": 1},
        {"task": "Read a book", "user_id": 2}
    ])

    return jsonify({"message": "Dummy data seeded into MongoDB successfully!"})
