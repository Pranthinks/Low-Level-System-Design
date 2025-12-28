from products_interface import Interface_Products

class WareHouse:
    def __init__(self):
        self.arr = {}  # Dictionary to separate products by type

    def add_product(self, obj: Interface_Products):
        type_name = obj.type
        if type_name not in self.arr:
            self.arr[type_name] = []

        self.arr[type_name].append(obj)
        print(f"Product {obj.SKN()} added successfully to {type_name}!")
    
    def remove_product(self, obj: Interface_Products):
        type_name = obj.type
        if type_name in self.arr and obj in self.arr[type_name]:
            self.arr[type_name].remove(obj)
            print(f"Product {obj.SKN()} removed successfully from {type_name}!")
        else:
            print(f"No matching product found in {type_name}.")

    def show_inventory(self):
        for type_name, products in self.arr.items():
            print(f"\n--- {type_name.capitalize()} ---")
            if not products:
                print("No products.")
            for prod in products:
                print(f"SKN: {prod.SKN()}, Quantity: {prod.Quantity()}, Price: {prod.price()}")
