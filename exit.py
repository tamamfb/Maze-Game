import turtle

# Exit Class
class Exit(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exit.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
