from products_interface import Interface_Products
from Electronics import electronics
from sports import Sports_prod

class Unified_Factory:

    def create_product(self, type , skn, quan, cost):
        if type.lower() == 'electronics':
            return electronics(skn, quan, cost)
        elif type.lower() == 'sports':
            return Sports_prod(skn , quan, cost)
        else:
            raise ValueError(f"Product '{type}' not recognized")
    
