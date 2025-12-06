from notify import Interface

class Email(Interface):
    def notify(self):
        print('This Notification is from Email method')