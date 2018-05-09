#!/usr/bin/env python3

import os, sys

cd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cd)

sys.path.insert(0, os.path.join(cd, 'libs'))

from moviepy.editor import *

clip = VideoFileClip('match.mp4')
clip.audio.write_audiofile('sound.mp3')