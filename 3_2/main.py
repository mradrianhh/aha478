import sys

from deck import Deck
from screens import *
from models import Player

# Response codes
PASS = "PASS"
PLACE = "PLACE"
DRAW = "DRAW"
INVALID = "INVALID"
VALID = "VALID"
QUIT = "QUIT"
START = "START"
BACK = "BACK"

# Global collection of players in the game.
players = {}

# The index of the player whose turn it currently is.
current_player_index = None

# The player whose turn it currently is.
current_player = None

# The stack of cards. Also acts as the dealer.
dealer_stack = None

# The topmost card of the playing stack.
top_card = None

# Winning player.
winner = None

# Global collection of screens.
screens = {}

def initialize():
    global current_player_index
    global current_player
    global dealer_stack
    global top_card
    global players
    global screens

    screens["HOME"] = HomeScreen()
    screens["ACTIONS"] = ActionsScreen()
    screens["PLACE"] = PlaceScreen()
    screens["SET_SUIT"] = SetSuitScreen()

    for i in range(int(sys.argv[1])):
        succeeded = False
        while(not succeeded):
            name = input(f"What is your name, player {i+1}? ")
            if not name in players:
                succeeded = True
        players[name] = Player(name)

    current_player_index = 0
    current_player = players[list(players.keys())[current_player_index]]
    
    dealer_stack = Deck()

    for key in players:
        players[key].hand = dealer_stack.hand(5)

    top_card = dealer_stack.cards.pop()
    
def evaluate_winner():
    global winner

    for key in players:
        if len(players[key].hand) == 0:
            winner = players[key]
            print(f"{winner.name} won!")
            sys.exit(0)

def evaluate_placed_card(card):
    # Evaluate whether the placed card is legal. Returns True if legal, False if illegal.
    if card.get_suit() == top_card.get_suit():
        return card
    elif card.get_value() == top_card.get_value():
        return card
    elif card.get_value() == "8":
        while(True):
            response_code, response = screens["SET_SUIT"].show()
            if response_code == VALID:
                card.set_suit(response)
                break
        return card
    else:
        return False
    

def next_turn():
    global current_player_index
    global current_player

    if current_player_index == len(players)-1:
        current_player_index = 0
    else:
        current_player_index += 1

    current_player = players[list(players.keys())[current_player_index]]

def play():
    global current_player
    global top_card
    global dealer_stack

    while(True):
        times_drawn = 0

        while(True):
            response = screens["ACTIONS"].show(current_player, top_card, times_drawn)
            if response == PLACE:
                # Present the user with his hand, and let him choose one to place. Evaluate the chosen card.
                while(True):
                    response, card_index = screens["PLACE"].show(current_player, top_card)
                    if response == VALID:
                        placed_card = current_player.hand[card_index-1]
                        legal = evaluate_placed_card(placed_card)
                        if legal:
                            # If his response is valid and the card is legal, make it the topcard and remove it from his hand.
                            top_card = placed_card
                            del current_player.hand[card_index-1]
                            next_turn()
                            break
                    elif response == BACK:
                        break
                break
            elif response == DRAW:
                times_drawn += 1
                current_player.hand.append(dealer_stack.cards.pop())
            elif response == PASS:
                next_turn()
                break
            elif response == QUIT:
                sys.exit(0)

        evaluate_winner()

if __name__ == "__main__":
    if int(sys.argv[1]) > 10:
        print("Max 10 players.")
        sys.exit(0)

    initialize()

    while(True):
        response = screens["HOME"].show()
        if response == QUIT:
            sys.exit(0)
        elif response == START:
            play()

