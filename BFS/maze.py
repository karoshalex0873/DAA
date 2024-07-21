import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from matplotlib.animation import FuncAnimation

def generate_maze(rows, cols):
    """
    Generate a simple maze using random walls.
    
    :param rows: Number of rows in the maze
    :param cols: Number of columns in the maze
    :return: 2D list representing the maze
    """
    maze = np.zeros((rows, cols), dtype=int)
    # Randomly place walls (1's) in the maze
    for r in range(rows):
        for c in range(cols):
            if (r, c) != (0, 0) and (r, c) != (rows-1, cols-1):
                maze[r, c] = np.random.choice([0, 1], p=[0.7, 0.3])
    return maze

def bfs(grid, start, goal):
    """
    Perform Breadth-First Search to find the shortest path in an unweighted grid.
    
    :param grid: 2D list representing the grid
    :param start: Tuple (row, col) representing the start position
    :param goal: Tuple (row, col) representing the goal position
    :return: List of tuples representing the path from start to goal
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    queue = deque([start])
    parent = {start: None}
    visited = set()
    visited.add(start)

    path = []  # To store the path found

    while queue:
        current = queue.popleft()

        # Check if we have reached the goal
        if current == goal:
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path

        # Explore neighbors
        for dr, dc in directions:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in visited:
                neighbor = (r, c)
                parent[neighbor] = current
                queue.append(neighbor)
                visited.add(neighbor)

    return []  # No path found

def plot_maze_animation(grid, path=None, visited_cells=None):
    """
    Plot the maze and animate the BFS process.
    
    :param grid: 2D list representing the grid
    :param path: List of tuples representing the path to highlight
    :param visited_cells: List of tuples representing cells visited during BFS
    """
    grid_np = np.array(grid)
    fig, ax = plt.subplots(figsize=(6, 6))
    img = ax.imshow(grid_np, cmap='gray_r', interpolation='none')
    ax.set_title("Maze Visualization")

    if path:
        path_np = np.array(path)
        ax.scatter(path_np[:, 1], path_np[:, 0], color='red', s=100, label='Path')

    if visited_cells:
        visited_cells_np = np.array(visited_cells)
        scatter = ax.scatter(visited_cells_np[:, 1], visited_cells_np[:, 0], color='blue', s=100, alpha=0.5, label='Visited Cells')

    def update(frame):
        if frame < len(visited_cells):
            scatter.set_offsets(visited_cells_np[:frame+1])
        return scatter,

    ani = FuncAnimation(fig, update, frames=len(visited_cells)+1, repeat=False, interval=100)

    plt.colorbar(img)
    plt.legend()
    plt.grid(True)  # Show grid lines
    plt.show()

# Generate a random maze
rows, cols = 10, 10
maze = generate_maze(rows, cols)

# Define start and goal positions
start = (0, 0)
goal = (rows - 1, cols - 1)

# Solve the maze using BFS
path = bfs(maze, start, goal)

# Visualize the maze and the BFS animation
if path:
    visited_cells = list(set((r, c) for r in range(rows) for c in range(cols) if maze[r, c] == 0))
    plot_maze_animation(maze, path, visited_cells)
else:
    print("No path found!")
