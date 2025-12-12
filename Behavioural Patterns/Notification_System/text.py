from notify import Interface

class Text(Interface):
    def notify(self):
        print('This Notification is from Text method')