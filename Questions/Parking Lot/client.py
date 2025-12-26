from Parking_System_Facade import ParkingSystemFacade

parking_system = ParkingSystemFacade(total_area=10)

parking_system.add_vehicle("car")
parking_system.add_vehicle("bike")

parking_system.show_parking()

parking_system.remove_vehicle("car", "credit")
parking_system.remove_vehicle("bike", "debit")

parking_system.show_parking()
