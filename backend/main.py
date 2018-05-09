#!/usr/bin/env python3

import os, sys

cd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cd)

sys.path.insert(0, os.path.join(cd, 'libs'))


from core.videostreamer import VideoStreamer

from core.database import  pg


from flask import Flask, Response
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)

import logging, json, base64
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app.config['SECRET_KEY'] = '@SUPERSAFE!'
socketio = SocketIO(app)
crop = None
emotion = None
situation = None
coordinates = None

def streamhandler(streamer):
    while True:
        frame = streamer.get_frame(crop)
        data = base64.b64encode(frame).decode('ascii')
        socketio.emit('video_stream', data, broadcast=True, room='VS_ROOM') # situation recognition and object recognition subscribe to this
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


@socketio.on('join')
def join(data):
    print('%s has joined' % data)
    join_room(data)
    if data == 'SR' or data == 'OR':
        join_room('VS_ROOM')
    elif data == 'ER' or data == 'USER':
        join_room('US_ROOM')
    return 'ok'


@socketio.on('leave')
def leave(data):
    print('%s has left' % data)
    leave_room(data)
    if data == 'SR' or data == 'OR':
        leave_room('VS_ROOM')
    elif data == 'ER' or data == 'USER':
        leave_room('US_ROOM')
    return 'ok'


@socketio.on('anketa')
def anketa(data):
    cursor = pg.cursor()
    cursor.execute("INSERT INTO preferences (preferences) VALUES (%s)", (json.dumps(data),))
    pg.commit()
    cursor.close()
    cdata = {
        'command': 'update_preferences',
        'preferences': data
    }
    emit('IP', cdata, broadcast=True, room='IP')

    cursor = pg.cursor()
    cursor.execute("SELECT id FROM preferences ORDER BY id DESC LIMIT 1")
    userid = cursor.fetchone()
    emit("anketa", userid)


@socketio.on('login')
def login(data):
    print('login -> ', data)
    cursor = pg.cursor()
    cursor.execute("SELECT preferences FROM preferences WHERE id = %s", (data,))
    preferences = cursor.fetchone()
    cdata = {
        'command': 'update_preferences',
        'preferences': data
    }
    emit('IP', cdata, broadcast=True, room='IP')
    return 'ok'


@socketio.on('user_input_stream')
def input_stream(data):
    emit('user_stream', data, boradcast=True, room='US_ROOM')


@socketio.on('ER')
def ER(data):
    global emotion
    global situation
    global coordinates
    emotion = data
    # print('emotion -> ', emotion)
    if all(v is not None for v in [emotion, situation, coordinates]):
        cdata = {
            'command': 'process',
            'emotion': emotion,
            'situation': situation,
            'coordinates': coordinates
        }
        emit('IP', cdata, broadcast=True, room='IP')
    elif emotion is None:
        print('=> emotion')
    elif situation is None:
        print('=> situation')
    elif coordinates is None:
        print('=> coordinates')


@socketio.on('SR')
def SR(data):
    global situation
    situation = data
    # print('situation -> ', situation)


@socketio.on('OR')
def OR(data):
    global coordinates
    coordinates = data
    # print('coordinates -> ', coordinates)


@socketio.on('IP')
def IP(data):
    global crop
    global emotion
    global situation
    crop = data
    # print('crop -> ', crop)
    coords = '(' + str(crop['lx']) + ', ' + str(crop['ly']) + ') x (' + str(crop['rx']) + ', ' + str(crop['ry']) + ')'
    logrow = emotion + ' | ' + situation + ' | ' + coords
    print ('========> ', logrow)
    emit('logger', logrow, broadcast=True, room='USER')


# Temporary
@socketio.on('get_match_info')
def get_match_info():
    teams = []
    real = {
        'name': "Real Madrid",
        'icon': "data:image/png;base64,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",
        'players': [
            {
                'name': "Ronaldo",
                'number': "7"
            },

            {
                'name': "Kroos",
                'number': "8"
            },

            {
                'name': "Modric",
                'number': "10"
            }
        ]
    }
    barcelona = {
        'name': "Barcelona",
        'icon': "https://lh4.googleusercontent.com/proxy/vsi7199xa-jME7JTgmW82a3FieinymCUxdLfEfpgL0Y06gGfBpRYN_UcYYYQJZZbnsstiMrghGpZAI9gWehpkGDjMG7WQGfqEq9C1s0P5KbPzh4h_zHst-oZ5E8ncJll4dDu-FHd2KV8mkNsn3MELiAimFZM-ji6qSirag15fIpekAb47-QapLBqwg=s0-d",
        'players': [
            {
                'name': "Iniesta",
                'number': "8"
            },

            {
                'name': "Messi",
                'number': "10"
            },

            {
                'name': "Busquets",
                'number': "5"
            }
        ]
    }
    teams.append(barcelona)
    teams.append(real)
    return teams


objects = ['Ronaldo', 'Messi', 'ball', 'referee']
currentObject = 'not chosen'


@socketio.on('setObjectToWatch')
def setObjectToWatch(objectName):
    global objects
    global currentObject
    for o in objects:
        if o == objectName:
            currentObject = o
    return currentObject



if __name__ == '__main__':
    socketio.run(app, log_output=False, debug=False)
