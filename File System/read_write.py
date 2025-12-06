from file import File

class read_write(File):
    def __init__(self):
        super().__init__()
    
    def read(self):
        super().read()
    
    def write(self):
        print("Writing from chile class")

obj = read_write()
obj.read()
obj.write()
    