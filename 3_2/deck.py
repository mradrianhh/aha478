from random import shuffle

from models import Card


suits = ["C", "D", "H", "S"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Deck():

    cards = []

    def __init__(self):
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
        shuffle(self.cards)

    def hand(self, n):
        # Deal out a hand of length "n".
        hand = []
        # Using a while-loop because I'll get a unused index-variable if I use a for-loop, and the pylint warning on it annoys me.
        i = 0
        while i < n:
            hand.append(self.cards.pop())
            i += 1

        return hand

    def deal(self, n, p):
        # Deal out "p" hands of "n" length.
        hands = []
        for i in range(p):
            hand = []
            for j in range(n):
                hand.append(self.cards.pop())
            hands.append(hand)

        return hands

    def __str__(self):
        # Create a string with every card separated by whitespace.
        string = ""
        for card in self.cards:
            string += card.get_name() + " "
        
        return string[:len(string)-1] # remove the last whitespace.
        