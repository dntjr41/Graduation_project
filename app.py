from flask import Flask, request, jsonify, render_template
from werkzeug.serving import WSGIRequestHandler
from werkzeug.utils import secure_filename
import os

import main

app = Flask(__name__)

@app.route('/face_swap', methods = ['GET', 'POST'])
def face_swap():
    data = request.get_json()

    if 'image' not in data:
        return "", 400

    main.convert(data['image'])


@app.route("/")
def index():
    return "<h1>Welcome to re:mind server !!</h1>"

if __name__ == "__main__":
    # https://stackoverflow.com/questions/63765727/unhandled-exception-connection-closed-while-receiving-data
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(threaded=True, host='127.0.0.1', port=5000)
    ALLOWED_HOSTS = ["*"]