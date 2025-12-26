from Vehicle_Interface import Interface_Vehicle
from car import Car
from bike import Bike
from truck import Truck

class Unified_Factory:
    def add_vehicle(self, val: str):

        if val.lower() == 'car':
            return Car()
        elif val.lower() == 'bike':
            return Bike()
        elif val.lower() == 'truck':
            return Truck()
        else:
            raise ValueError(f"Vehicle '{val}' not recognized")
    
    
