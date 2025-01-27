import os
import webbrowser
from threading import Timer
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


app = Flask(__name__)
currentPath = os.path.dirname(os.path.abspath(__file__))
serveFile = 'index.html'
socketIo = SocketIO(app, async_mode="eventlet")


@app.route('/')
def index():
    return send_from_directory(currentPath, serveFile)


def serve():
    webbrowser.open("http://localhost:5000")

@socketIo.on('reload')
def reloadChanges():
    print("Changes detected, reloading...")


if __name__ == '__main__':
    Timer(1, serve).start()
    socketIo.run(app, debug=True)

