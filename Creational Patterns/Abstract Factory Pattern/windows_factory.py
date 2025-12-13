from UI_interface import UIfactory
from windows_products import Windows_buttons, Windows_Scrollbar


class Windows_Factory(UIfactory):

    def create_button(self):
        return Windows_buttons()
    
    def create_scrollbar(self):
        return Windows_Scrollbar()
