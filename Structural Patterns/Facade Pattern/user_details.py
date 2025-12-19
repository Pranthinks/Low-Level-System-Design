class User:
    
    def __init__(self , val: int):
        self.val = val
    def details(self):
        print("The user id given is: ", self.val)