from interface import Interface

class Device_two(Interface):
    def display(self, temp):
        print('From Device -2 Current Temperature:', temp)