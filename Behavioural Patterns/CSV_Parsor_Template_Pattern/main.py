from interface import Interface
from csv_method import csv
from json_method import json


obj1 = csv()
obj2 = json()

obj1.process_file()
print()
obj2.process_file()