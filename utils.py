from collections import deque

# Calculate Neighbors for Dijkstra
def get_neighbors(position, walls):
    x, y = position
    neighbors = [
        (x + 24, y),  # Right
        (x - 24, y),  # Left
        (x, y + 24),  # Up
        (x, y - 24)   # Down
    ]
    valid_neighbors = []
    for nx, ny in neighbors:
        if (nx, ny) not in walls:
            valid_neighbors.append((nx, ny))
    return valid_neighbors

# Dijkstra Algorithm to find shortest path
def dijkstra(start, goal, walls):
    queue = deque([(start, [start])])  # Queue contains (position, path)
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path  # Return the path when we reach the goal

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current, walls):
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return []  # Return empty path if no path is found

# Move zombie towards player
def move_zombie_towards_player(zombie, player, walls):
    start = (zombie.xcor(), zombie.ycor())
    goal = (player.xcor(), player.ycor())

    path = dijkstra(start, goal, walls)

    if path and len(path) > 1:
        next_position = path[1]
        zombie.goto(next_position[0], next_position[1])
