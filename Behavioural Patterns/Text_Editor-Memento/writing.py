from history_memento import History

class write(History):
    def write(self , text):
        print(text)
        self.save(text)