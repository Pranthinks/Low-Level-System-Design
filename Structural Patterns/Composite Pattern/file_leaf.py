from file import FileSystemItem

class File(FileSystemItem):
    def __init__(self, val: str):
        self.val = val

    def Show_details(self):
        print("Contains File:", self.val)
