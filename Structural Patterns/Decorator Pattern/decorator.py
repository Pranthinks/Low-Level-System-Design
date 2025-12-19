from interface import pizza

class Decorator(pizza):

    def __init__(self, obj: pizza):
        self.obj = obj

    def get_cost(self):
        return self.obj.get_cost()
    
    def get_description(self):
        return self.obj.get_description()