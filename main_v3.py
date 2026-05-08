import turtle
import math
import random
from collections import deque
import time

from colors import COLOR_PLAYER, COLOR_ZOMBIE, COLOR_FOOD, COLOR_EXIT, COLOR_WALL
from pen import Pen
from player import Player
from zombie import Zombie
from food import Food
from exit import Exit
from levels import levels
from utils import dijkstra, get_neighbors, move_zombie_towards_player
from level_generator import generate_dynamic_level, generate_endless_levels
from menu import Menu

# Setup Screen dengan warna yang lebih menarik
wn = turtle.Screen()
wn.bgcolor("black")  # Black background
wn.title("🧟 Zombie Maze Runner 🧟")
wn.setup(800, 800)
wn.tracer(0)

# Register Shapes
turtle.register_shape("assets/player.gif")
turtle.register_shape("assets/zombie.gif")
turtle.register_shape("assets/wall.gif")
turtle.register_shape("assets/food.gif")
turtle.register_shape("assets/exit.gif")

# Maze Setup - dengan clearing yang lebih baik
def setup_maze(level, level_index=0):
    # Clear semua stamps dan drawings sebelumnya
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

            if character == "Z":
                # Difficulty scales with level
                if endless_mode:
                    difficulty = min(3, 1 + (endless_level_num // 3))  # Scale with wave
                else:
                    difficulty = level_index + 1  # Difficulty 1, 2, 3
                zombies.append(Zombie(screen_x, screen_y, difficulty))

            if character == "E":
                exits.append(Exit(screen_x, screen_y))

# Initialize Pen, Player, Walls, Foods, Zombies, Exits
pen = Pen()
player = Player()
walls = []
foods = []
zombies = []
exits = []
current_level = 0
is_paused = False
pause_display = None

# Endless Mode Variables
endless_mode = False
endless_level_num = 1
endless_generated_levels = []

# Menu system
main_menu = None
menu_active = False


# Stamina Display dengan visual bar - created lazily
stamina_display = None
info_display = None
HUD_TEXT_Y = 330
HUD_SCORE_X = -320
HUD_HP_X = 320
STAMINA_BAR_X = 170
STAMINA_BAR_Y = 322
STAMINA_BAR_WIDTH = 120
STAMINA_BAR_HEIGHT = 18

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
    stamina_display.setheading(0)
    stamina_display.goto(STAMINA_BAR_X, STAMINA_BAR_Y)
    stamina_display.pendown()
    stamina_display.pensize(2)
    stamina_display.color("gray")
    
    # Bar background (60 unit width = full stamina)
    for _ in range(2):
        stamina_display.forward(STAMINA_BAR_WIDTH)
        stamina_display.right(90)
        stamina_display.forward(STAMINA_BAR_HEIGHT)
        stamina_display.right(90)
    
    # Draw stamina bar fill
    stamina_display.penup()
    stamina_display.setheading(0)
    stamina_display.goto(STAMINA_BAR_X, STAMINA_BAR_Y)
    stamina_display.pendown()
    stamina_display.pensize(2)
    
    # Color based on stamina level
    if player.stamina > 30:
        stamina_display.color("lime")  # Green
    elif player.stamina > 15:
        stamina_display.color("gold")  # Yellow
    else:
        stamina_display.color("red")  # Red
    
    # Bar fill width = stamina * 2 pixels per point
    bar_width = (player.stamina / player.max_stamina) * STAMINA_BAR_WIDTH
    for _ in range(2):
        stamina_display.forward(bar_width)
        stamina_display.right(90)
        stamina_display.forward(STAMINA_BAR_HEIGHT)
        stamina_display.right(90)
    
    # Draw HP label on the same baseline as the score.
    stamina_display.penup()
    stamina_display.goto(HUD_HP_X, HUD_TEXT_Y)
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
    if endless_mode:
        info_display.write("🌀 Wave: {} | Score: {}".format(endless_level_num, player.score), align="left", font=("Arial", 12, "normal"))
    else:
        info_display.write("Score: {}".format(player.score), align="left", font=("Arial", 12, "normal"))

# Game Over Flag
game_over_flag = False

# Game Over Screen with Win Condition
def game_over(won=False):
    global game_over_flag, endless_mode, endless_level_num
    
    # Endless mode: auto-load next level when winning
    if won and endless_mode:
        endless_level_num += 1
        start_game(-1)  # -1 indicates endless mode
        return
    
    game_over_flag = True

    # Hide everything
    player.hideturtle()
    for food in foods:
        food.hideturtle()
    for zombie in zombies:
        zombie.hideturtle()
    for exit_point in exits:
        exit_point.hideturtle()
    if stamina_display:
        stamina_display.hideturtle()
    if info_display:
        info_display.hideturtle()

    # Create semi-transparent overlay effect with multiple rectangles
    overlay = Pen()
    overlay.goto(0, 0)
    overlay.color("black")
    overlay.pendown()
    overlay.pensize(1)
    for _ in range(2):
        overlay.forward(400)
        overlay.right(90)
        overlay.forward(400)
        overlay.right(90)
    overlay.hideturtle()

    # Display message
    pen.clear()
    pen.goto(0, 50)

    if won:
        pen.color(COLOR_EXIT)
        pen.write("🎉 YOU WIN! 🎉", align="center", font=("Arial", 32, "bold"))
        pen.goto(0, 0)
        pen.color("lime")
        pen.write("Final Score: {}".format(player.score), align="center", font=("Arial", 18, "normal"))
    else:
        pen.color("red")
        pen.write("💀 GAME OVER 💀", align="center", font=("Arial", 32, "bold"))
        pen.goto(0, 0)
        pen.color("gold")
        pen.write("Score: {}".format(player.score), align="center", font=("Arial", 18, "normal"))

    # Display options
    pen.goto(0, -60)
    pen.color("white")
    pen.write("Press M for Menu", align="center", font=("Arial", 16, "normal"))

    pen.goto(0, -100)
    pen.color("white")
    pen.write("Press Q to Quit", align="center", font=("Arial", 16, "normal"))

# Add Exit Collision Logic
def check_exit_collision():
    for exit_point in exits:
        if player.is_collision(exit_point):
            game_over(won=True)

# Pause/Resume game
def toggle_pause():
    global is_paused, pause_display
    is_paused = not is_paused
    
    if pause_display is None:
        pause_display = Pen()
    
    if is_paused:
        pause_display.goto(0, 0)
        pause_display.color(COLOR_EXIT)
        pause_display.write("|| PAUSED ||", align="center", font=("Arial", 24, "bold"))
    else:
        pause_display.clear()

# Clear screen function
def clear_screen():
    pen.clear()
    pen.hideturtle()
    pen.penup()

# Show Menu dengan visual yang lebih bagus
def show_menu():
    global game_over_flag, is_paused, walls, foods, zombies, exits, main_menu, menu_active
    game_over_flag = True
    is_paused = False
    menu_active = True

    # Clear dan hide semua game objects
    player.hideturtle()
    for food in foods:
        food.hideturtle()
    for zombie in zombies:
        zombie.hideturtle()
    for exit_point in exits:
        exit_point.hideturtle()
    if stamina_display:
        stamina_display.hideturtle()
    if info_display:
        info_display.hideturtle()
    
    # Reset lists untuk clean state
    walls.clear()
    foods.clear()
    zombies.clear()
    exits.clear()
    
    # Reset background
    wn.bgcolor("black")
    pen.clear()
    pen.penup()
    pen.hideturtle()

    # Create menu
    main_menu = Menu(wn)
    main_menu.draw_title("🧟 ZOMBIE MAZE GAME 🧟")
    
    # Add menu items
    main_menu.add_item(0, 60, "Level 1 (Easy)", COLOR_PLAYER, select_level_1)
    main_menu.add_item(0, 5, "Level 2 (Medium)", COLOR_PLAYER, select_level_2)
    main_menu.add_item(0, -50, "Level 3 (Hard)", COLOR_PLAYER, select_level_3)
    main_menu.add_item(0, -105, "🌀 Endless Mode", "cyan", select_endless_mode)
    
    main_menu.select_first()
    main_menu.draw()
    main_menu.draw_footer("Use UP/DOWN to navigate | ENTER Select | Q Quit")

# Close the Game
def close_game():
    wn.bye()

# Level selection wrappers - hanya bekerja saat game over
def select_level_1():
    start_game(0)

def select_level_2():
    start_game(1)

def select_level_3():
    start_game(2)

def select_endless_mode():
    start_game(-1)  # -1 indicates endless mode

# Menu navigation
def menu_up():
    global main_menu, menu_active
    if menu_active and main_menu:
        main_menu.select_prev()

def menu_down():
    global main_menu, menu_active
    if menu_active and main_menu:
        main_menu.select_next()

def menu_select():
    global main_menu, menu_active
    if menu_active and main_menu:
        main_menu.click_selected()

# Wrapper functions untuk player movement
def player_go_left():
    if not game_over_flag and player.stamina > 0 and not is_paused:
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            player.goto(player.xcor() - 24, player.ycor())
            player.decrease_stamina()

def player_go_right():
    if not game_over_flag and player.stamina > 0 and not is_paused:
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            player.goto(player.xcor() + 24, player.ycor())
            player.decrease_stamina()

def player_go_up():
    if menu_active:
        menu_up()
    elif not game_over_flag and player.stamina > 0 and not is_paused:
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            player.goto(player.xcor(), player.ycor() + 24)
            player.decrease_stamina()

def player_go_down():
    if menu_active:
        menu_down()
    elif not game_over_flag and player.stamina > 0 and not is_paused:
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            player.goto(player.xcor(), player.ycor() - 24)
            player.decrease_stamina()

# Keyboard Bindings - setup awal
wn.listen()
wn.onkeypress(player_go_left, "Left")
wn.onkeypress(player_go_right, "Right")
wn.onkeypress(player_go_up, "Up")
wn.onkeypress(player_go_down, "Down")
wn.onkeypress(menu_select, "Return")
wn.onkeypress(select_level_1, "1")
wn.onkeypress(select_level_2, "2")
wn.onkeypress(select_level_3, "3")
wn.onkeypress(select_endless_mode, "e")
wn.onkeypress(show_menu, "m")
wn.onkeypress(toggle_pause, "p")
wn.onkeypress(close_game, "q")

# Calculate Neighbors for Dijkstra
# Initialize Frame Counter
frame_count = 0

def start_game(level_index):
    global game_over_flag, current_level, is_paused, endless_mode, endless_level_num, endless_generated_levels
    global walls, foods, zombies, exits, menu_active
    game_over_flag = False
    is_paused = False
    menu_active = False
    
    # Endless mode
    if level_index == -1:
        endless_mode = True
        # Generate first batch of levels if not already generated
        if not endless_generated_levels:
            endless_generated_levels = generate_endless_levels(1, 20)
        
        # Get level from generated levels, generate more if needed
        if endless_level_num > len(endless_generated_levels):
            endless_generated_levels.extend(generate_endless_levels(endless_level_num, 5))
        
        current_level = endless_level_num - 1
        level_data = endless_generated_levels[current_level]
    else:
        # Standard mode
        endless_mode = False
        current_level = level_index
        level_data = levels[level_index]

    # Clean up menu if it exists
    if main_menu:
        main_menu.cleanup()
    
    # Initialize displays
    init_displays()

    # Set background dan clear screen
    wn.bgcolor("black")
    pen.clear()
    pen.penup()
    pen.hideturtle()
    
    # Hide semua objects dari level sebelumnya
    player.hideturtle()
    for food in foods:
        food.hideturtle()
    for zombie in zombies:
        zombie.hideturtle()
    for exit_point in exits:
        exit_point.hideturtle()
    
    pen.clear()
    pen.penup()
    pen.hideturtle()

    # Reset player, walls, foods, zombies, and exits
    player.goto(-288, 288)
    player.stamina = 60
    player.max_stamina = 60
    player.score = 0
    player.collected_foods = 0
    player.showturtle()
    
    walls.clear()
    foods.clear()
    zombies.clear()
    exits.clear()

    setup_maze(level_data, current_level)
    
    # Don't update displays yet - let main loop handle it
    # to avoid turtle state issues


show_menu()

# Main Game Loop
while True:
    if not game_over_flag and not is_paused:
        # Food collision
        for food in foods[:]:
            if player.is_collision(food):
                if food.food_type == "bonus":
                    player.add_stamina(20)
                else:
                    player.add_stamina(10)
                player.collected_foods += 1
                food.destroy()
                foods.remove(food)

        # Zombie collision
        for zombie in zombies:
            if player.is_collision(zombie):
                game_over()

        # Check exit collision (win condition)
        check_exit_collision()

        # Check if stamina is 0 (lose condition)
        if player.stamina <= 0:
            game_over(won=False)

        # Update displays
        update_stamina_display()
        update_info_display()

        # Increment frame counter
        frame_count += 1

        # Move zombies dengan difficulty scaling
        for zombie in zombies:
            zombie_interval = zombie.get_speed()
            if frame_count % zombie_interval == 0:
                move_zombie_towards_player(zombie, player, walls)

    # Update the screen
    try:
        wn.update()
    except (turtle.Terminator, AttributeError):
        # Handle window closure gracefully
        break

    # Add a small delay to control the overall game speed
    time.sleep(0.01)
