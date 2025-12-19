from file import FileSystemItem

class Big_Folder(FileSystemItem):
    def __init__(self, name: str):
        self.__res = []      # private list of FileSystemItem
        self.name = name
    
    def add(self, item: FileSystemItem):
        self.__res.append(item)
    
    def Show_details(self):
        print("In Folder:", self.name, "we have:")
        for item in self.__res:
            item.Show_details()   # polymorphism
