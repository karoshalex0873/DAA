# Sokoban Game with Dijkstra's Algorithm

This project implements a Sokoban game using Dijkstra's algorithm for pathfinding. The game is built using Python and Pygame for visualization and animations.

## Game Description

Sokoban is a classic puzzle game where the player pushes boxes to specified goals. The objective is to move all boxes to their designated locations using the shortest path. This implementation uses Dijkstra's algorithm to calculate the shortest path for moving the player and the boxes.

## Features

- Grid-based game environment
- Pathfinding using Dijkstra's algorithm
- Visualization and animations using Pygame

## Getting Started

### Prerequisites

- Python 3.x
- Pygame

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/sokoban-game.git
    cd sokoban-game
    ```

2. **Install Pygame**:

    ```bash
    pip install pygame
    ```

### Running the Game

1. **Navigate to the project directory**:

    ```bash
    cd sokoban-game
    ```

2. **Run the game**:

    ```bash
    python sokoban_game.py
    ```

## How to Play

- Use the `SPACE` key to trigger the pathfinding and animation.
- The player (`P`) will move towards the box (`B`), and the box will move towards the goal (`G`).

## Project Structure

- `sokoban_game.py`: Main game file containing the game logic and Pygame setup.
- `README.md`: Project documentation and setup instructions.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Pygame: [Pygame](https://www.pygame.org)
- Dijkstra's Algorithm: [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
