from .screen_interface import ScreenInterface

class ActionsScreen(ScreenInterface):

    def show(self, current_player, top_card, times_drawn):
        print(f"{current_player.name}'s turn\n")
        print(f"Top card: {top_card.get_name()}")
        hand = ""
        for card in current_player.hand:
            hand += card.get_name() + " "
        hand = hand[:len(hand)-1]
        print(f"Your hand: {hand}")

        if times_drawn < 3:
            print("1. Place card | 2. Draw card | 3. Pass | 0. Quit Game")
            response = input()
            if response == "3":
                return "PASS"
            elif response == "2":
                return "DRAW"
            elif response == "1":
                return "PLACE"
            elif response == "0":
                return "QUIT"
            else:
                return "INVALID"
        else:
            print("1. Place card | 2. Pass | 0. Quit Game")
            response = input()
            if response == "2":
                return "PASS"
            elif response == "1":
                return "PLACE"
            elif response == "0":
                return "QUIT"
            else:
                return "INVALID"

        

