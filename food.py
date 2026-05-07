import turtle
import random
from colors import COLOR_FOOD

# Food Class
class Food(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("food.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.food_type = random.choice(["normal", "bonus"])  # 50% bonus food
        if self.food_type == "bonus":
            self.color("gold")  # Gold color for bonus
        else:
            self.color(COLOR_FOOD)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
