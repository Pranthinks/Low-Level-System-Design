from user_details import User
from order_details import Order_details

class API_Gateway:

    def __init__(self, id, order):
        self.obj1 = User(id)
        self.obj2 = Order_details(order)

    def get_full_details(self):
        self.obj1.details()
        self.obj2.or_details()