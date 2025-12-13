from buttons_interface import Buttons
from scrollbar_interface import Scroll


class macOS_buttons(Buttons):
    def render(self):
        print("Rendering macOS buttons!!!")

class macOS_Scrollbar(Scroll):
    def render(self):
        print("Rendering macOS scrollbar!!!")