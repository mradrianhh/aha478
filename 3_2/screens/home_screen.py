import sys

from .screen_interface import ScreenInterface

class HomeScreen(ScreenInterface):

    def show(self):
        # Present the home screen. Read the player option, and repeat the selection if the answer can't be understood. 
        print("\n\tCRAZY EIGHTS\n")
        print("1. START GAME | 0. QUIT GAME\n")
        response = input()
        if response == "0":
            return "QUIT"
        elif response == "1":
            return "START"
        else:
            return "INVALID"
