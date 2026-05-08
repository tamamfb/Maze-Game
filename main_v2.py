import turtle
import time

from colors import COLOR_PLAYER, COLOR_WALL, COLOR_FOOD
from pen import Pen
from player import Player
from food import Food
from levels import levels

# Setup Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("🧟 Zombie Maze Runner - Version 2 🧟")
wn.setup(800, 800)
wn.tracer(0)

# Register Shapes
turtle.register_shape("assets/player.gif")
turtle.register_shape("assets/wall.gif")
turtle.register_shape("assets/food.gif")

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
            
            if character == "T":
                foods.append(Food(screen_x, screen_y))

# Initialize Objects
pen = Pen()
player = Player()
walls = []
foods = []
current_level = 0
game_over_flag = False

# HUD Constants
HUD_TEXT_Y = 330
HUD_SCORE_X = -320
HUD_STAMINA_X = 320
STAMINA_BAR_X = 170
STAMINA_BAR_Y = 322
STAMINA_BAR_WIDTH = 120
STAMINA_BAR_HEIGHT = 18

# Display Elements
stamina_display = None
info_display = None

def init_displays():
    global stamina_display, info_display
    if stamina_display is None:
        stamina_display = Pen()
        stamina_display.color("yellow")
    if info_display is None:
        info_display = Pen()
        info_display.color("cyan")

def update_stamina_display():
    if stamina_display is None:
        return
    try:
        stamina_display.clear()
    except:
        pass
    
    # Draw stamina bar background
    stamina_display.penup()
    stamina_display.goto(STAMINA_BAR_X, STAMINA_BAR_Y)
    stamina_display.pendown()
    stamina_display.pensize(2)
    stamina_display.color("gray")
    
    for _ in range(2):
        stamina_display.forward(STAMINA_BAR_WIDTH)
        stamina_display.right(90)
        stamina_display.forward(STAMINA_BAR_HEIGHT)
        stamina_display.right(90)
    
    # Draw stamina bar fill
    stamina_display.penup()
    stamina_display.goto(STAMINA_BAR_X, STAMINA_BAR_Y)
    stamina_display.pendown()
    stamina_display.pensize(2)
    
    if player.stamina > 30:
        stamina_display.color("lime")
    elif player.stamina > 15:
        stamina_display.color("gold")
    else:
        stamina_display.color("red")
    
    bar_width = (player.stamina / player.max_stamina) * STAMINA_BAR_WIDTH
    for _ in range(2):
        stamina_display.forward(bar_width)
        stamina_display.right(90)
        stamina_display.forward(STAMINA_BAR_HEIGHT)
        stamina_display.right(90)
    
    stamina_display.penup()
    stamina_display.goto(HUD_STAMINA_X, HUD_TEXT_Y)
    stamina_display.color("white")
    stamina_display.write("HP: {}/{}".format(player.stamina, player.max_stamina), 
                          align="right", font=("Arial", 12, "bold"))

def update_info_display():
    if info_display is None:
        return
    try:
        info_display.clear()
    except:
        pass
    info_display.color("cyan")
    info_display.penup()
    info_display.goto(HUD_SCORE_X, HUD_TEXT_Y)
    info_display.write("Level: {} | Score: {} | Food: {}".format(current_level + 1, player.score, player.collected_foods), 
                       align="left", font=("Arial", 12, "normal"))

# Player Movement
def player_go_left():
    if not game_over_flag and player.stamina > 0:
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.decrease_stamina()
            player.score += 1

def player_go_right():
    if not game_over_flag and player.stamina > 0:
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.decrease_stamina()
            player.score += 1

def player_go_up():
    if not game_over_flag and player.stamina > 0:
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.decrease_stamina()
            player.score += 1

def player_go_down():
    if not game_over_flag and player.stamina > 0:
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            player.goto(move_to_x, move_to_y)
            player.decrease_stamina()
            player.score += 1

# Game Over
def game_over():
    global game_over_flag
    game_over_flag = True
    
    player.hideturtle()
    for food in foods:
        food.hideturtle()
    if stamina_display:
        stamina_display.hideturtle()
    if info_display:
        info_display.hideturtle()
    
    pen.clear()
    pen.goto(0, 50)
    pen.color("red")
    pen.write("STAMINA HABIS!", align="center", font=("Arial", 32, "bold"))
    pen.goto(0, 0)
    pen.color("gold")
    pen.write("Score: {}".format(player.score), align="center", font=("Arial", 18, "normal"))
    pen.goto(0, -60)
    pen.color("white")
    pen.write("Press 1 untuk restart", align="center", font=("Arial", 16, "normal"))

def restart_game():
    start_game(0)

# Keyboard Bindings
wn.listen()
wn.onkeypress(player_go_left, "Left")
wn.onkeypress(player_go_right, "Right")
wn.onkeypress(player_go_up, "Up")
wn.onkeypress(player_go_down, "Down")
wn.onkeypress(restart_game, "1")

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
    player.stamina = 60
    player.max_stamina = 60
    player.score = 0
    player.collected_foods = 0
    player.showturtle()
    
    walls.clear()
    foods.clear()
    
    init_displays()
    level_data = levels[level_index]
    setup_maze(level_data, level_index)

# Start the first level
start_game(0)

# Main Game Loop
while True:
    if not game_over_flag:
        # Check food collision
        for food in foods[:]:
            if player.is_collision(food):
                if food.food_type == "bonus":
                    player.add_stamina(20)
                else:
                    player.add_stamina(10)
                player.collected_foods += 1
                food.destroy()
                foods.remove(food)
        
        # Check stamina
        if player.stamina <= 0:
            game_over()
        
        # Update displays
        update_stamina_display()
        update_info_display()
    
    try:
        wn.update()
    except (turtle.Terminator, AttributeError):
        break
    
    time.sleep(0.01)
