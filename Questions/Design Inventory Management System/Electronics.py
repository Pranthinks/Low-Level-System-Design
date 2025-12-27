from products_interface import Interface_Products

class electronics(Interface_Products):
    def __init__(self, skn, quan, cost):
        self.skn = skn
        self.quan = quan
        self.cost = cost

    def SKN(self):
        print("SKN added to electronics!!!", self.skn)
    
    def Quantity(self):
        print("Total Electronics added:", self.quan)
    
    def price(self):
        print("Cost of Electronics:", self.cost)