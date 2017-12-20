import random


class ObjectRecognition:
    def __init__(self, width, height):
        names = ['Ronaldo', 'Messi', 'ball', 'referee']
        self.objects = []
        for name in names:
            lx = random.randint(0, width - 100)
            ly = random.randint(0, height - 100)
            rx = random.randint(lx + 100, width)
            ry = random.randint(ly + 100, height)
            self.objects.append({
                'name': name,
                'lx': lx,
                'ly': ly,
                'rx': rx,
                'ry': ry
            })

    def getcoordinates(self, chunk):
        return self.objects
