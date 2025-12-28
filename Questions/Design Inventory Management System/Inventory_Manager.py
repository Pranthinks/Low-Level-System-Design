from warehouse import WareHouse
from products_interface import Interface_Products

class Manager:
    def __init__(self):
        # Dictionary to store multiple warehouses
        self.warehouses = {}
    
    def add_warehouse(self, name: str):
        if name not in self.warehouses:
            self.warehouses[name] = WareHouse()
            print(f"Warehouse '{name}' added.")
        else:
            print(f"Warehouse '{name}' already exists.")
    
    def Warehouse_Addproduct(self, warehouse_name: str, product: Interface_Products):
        if warehouse_name in self.warehouses:
            self.warehouses[warehouse_name].add_product(product)
        else:
            print(f"Warehouse '{warehouse_name}' does not exist.")
    
    def Warehouse_Removeproduct(self, warehouse_name: str, product: Interface_Products):
        if warehouse_name in self.warehouses:
            self.warehouses[warehouse_name].remove_product(product)
        else:
            print(f"Warehouse '{warehouse_name}' does not exist.")
    
    def Stock_Details(self, warehouse_name: str):
        if warehouse_name in self.warehouses:
            print(f"\nInventory for warehouse '{warehouse_name}':")
            self.warehouses[warehouse_name].show_inventory()
        else:
            print(f"Warehouse '{warehouse_name}' does not exist.")
    
    def Stock_All_Warehouses(self):
        for name, wh in self.warehouses.items():
            print(f"\n--- Warehouse: {name} ---")
            wh.show_inventory()
