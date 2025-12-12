from notify import Interface
from emaill import Email
from text import Text

class Notification_System:
    def __init__(self, N_Type : Interface):
        self.N_Type = N_Type

    def send_message(self):
        self.N_Type.notify()

obj1 = Email()
obj2 = Text()

main_obj = Notification_System(obj1)
main_obj.send_message()

main_obj2 = Notification_System(obj2)
main_obj2.send_message()
