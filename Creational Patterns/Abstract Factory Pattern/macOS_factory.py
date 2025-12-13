from UI_interface import UIfactory
from macos_products import macOS_buttons, macOS_Scrollbar


class macOS_Factory(UIfactory):

    def create_button(self):
        return macOS_buttons()
    
    def create_scrollbar(self):
        return macOS_Scrollbar()
