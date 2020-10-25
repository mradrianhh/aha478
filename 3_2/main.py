import sys

from deck import Deck
from screens import *
from models import Player
from vars import *

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

    # Assign the screens to be used in the program to the dict with their identifier.
    screens["HOME"] = HomeScreen()
    screens["ACTIONS"] = ActionsScreen()
    screens["PLACE"] = PlaceScreen()
    screens["SET_SUIT"] = SetSuitScreen()

    # Nickname entry for each player.
    for i in range(int(sys.argv[1])):
        succeeded = False
        while(not succeeded):
            name = input(f"What is your name, player {i+1}? ")
            if not name in players:
                succeeded = True
        players[name] = Player(name)

    # Set the initial current player.
    current_player_index = 0
    current_player = players[list(players.keys())[current_player_index]]
    
    dealer_stack = Deck()

    # Give each player 5 cards.
    for key in players:
        players[key].hand = dealer_stack.hand(5)

    # Make the top_card the topmost card of the dealer stack(aka. the last card).
    top_card = dealer_stack.cards.pop()
    
def evaluate_winner():
    global winner

    # Every time before we change turns, check if any of the players have 0 cards. If it's the case, that player have won.
    for key in players:
        if len(players[key].hand) == 0:
            winner = players[key]
            print(f"{winner.name} won!")
            sys.exit(0)

def evaluate_placed_card(card):
    # Evaluate whether the placed card is legal. If it's legal, it'll return the card to be top_card.
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
        return None
    

def next_turn():
    global current_player_index
    global current_player

    evaluate_winner()
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
            # Present the "actions"-screen and save it's response-code.
            response = screens["ACTIONS"].show(current_player, top_card, times_drawn)
            if response == PLACE:
                # Present the user with his hand, and let him choose one to place. Evaluate the chosen card.
                while(True):
                    # Present the "place"-screen and save it's response-code and the card-index the player chose.
                    # If the player chose a valid card-index, the response is valid.
                    # If the player chose a invalid card-index, the response is invalid.
                    # If the player chose back, the response is back.
                    response, card_index = screens["PLACE"].show(current_player, top_card)
                    if response == VALID:
                        # Find the card the player chose to place by it's index in the player hand.
                        placed_card = current_player.hand[card_index-1]
                        # Evaluate the placed card and save the resulting top_card.
                        card = evaluate_placed_card(placed_card)
                        if card != None:
                            # If his response is valid and the card is legal, make it the topcard and remove it from his hand. 
                            # The top_card might be different if he placed an 8 and changed suit.
                            top_card = card
                            del current_player.hand[card_index-1]
                            next_turn()
                            break
                    elif response == BACK:
                        break
                break
            elif response == DRAW:
                # If the player chooses draw, increase times_drawn by 1 and move the topmost card in the dealer_stack to the players hand.
                times_drawn += 1
                current_player.hand.append(dealer_stack.cards.pop())
            elif response == PASS:
                # If the player chooses pass, skip to the next turn.
                next_turn()
                break
            elif response == QUIT:
                sys.exit(0)

if __name__ == "__main__":
    if int(sys.argv[1]) > 10:
        print("Max 10 players.")
        sys.exit(0)

    initialize()

    # Show the home screen and read user option.
    while(True):
        response = screens["HOME"].show()
        if response == QUIT:
            sys.exit(0)
        elif response == START:
            play()

