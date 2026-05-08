import turtle
import math

# Player Class dengan system stamina dan score
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("assets/player.gif")
        self.penup()
        self.speed(0)
        self.stamina = 60
        self.max_stamina = 60
        self.score = 0
        self.collected_foods = 0

    def decrease_stamina(self):
        if self.stamina > 0:
            self.stamina -= 1
        if self.stamina <= 0:
            self.stamina = 0

    def add_stamina(self, amount):
        self.stamina = min(self.stamina + amount, self.max_stamina)
        self.score += 50

    def add_score(self, points):
        self.score += points

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        return distance < 5
