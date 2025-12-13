from buttons_interface import Buttons
from scrollbar_interface import Scroll


class Windows_buttons(Buttons):
    def render(self):
        print("Rendering Windows buttons!!!")

class Windows_Scrollbar(Scroll):
    def render(self):
        print("Rendering Windows scrollbar!!!")