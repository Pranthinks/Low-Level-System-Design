from payment_interface import Interface_Payments

class DebitCard(Interface_Payments):

    def pay(self, vehicle_name: str):
        print(f"Paid using Debit Card for {vehicle_name}.")