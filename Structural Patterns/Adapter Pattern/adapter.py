from interface import Interface


class Adapter_Email(Interface):

    def __init__(self , custom):
        self.custom = custom
    

    def Sending(self):
        self.custom.send()