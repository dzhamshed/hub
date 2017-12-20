#!/usr/bin/python

import os, sys

cd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cd)

sys.path.insert(0, os.path.join(cd, 'libs'))


from core.videostreamer import VideoStreamer
from modules.intelligentprocessing import IntelligentProcessing
from modules.emotionrecognition import EmotionRecognition
from modules.situationrecognition import SituationRecognition
from modules.objectrecoginition import ObjectRecognition
from moviepy.editor import *
from core.database import  pg

# first extract audio from video
clip = VideoFileClip(os.path.dirname(os.path.abspath(__file__)) + '/match.mp4')
# clip.audio.write_audiofile('sound.mp3')

IP = IntelligentProcessing()
ER = EmotionRecognition()
SR = SituationRecognition()
OR = ObjectRecognition(clip.size[0], clip.size[1])


from flask import Flask, Response
from flask_socketio import SocketIO, send, emit
app = Flask(__name__)

import logging, json
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app.config['SECRET_KEY'] = '@SUPERSAFE!'
socketio = SocketIO(app)
streamframe = None
crop = None


def start_cycle(chunk):
    global crop
    emotion = ER.getemotion(chunk)
    print('emotion -> ', emotion)
    situation = SR.getsituation(streamframe)
    print('situation -> ', situation)
    coordinates = OR.getcoordinates(streamframe)
    crop = IP.getobject(emotion, situation, coordinates)
    print('crop -> ', crop)
    coords = '(' + str(crop['lx']) + ', ' + str(crop['ly']) + ') x (' + str(crop['rx']) + ', ' + str(crop['ry']) + ')'

    emit('output_log', emotion + ' | ' + situation + ' | ' + coords, broadcast=True)


def streamhandler(streamer):
    while True:
        frame = streamer.get_frame(crop)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def audiohandler():
    with open('sound.mp3', 'rb') as file:
        chunk = file.read(1024)
        while chunk is not None:
            yield chunk
            chunk = file.read(1024)


@app.route('/')
def index():
    return 'Hey, Man'


@app.route('/video')
def video():
    return Response(streamhandler(VideoStreamer(os.path.dirname(os.path.abspath(__file__)) + '/match.mp4')),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/audio')
def audio():
    return Response(audiohandler(), mimetype='audio/wav')


@socketio.on('connect')
def connect():
    print('socket connected')


@socketio.on('disconnect')
def disconnect():
    print('socket disconnected')


@socketio.on('input_stream')
def input_stream(data):
    start_cycle(data)
    emit('output_stream', data, broadcast=True)


@socketio.on('anketa')
def anketa(data):
    cursor = pg.cursor()
    cursor.execute("INSERT INTO preferences (preferences) VALUES (%s)", (json.dumps(data),))
    pg.commit()
    cursor.close()
    IP.setPreferences(data)

    cursor = pg.cursor()
    cursor.execute("SELECT id FROM preferences ORDER BY id DESC LIMIT 1")
    userid = cursor.fetchone()
    emit("registered", userid, broadcast=True)


@socketio.on('login')
def login(id):
    cursor = pg.cursor()
    cursor.execute("SELECT preferences FROM preferences WHERE id = %s", (id,))
    preferences = cursor.fetchone()
    IP.setPreferences(preferences)


if __name__ == '__main__':
    socketio.run(app, log_output=False, debug=False)
