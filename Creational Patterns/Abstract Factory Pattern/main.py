from UI_interface import UIfactory
from windows_factory import Windows_Factory
from macOS_factory import macOS_Factory


def final(factory : UIfactory):
    button = factory.create_button()
    scroll = factory.create_scrollbar()

    button.render()
    scroll.render()

wind = Windows_Factory()
mac = macOS_Factory()

final(wind)
final(mac)