#!/usr/bin/python

import os, sys

cd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cd)

sys.path.insert(0, os.path.join(cd, 'libs'))

import random
from socketIO_client import SocketIO


socketio = None
emotions = ['fear', 'anger', 'sadness', 'depression', 'joy', 'disgust', 'surprise', 'trust', 'anticipation']

def listener(data):
  print('received => ', len(data))
  emotion = random.choice(emotions)
  socketio.emit('ER', emotion)
  print('sent => ', emotion)


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
  socketio.on('user_stream', listener)
  socketio.emit('join', 'ER')
  socketio.wait()
  socketio.emit('leave', 'ER')