#!/usr/bin/python

import os, sys

cd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cd)

sys.path.insert(0, os.path.join(cd, 'libs'))

import random
from socketIO_client import SocketIO


socketio = None
objects = ['Ronaldo', 'Messi', 'ball', 'referee']
coords = None
counter = 0
preferences = None

def getobject(emotion, situation, coordinates):
  global counter
  global coords
  global objects
  if counter % 2 == 0:
    objct = random.choice(objects)
    coords = [c for c in coordinates if c['name'] == objct]
    coords = coords[0]
  counter += 1
  return coords


def setPreferences(prefs):
  global preferences
  preferences = prefs


def listener(data):
  print('received => ', data)
  if data['command'] == 'process':
    resp = getobject(data['emotion'], data['situation'], data['coordinates'])
    socketio.emit('intelligent_processing', resp)
    print('sent => ', resp)
  elif data['command'] == 'UP':
    setPreferences(data['preferences'])


def connected():
  print('connected')


def reconnected():
  print('reconnected')


def disconnected():
  print('disconnected')


if __name__ == '__main__':
  socketio = SocketIO('localhost', 5000)
  socketio.on('connect', connected)
  socketio.on('reconnect', reconnected)
  socketio.on('disconnect', disconnected)
  socketio.on('intelligent_processing', listener)
  socketio.emit('join', 'IP')
  socketio.wait()
  socketio.emit('leave', 'IP')