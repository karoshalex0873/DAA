import pygame
import heapq
import sys

# Define constants
TILE_SIZE = 50
GRID_SIZE = 5
SCREEN_SIZE = GRID_SIZE * TILE_SIZE

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define grid
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 'G', 1, 0],
    [0, 0, 0, 1, 0],
    [0, 'P', 'B', 0, 0]
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Sokoban Game")

class SokobanGame:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        self.player_pos = self.find_element('P')
        self.box_pos = self.find_element('B')
        self.goal_pos = self.find_element('G')

    def find_element(self, element):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.grid[y][x] == element:
                    return (x, y)
        return None

    def is_valid(self, x, y):
        return 0 <= x < self.cols and 0 <= y < self.rows and self.grid[y][x] != 1

    def dijkstra(self, start, goal):
        pq = []
        heapq.heappush(pq, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while pq:
            current_cost, current = heapq.heappop(pq)

            if current == goal:
                break

            for dx, dy in self.directions:
                nx, ny = current[0] + dx, current[1] + dy
                if self.is_valid(nx, ny):
                    new_cost = current_cost + 1  # Assuming uniform cost for each move
                    if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                        cost_so_far[(nx, ny)] = new_cost
                        priority = new_cost
                        heapq.heappush(pq, (priority, (nx, ny)))
                        came_from[(nx, ny)] = current

        return self.reconstruct_path(came_from, start, goal)

    def reconstruct_path(self, came_from, start, goal):
        if goal not in came_from:
            return []  # No path found
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path

    def move_box(self, player_path, box_path):
        for pos in player_path[1:]:
            self.player_pos = pos
            self.draw_grid()
            pygame.time.wait(100)
        for pos in box_path[1:]:
            self.box_pos = pos
            self.draw_grid()
            pygame.time.wait(100)

    def draw_grid(self, path=None):
        screen.fill(WHITE)
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, BLACK, rect)
                elif (x, y) == self.player_pos:
                    pygame.draw.rect(screen, BLUE, rect)
                elif (x, y) == self.box_pos:
                    pygame.draw.rect(screen, RED, rect)
                elif (x, y) == self.goal_pos:
                    pygame.draw.rect(screen, GREEN, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

        if path:
            for pos in path:
                rect = pygame.Rect(pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, BLUE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)
        
        pygame.display.flip()

def main():
    game = SokobanGame(grid)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_path = game.dijkstra(game.player_pos, game.box_pos)
                    box_path = game.dijkstra(game.box_pos, game.goal_pos)
                    if player_path and box_path:
                        game.move_box(player_path, box_path)
        
        game.draw_grid()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
