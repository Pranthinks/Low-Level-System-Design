from products_interface import Interface_Products

class electronics(Interface_Products):
    def __init__(self, skn, quan, cost):
        self.skn = skn
        self.quan = quan
        self.cost = cost
        self.type = "electronics"

    def SKN(self):
        return self.skn
    
    def Quantity(self):
        return self.quan
    
    def price(self):
        return self.cost
