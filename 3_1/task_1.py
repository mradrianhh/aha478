import matplotlib.pyplot as plt

class Ball():

    position = []

    def __init__(self, x, y):
        self.position = [x, y]

    def __add__(self, other):
        return Ball(self.position[0] + other.position[0], self.position[1] + other.position[1])

class System():

    balls = []

    def add_ball(self, x, y):
        self.balls.append(Ball(x,y))

    def plot_balls(self):
        
        for ball in self.balls:
            plt.plot(ball.position[0], ball.position[1], "o")

        plt.show()

if __name__ == "__main__":
    system = System()
    system.add_ball(1,2)
    system.add_ball(2,1)
    system.plot_balls()
    ball = Ball(1,2) + Ball(2,1)
    print(ball.position)