from Parking_Area import ParkingArea
from credit_card import CreditCard
from debit_card import DebitCard

class ParkingSystemFacade:

    def __init__(self, total_area=10):
        self.parking = ParkingArea(total_area)
    
    def add_vehicle(self, vehicle_type: str):
        self.parking.Vehicle_Add(vehicle_type)
    
    def remove_vehicle(self, vehicle_type: str, payment_method: str):
        if payment_method.lower() == "credit":
            payment = CreditCard()
        elif payment_method.lower() == "debit":
            payment = DebitCard()
        else:
            print("Invalid payment method. Defaulting to Credit Card.")
            payment = CreditCard()
        
        self.parking.Vehicle_Remove(vehicle_type, payment)
    
    def show_parking(self):
        self.parking.Show_Parking()
