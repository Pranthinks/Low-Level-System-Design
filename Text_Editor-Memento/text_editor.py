from history_memento import History
from writing import write

class Text_Editor:
    def __init__(self, poly: History):
        self.poly = poly
    
    def writing(self, text):
        self.poly.write(text)
        print("Current Text:", self.poly.cur_print())
    
    def undo(self):
        prev = self.poly.undo()
        print("After Undo:", prev)



    


#Main usage

obj = write()

main_obj = Text_Editor(obj)
main_obj.writing('Hello how are you?')
main_obj.writing('I am great')
main_obj.undo()
main_obj.undo()
main_obj.writing('I am praneeth')