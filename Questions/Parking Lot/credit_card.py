from payment_interface import Interface_Payments

class CreditCard(Interface_Payments):

    def pay(self, vehicle_name: str):
        print(f"Paid using Credit Card for {vehicle_name}.")
