from Vehicle_Interface import Interface_Vehicle


class Truck(Interface_Vehicle):

    def type(self):
        print("This is a Truck!!!")
    
    def space_needed(self):
        return 3