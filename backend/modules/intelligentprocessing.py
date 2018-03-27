import random


class IntelligentProcessing:
    def __init__(self):
        self.objects = ['Ronaldo', 'Messi', 'ball', 'referee']
        self.coords = None
        self.currentObject = 'not chosen'
        self.counter = 0
        self.preferences = None

    def getobject(self, emotion, situation, coordinates):
        if self.counter % 2 == 0:
            objct = random.choice(self.objects)
            coords = [c for c in coordinates if c['name'] == objct]
            self.coords = coords[0]
        self.counter += 1
        return self.coords

    def setPreferences(self, preferences):
        self.preferences = preferences

    def getObjectToWatch(self):
        return self.currentObject

    def setObjectToWatch(self, objectName):
        for o in self.objects:
            if o == objectName:
                self.currentObject = o
        return self.currentObject
