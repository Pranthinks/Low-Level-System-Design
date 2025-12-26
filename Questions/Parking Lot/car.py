from Vehicle_Interface import Interface_Vehicle


class Car(Interface_Vehicle):

    def type(self):
        print("This is a Car!!")
    
    def space_needed(self):
        return 2