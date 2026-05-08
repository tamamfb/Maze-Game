import turtle
import time

from colors import COLOR_PLAYER, COLOR_WALL
from pen import Pen
from player import Player
from levels import levels

# Setup Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("🧟 Zombie Maze Runner - Version 1 🧟")
wn.setup(800, 800)
wn.tracer(0)

# Register Shapes
turtle.register_shape("assets/player.gif")
turtle.register_shape("assets/wall.gif")

# Maze Setup
def setup_maze(level, level_index=0):
    pen.clear()
    pen.hideturtle()
    
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("assets/wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))
            
            if character == "P":
                player.goto(screen_x, screen_y)

# Initialize Pen, Player, Walls
pen = Pen()
player = Player()
walls = []
current_level = 0
game_over_flag = False

# Display Info
def update_info_display():
    pen.penup()
    pen.goto(-300, 330)
    pen.color("cyan")
    pen.write("Level: {} | Score: {}".format(current_level + 1, player.score), 
              align="left", font=("Arial", 12, "normal"))

# Player Movement Functions
def player_go_left():
    if not game_over_flag:
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.score += 1

def player_go_right():
    if not game_over_flag:
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.score += 1

def player_go_up():
    if not game_over_flag:
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.score += 1

def player_go_down():
    if not game_over_flag:
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.score += 1

# Keyboard Bindings
wn.listen()
wn.onkeypress(player_go_left, "Left")
wn.onkeypress(player_go_right, "Right")
wn.onkeypress(player_go_up, "Up")
wn.onkeypress(player_go_down, "Down")

def start_game(level_index):
    global game_over_flag, current_level
    game_over_flag = False
    current_level = level_index
    
    wn.bgcolor("black")
    pen.clear()
    pen.penup()
    pen.hideturtle()
    
    player.hideturtle()
    player.goto(-288, 288)
    player.score = 0
    player.showturtle()
    
    walls.clear()
    level_data = levels[level_index]
    setup_maze(level_data, level_index)

# Start the first level
start_game(0)

# Main Game Loop
while True:
    update_info_display()
    
    try:
        wn.update()
    except (turtle.Terminator, AttributeError):
        break
    
    time.sleep(0.01)
