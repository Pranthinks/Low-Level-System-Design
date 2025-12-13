
from burger import Burger


class Building:
    def __init__(self):
        self.obj = Burger()
    

    def add_bun(self, bun):
        self.obj.bun  = bun
        return self
    
    def add_cheese(self, cheese):
        self.obj.cheese  = cheese
        return self
    
    def add_chilli(self, chilli):
        self.obj.chilli  = chilli
        return self
    
    def build(self):
        return self.obj

burger = (
    Building()
    .add_bun("Sesame")
    .add_cheese("Chicken")
    .add_chilli("Red Chilli")
    .build()
)

print(burger)
