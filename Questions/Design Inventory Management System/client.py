from Products_Factory import Unified_Factory
from Inventory_Manager import Manager

factory = Unified_Factory()
manager = Manager()

# Create two warehouses
manager.add_warehouse("Dallas")
manager.add_warehouse("Austin")

# Create products via factory
e1 = factory.create_product("electronics", "E100", 5, 500)
s1 = factory.create_product("sports", "S200", 10, 150)

# Add products to specific warehouses
manager.Warehouse_Addproduct("Dallas", e1)
manager.Warehouse_Addproduct("Austin", s1)

# Show inventory for one warehouse
manager.Stock_Details("Dallas")

# Show inventory for all warehouses
manager.Stock_All_Warehouses()
