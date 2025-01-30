import os
import webbrowser
from threading import Timer
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)
socketIo = SocketIO(app, async_mode="eventlet")

currentPath = os.path.dirname(os.path.abspath(__file__))
serveFile = 'index.html'


@app.route('/')
def index():
    return send_from_directory(currentPath, serveFile)


class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".html"):
            print(f"Detected change in {event.src_path}, reloading...")
            socketIo.emit('reload')  # Envía evento de recarga al cliente


def serve():
    webbrowser.open("http://localhost:5000")


if __name__ == '__main__':
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=currentPath, recursive=False)
    observer.start()

    Timer(1, serve).start()

    try:
        socketIo.run(app, debug=True)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
