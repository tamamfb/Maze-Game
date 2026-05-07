import turtle
from colors import COLOR_POWERUP

# PowerUp Class - Shield
class PowerUp(turtle.Turtle):
    def __init__(self, x, y, power_type="shield"):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.8, 0.8)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.power_type = power_type
        self.color(COLOR_POWERUP)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
