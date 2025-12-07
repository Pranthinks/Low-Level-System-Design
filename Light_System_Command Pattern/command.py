from interface import Interface
from light import Light


class Turn_on(Interface):
    def __init__(self, obj : Light):
        self.obj = obj

    def execute(self):
        self.obj.on()

class Turn_off(Interface):
    def __init__(self, obj : Light):
        self.obj = obj

    def execute(self):
        self.obj.off()