import turtle
import math
import random

# Color definitions
COLOR_WALL = "darkblue"
COLOR_PLAYER = "lime"
COLOR_ZOMBIE = "red"
COLOR_FOOD = "gold"
COLOR_POWERUP = "cyan"
COLOR_EXIT = "lightgreen"

# Pen Class untuk text dan shapes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()

# Player Class dengan system stamina dan score
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("player.gif")
        self.penup()
        self.speed(0)
        self.stamina = 60
        self.max_stamina = 60
        self.score = 0
        self.has_shield = False
        self.shield_time = 0
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

    def activate_shield(self):
        self.has_shield = True
        self.shield_time = 150  # 15 detik dengan 0.01s per frame

    def update_shield(self):
        if self.has_shield:
            self.shield_time -= 1
            if self.shield_time <= 0:
                self.has_shield = False

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        return distance < 5

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

# Zombie Class dengan difficulty scaling
class Zombie(turtle.Turtle):
    def __init__(self, x, y, difficulty=1):
        turtle.Turtle.__init__(self)
        self.shape("zombie.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.difficulty = difficulty  # 1, 2, 3 for levels

    def get_speed(self):
        """Return zombie move interval based on difficulty"""
        if self.difficulty == 1:
            return 12
        elif self.difficulty == 2:
            return 8
        else:
            return 5

# Exit Class
class Exit(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exit.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
