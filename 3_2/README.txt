"""
Python implementation of "Crazy Eights".

Game explanation:

Each player draws 5 cards from a shuffled deck when the game starts.
Then the top card in the stack gets placed into a new stack.
Players take turns placing a card onto the new stack, but the card they place must meet one of the following conditions:
    (i) - The card is of the same suit.
    (ii) - The card is of the same value.
    (iii) - The card is of value 8.
If the player places a card of the value 8, the player chooses the current stack color.
If the player has no legal cards to play, it must draw 3 cards.
If the player still has no legal cards to play, it must pass.
The winner is the player that empties it's hand first.

Program architecture:

The main program acts as an entry point that initializes the game.

Response codes:

"PLACE" - Player has chosen to place a card.
"DRAW" - Player has chosen to draw a card.
"PASS" - Player has chosen to pass.
"INVALID" - The player input could not be understood.
"""