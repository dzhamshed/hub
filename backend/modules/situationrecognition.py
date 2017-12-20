import random


class SituationRecognition:
    def __init__(self):
        self.situations = ['offside', 'penalty', 'corner', 'outside', 'freekick', 'game']

    def getsituation(self, chunk):
        return random.choice(self.situations)
