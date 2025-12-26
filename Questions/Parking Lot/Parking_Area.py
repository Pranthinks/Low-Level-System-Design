from vehicle_factory import Unified_Factory
from payment_interface import Interface_Payments

obj = Unified_Factory()

class ParkingArea:

    def __init__(self, total_area = 10):
        self.arr = []
        self.total_area = total_area
    

    def Vehicle_Add(self, val : str):
        vehicle_obj = obj.add_vehicle(val)
        area_req = vehicle_obj.space_needed()
        if self.total_area - area_req >= 0:
            self.arr.append(vehicle_obj)
            print("Your", val, "has been added, take your payment receipt!!!")
            self.total_area -= area_req
        else:
            print("Sorry, No Available space!!!")
    
    def Vehicle_Remove(self, val: str, payment: Interface_Payments):
        # find the vehicle object of that type
        for vehicle in self.arr:
            if vehicle.__class__.__name__.lower() == val.lower():
                self.arr.remove(vehicle)
                self.total_area += vehicle.space_needed()
                payment.pay(val)
                print(f"{val} has been removed. Remaining space: {self.total_area}")
                return
        print(f"No {val} found in the parking area.")
    
    def Show_Parking(self):
        print("Vehicles in parking:")
        for v in self.arr:
            print(f"- {v.__class__.__name__}")
        print(f"Total available space: {self.total_area}")


