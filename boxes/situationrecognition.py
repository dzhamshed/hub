#!/usr/bin/python

import os, sys

cd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cd)

sys.path.insert(0, os.path.join(cd, 'libs'))

import random
from socketIO_client import SocketIO


socketio = None
situations = ['offside', 'penalty', 'corner', 'outside', 'freekick', 'game']

def listener(data):
  print('received => ', len(data))
  situation = random.choice(situations)
  socketio.emit('SR', situation)
  print('sent => ', situation)


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
  socketio.on('video_stream', listener)
  socketio.emit('join', 'SR')
  socketio.wait()
  socketio.emit('leave', 'SR')