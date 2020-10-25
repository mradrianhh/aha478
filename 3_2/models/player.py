class Player():
    hand = []
    name = ""

    def __init__(self, name):
        self.name = name

    def show_hand(self):
        """
        Print the player's hand.

        Concatenates each card's string represantion with a whitespace.
        """
        hand_str = ""
        for card in self.hand:
            hand_str += card.get_name() + " "
        hand_str = hand_str[:len(hand_str)-1]
        print(hand_str)
        
