from device1 import Device_one
from device2 import Device_two
from interface import Interface

class Station:
    def __init__(self, devices : list[Interface]):
        self.devices = devices
        
    def set_temperature(self, temp: int):
        for device in self.devices:
            device.display(temp)
    
    def count(self):
        print('The Total Devices:', len(self.devices))
    
    def remove_device(self, id):
        if 0 <= id < len(self.devices):
            removed = self.devices.pop(id)
            print(f'Device {id} has been removed')
        else:
            print('Invalid device id!')
    
    def add_device(self, device : Interface):
        self.devices.append(device)
        print(f'Device added. Total devices: {len(self.devices)}')


#Main Initialization
obj1 = Device_one()
main_obj = Station([obj1])
main_obj.set_temperature(98)
main_obj.count()
obj2 = Device_two()
main_obj.add_device(obj2)
main_obj.set_temperature(45)