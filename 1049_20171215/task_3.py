import numpy as np
import random

N = 10000

class Player():
    _wallet = 0
    def __init__(self):
        pass

    def get_wallet(self):
        return self._wallet

    def change_wallet(self, amount):
        self._wallet += amount

class GameManager():

    def __init__(self):
        pass

    # Toss a coin 10 times.
    # If 7 of the tosses give heads, you win 200.
    # Each game costs 30.
    def play_game(self, player):
        player.change_wallet(-30)
        heads = 0
        tails = 0
        for i in range(10):
            result = random.random()
            if result < 0.5:
                heads += 1
            else:
                tails += 1

        if heads >= 7:
            player.change_wallet(200)
    

if __name__ == "__main__":
    game_manager = GameManager()
    player = Player()

    # Play N games.
    for i in range(N):
        game_manager.play_game(player)

    print(player.get_wallet())