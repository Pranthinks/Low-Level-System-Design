from interface import Interface

class Device_one(Interface):
    def display(self, temp):
        print('From Device - 1 Current Temperature:', temp)