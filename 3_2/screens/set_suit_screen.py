from .screen_interface import ScreenInterface

class SetSuitScreen(ScreenInterface):

    def show(self):
        response = input("Choose a suit(C/D/H/S): ")

        if response in ["C", "D", "H", "S"]:
            return "VALID", response
        else:
            return "INVALID", None