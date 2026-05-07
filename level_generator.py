import random

def generate_dynamic_level(level_num=1):
    """
    Generate dynamic maze level
    level_num: difficulty (1-10+)
    """
    width = 25
    height = 25
    
    # Wall density - increase with level
    wall_density = 0.25 + (level_num * 0.02)  # More walls as level increases
    num_foods = 3 + level_num
    num_zombies = 1 + (level_num // 2)
    
    # Cap values
    wall_density = min(wall_density, 0.4)
    num_zombies = min(num_zombies, 5)
    
    # Create grid filled with empty spaces
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Border walls
    for x in range(width):
        grid[0][x] = 'X'
        grid[height-1][x] = 'X'
    for y in range(height):
        grid[y][0] = 'X'
        grid[y][width-1] = 'X'
    
    # Generate random walls (recursive backtracking)
    def carve_path(x, y):
        grid[y][x] = ' '
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width-1 and 0 < ny < height-1 and grid[ny][nx] == 'X':
                grid[y + dy//2][x + dx//2] = ' '
                carve_path(nx, ny)
    
    # Start maze generation from random position
    start_x = random.randint(1, width-2)
    start_y = random.randint(1, height-2)
    if start_x % 2 == 0:
        start_x -= 1
    if start_y % 2 == 0:
        start_y -= 1
    carve_path(start_x, start_y)
    
    # Add some random walls for variety
    for _ in range(int(width * height * 0.05)):
        x = random.randint(2, width-3)
        y = random.randint(2, height-3)
        if not (x == start_x and y == start_y):
            grid[y][x] = 'X'
    
    # Place player (top-left area)
    player_x = random.randint(2, 5)
    player_y = random.randint(2, 5)
    grid[player_y][player_x] = 'P'
    
    # Place exit (bottom-right area)
    exit_x = random.randint(width-6, width-3)
    exit_y = random.randint(height-6, height-3)
    grid[exit_y][exit_x] = 'E'
    
    # Place foods
    placed_foods = 0
    attempts = 0
    while placed_foods < num_foods and attempts < num_foods * 5:
        fx = random.randint(2, width-3)
        fy = random.randint(2, height-3)
        if grid[fy][fx] == ' ':
            grid[fy][fx] = 'T'
            placed_foods += 1
        attempts += 1
    
    # Place zombies
    placed_zombies = 0
    attempts = 0
    while placed_zombies < num_zombies and attempts < num_zombies * 10:
        zx = random.randint(2, width-3)
        zy = random.randint(2, height-3)
        # Don't place zombie too close to player
        if grid[zy][zx] == ' ' and abs(zx - player_x) + abs(zy - player_y) > 8:
            grid[zy][zx] = 'Z'
            placed_zombies += 1
        attempts += 1
    
    # Convert grid to string array format
    level = [''.join(row) for row in grid]
    return level


def generate_endless_levels(start_level=1, count=10):
    """
    Generate multiple levels for endless mode
    """
    levels = []
    for i in range(count):
        levels.append(generate_dynamic_level(start_level + i))
    return levels
