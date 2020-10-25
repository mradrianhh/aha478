Python implementation of "Crazy Eights".

Instructions:

To run the program, enter the following command:

    python main.py <n>

where <n> is the number of players.

The number of players is capped at 10 as it's the maximum amount of players one deck has sufficient cards for,
but please keep in mind that it would only be 2 cards left in the dealer_stack then.

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

The main program is the entry point.
The main program(main.py) holds and controls the state of the program.
The main program holds the dealer_stack, the top_card and the players. Through
their extension methods, the main program is able to control the entire state of the program.

The screen

Design notes:

The program isn't in true accordance with oop-programming, and there certainly are improvements that can be made to accomplish this accordance.
Most of the logic contained in main.py, shouldn't be contained there. Rather, it should be encapsulated and, in my opinion, delegated to some sort of manager. 
In this project, I would certainly consider making a "dealer"-class. Not only would it be able to encapsulate the logic which clutters the entry-point file and act as the manager,
but it would also be more appropriate for many of the methods in the "deck"-class to exist in the "dealer"-class.

I'd rather have the "deck"-class be a glorified stack-structure with the basic push() and pop() methods. 
The "dealer"-class would contain a deck which it could manipulate.
The "dealer"-class would have extension-methods such as deal() and hand() that would manipulate the stack, but by placing them in the "dealer"-class,
you would emphasize the true purpose of the methods: to give the players cards, which again would make their correct usage more clear.
It would also be more natural for the "dealer"-class to initialize the players in the game, give them cards, etc. To see why this would be the case,
imagine expanding this into a multiplayer game. You'd have a server-client design in which the clients were the "players" and the server was the "dealer".
This means that the dealer accepts a connection; the dealer reads the request; the dealer responds asking the player for a username, and, finally, the dealer
reads this username, creates a new player in it's game and deals the player a hand. Through this architecture-design it's apparent why you would encapsulate that logic into the
"dealer"-class.

It would certainly be interesting to introduce networking and make a server-client based multiplayer game, and I would've done it in golang, but not in python. I'm not proficient
enough, it's dynamic nature drives me crazy, and the lack of pointers makes it a pain to pass around and manipulate state.

The "screens"-package is a halfway-implementation of a golang "navigator"-package I made. It's also a halfway implementation in regards to it's oop accordance.
Yes, it examplifies inheritence. It also encapsulates lots of the logic that else would be contained in the main program, but what it lacks - and the lack of it
still contaminates the main program - is the "navigator". The manager-class belonging to the package that keeps controls of all of the screens, controls the output(the ui),
and parses the input.

Sidenote in regards to the use of an interface(although it's never a true usage in python): yes, by extending the "ScreenInterface" class, every screen is of type "ScreenInterface".
This would be a necessity in a statically-typed language where lists/dicts/enumerables could only contain predetermined object-type(s), because if we were to have a list of screens,
we couldn't put all our different screens in one list without them inheriting from the same parent-class, because only then would they be of the same type.

Still got no clue how the python module system works, and I don't care enough to find out. A wise meme once told me: if it works, don't touch it.

Response codes:

"PLACE" - Player has chosen to place a card.
"DRAW" - Player has chosen to draw a card.
"PASS" - Player has chosen to pass.
"INVALID" - The player input could not be understood.
"VALID" - The player input was understood and valid.
"QUIT" - Quit the program.
"START" - Start the program.
"BACK" - Go back to the previous screen.