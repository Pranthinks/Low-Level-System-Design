from base_pizza import Base_pizza
from toppings import Cheese, Olives

obj = Base_pizza()
print(obj.get_cost())
print(obj.get_description())

obj1 = Cheese(obj)
print(obj1.get_description())

obj2 = Olives(obj)
print(obj2.get_description())