from interface import Interface
from command import Turn_on, Turn_off
from light import Light


class Remote_Control:
    def __init__(self, obj : Interface):
        self.obj = obj
    
    def control(self):
        self.obj.execute()

light = Light()

    
turn_on_command = Turn_on(light)
remote = Remote_Control(turn_on_command)
remote.control()  
turn_off_command = Turn_off(light)
remote = Remote_Control(turn_off_command)
remote.control()  






