from flask import Flask, request, jsonify, render_template
from werkzeug.serving import WSGIRequestHandler
from werkzeug.utils import secure_filename
import os
import base64
import main
from Wav2Lip.wav2lip_main import wav2_main

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
output_path = 'D:/Unity Project/Unity-Study/Flutter/assets/demo.mp4' # write your output path
app = Flask(__name__)


@app.route('/face_swap', methods=['GET', 'POST'])
def face_swap():
    data = request.get_json()

    if 'image' not in data:
        return "", 400
    elif 'templete' not in data:
        return "", 400
    main.convert(data['image'], data['templete'])


@app.route('/lip', methods=['GET', 'POST'])
def lip():
    data = request.get_json()

    if 'image' not in data:
        return "", 400
    elif 'templete' not in data:
        return "", 400
    elif 'audio' not in data:
        return "", 400
    main.convert(data['image'], data['templete'])

    file = base64.b64decode(data['audio'])


    audio_path = './demo_file/voice.wav'
    wav_file = open(audio_path, "wb")
    wav_file.write(file)
    wav2_main(output_path, audio_path)

@app.route('/video/<string:file_name>', methods=['GET', 'POST'])
def home(file_name):
    return render_template('index.html', file_name=file_name)

@app.route("/")
def index():
    return "<h1>Welcome to re:mind server !!</h1>"

if __name__ == "__main__":
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(threaded=True, host='127.0.0.1', port=5000)
    ALLOWED_HOSTS = ["*"]