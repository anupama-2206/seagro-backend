from app import create_app

app = create_app()

if __name__ == '__main__':
    # Use SocketIO to run the app
    app.socketio.run(app, host='0.0.0.0', port=5000)
