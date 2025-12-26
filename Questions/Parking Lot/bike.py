from Vehicle_Interface import Interface_Vehicle


class Bike(Interface_Vehicle):

    def type(self):
        print("This is a Bike!!!")
    
    def space_needed(self):
        return 1