import turtle
from colors import COLOR_ZOMBIE

# Zombie Class dengan difficulty scaling
class Zombie(turtle.Turtle):
    def __init__(self, x, y, difficulty=1):
        turtle.Turtle.__init__(self)
        self.shape("assets/zombie.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.difficulty = difficulty  # 1, 2, 3 for levels
        self.color(COLOR_ZOMBIE)

    def get_speed(self):
        """Return zombie move interval based on difficulty"""
        if self.difficulty == 1:
            return 12
        elif self.difficulty == 2:
            return 8
        else:
            return 5
