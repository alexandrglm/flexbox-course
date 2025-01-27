import os
import webbrowser
from threading import Timer
from flask import Flask, send_from_directory

app = Flask(__name__)
currentPath = os.path.dirname(os.path.abspath(__file__))
serveFile = 'index.html'


@app.route('/')
def index():
    return send_from_directory(currentPath, serveFile)

def serve():
    webbrowser.open("http://localhost:5000")

if __name__ == '__main__':
    Timer(1, serve).start()
    app.run(debug=True, use_reloader=True)

