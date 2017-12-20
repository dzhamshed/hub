import random


class EmotionRecognition:
    def __init__(self):
        self.emotions = ['fear', 'anger', 'sadness', 'depression', 'joy', 'disgust', 'surprise', 'trust', 'anticipation']

    def getemotion(self, chunk):
        return random.choice(self.emotions)
