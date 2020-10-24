from .screen_interface import ScreenInterface

class PlaceScreen(ScreenInterface):

    def show(self, current_player, top_card):
        print(f"Top card: {top_card.get_name()}")
        hand = ""
        for card in current_player.hand:
            hand += card.get_name() + " "
        hand = hand[:len(hand)-1]
        print(f"Your hand: {hand}\n")

        if len(current_player.hand) == 1:
            print("(1). Choose card. | 0. Back")
            response = input()
        else:
            print(f"Choose card (1-{len(current_player.hand)}) | 0. Back")
            response = input()
        
        try:
            if response == "0":
                return "BACK", None
            elif int(response) < len(current_player.hand):
                return "VALID", int(response)
            else:
                return None, None
        except:
            return None, None
        

