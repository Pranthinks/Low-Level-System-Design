from products_interface import Interface_Products

class Sports_prod(Interface_Products):
    def __init__(self, skn, quan, cost):
        self.skn = skn
        self.quan = quan
        self.cost = cost

    def SKN(self):
        print("SKN added to Sports Goods!!!", self.skn)
    
    def Quantity(self):
        print("Total Sports Goods added:", self.quan)
    
    def price(self):
        print("Cost of Sports Goods:", self.cost)