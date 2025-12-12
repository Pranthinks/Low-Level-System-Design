class App:
    __instance = None  # Class-level private variable to store the singleton instance

    def __new__(cls, name=None, age=None):
        if cls.__instance is None:
            cls.__instance = super(App, cls).__new__(cls)
            cls.__instance.__initialized = False  # Flag to ensure __init__ runs only once
        return cls.__instance

    def __init__(self, name=None, age=None):
        if self.__initialized:
            return  # Avoid re-initialization
        self.__name = name  # Private variable
        self.__age = age    # Private variable
        self.__initialized = True

    # Getter for name
    def find_name(self):
        print("The name is", self.__name)

    # Getter for age
    def find_age(self):
        print("The age is", self.__age)

    # Optional: setters if you want controlled modification
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


# Testing singleton behavior
obj1 = App('Praneeth', 32)
obj2 = App('Rajesh', 45)

obj1.find_name()  # Output: The name is Praneeth
obj2.find_name()  # Output: The name is Praneeth (same instance as obj1)
obj2.set_name("Rajesh")
obj1.find_name()  # Output: The name is Rajesh (again, same instance)
