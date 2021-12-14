from flask import Flask, request, jsonify, render_template
from werkzeug.serving import WSGIRequestHandler
from werkzeug.utils import secure_filename
import os

import main
import Wav2Lip.main

app = Flask(__name__)

@app.route('/face_swap', methods = ['GET', 'POST'])
def face_swap():
    data = request.get_json()

    if 'image' not in data:
        return "", 400
    elif 'templete' not in data:
        return "", 400
    main.convert(data['image'], data['templete'])

#임시 링크
video_path = 'D:/SimSwap/SimSwap/output/demo.mp4'
audio_path = 'D:/SimSwap/SimSwap/output/demoa.wav'

@app.route('/lip', methods = ['GET', 'POST'])
def lip():
    Wav2Lip.main.set_path(video_path, audio_path)
    Wav2Lip.main()

@app.route("/")
def index():
    return "<h1>Welcome to re:mind server !!</h1>"

if __name__ == "__main__":
    # https://stackoverflow.com/questions/63765727/unhandled-exception-connection-closed-while-receiving-data
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(threaded=True, host='127.0.0.1', port=5000)
    ALLOWED_HOSTS = ["*"]