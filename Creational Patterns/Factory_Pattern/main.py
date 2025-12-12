from vehicle_factory import VehicleFactory

class Fetch:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle_type: str):
        vehicle = VehicleFactory.get_vehicle(vehicle_type)
        self.vehicles.append(vehicle)

    def show_colors(self):
        for vehicle in self.vehicles:
            vehicle.color()



fetch = Fetch()
fetch.add_vehicle("car")
fetch.add_vehicle("bike")
fetch.show_colors()
