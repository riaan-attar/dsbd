from queue import PriorityQueue

# Function to calculate heuristic (Manhattan Distance)
def heuristic(a, b):
    # |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    # Priority queue stores elements in form: (priority, cost, position, path)
    pq = PriorityQueue()
    
    # Put starting position into queue with cost 0
    pq.put((0, 0, start, [start]))
    
    # To avoid revisiting nodes
    visited = set()

    while not pq.empty():
        # Get the best (lowest cost + heuristic) node
        priority, cost, current, path = pq.get()

        # If we already visited this cell, skip
        if current in visited:
            continue

        # Mark current cell as visited
        visited.add(current)

        # If goal is reached, return the path
        if current == goal:
            return path
        
        # Movement directions (Right, Left, Down, Up)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Try each direction
        for dx, dy in directions:
            new_x = current[0] + dx
            new_y = current[1] + dy

            # Check if inside maze and open path (0 means free to move)
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0:
                new_pos = (new_x, new_y)
                new_cost = cost + 1  # cost increases by 1 each move
                new_priority = new_cost + heuristic(new_pos, goal)  # A* rule: cost + heuristic
                # Add new state to priority queue
                pq.put((new_priority, new_cost, new_pos, path + [new_pos] ))

    # If no path found
    return None


# Example Maze (0 = path, 1 = wall)
maze = [
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0]
]

start = (0, 0)  # Starting cell
goal = (4, 4)   # Goal cell

# Run A*
result = astar(maze, start, goal)

# Print result
if result:
    print("Path found:")
    print(result)
else:
    print("No path found")
 