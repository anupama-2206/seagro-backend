# app/models.py
# You do not need to import db from __init__.py as MongoDB is initialized in create_app()

# If you need to define MongoDB-related functions, you can do so here.
# Example MongoDB operation: User collection
def get_user_collection(app):
    mongo = app.mongo  # Access the app's mongo instance
    return mongo.db.users
