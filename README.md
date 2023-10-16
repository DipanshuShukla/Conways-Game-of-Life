# Game of Life Simulation

This is a simple Python project that implements Conway's Game of Life using the Tkinter library for the graphical user interface. The Game of Life is a cellular automaton devised by John Conway, which is known for its simplicity and complexity, and is often used in computer science and mathematics.

![Game of Life Demo](demo.gif)

## Project Structure

The project consists of two main Python files:

- `GOL.py`: This file contains the core logic for the Game of Life simulation and the Tkinter user interface.
- `runner.py`: This is the entry point for the project and initializes the Game of Life instance.

## How to Run

1. Make sure you have Python installed on your system.

2. Clone this repository to your local machine or download the project files.

3. Run the following command to start the Game of Life simulation:

   ```bash
   python runner.py
   ```

4. The Game of Life window will open, and you can interact with the simulation.

## Usage

- The Game of Life simulation initializes with a random grid of cells.
- You can control the speed of the simulation by modifying the `speed` parameter in `GOL.py`.
- The grid is displayed using the Tkinter library, and cells can be in one of two states: alive (black) or dead (white).
- The simulation will evolve following the rules of Conway's Game of Life, and you can observe the patterns that emerge.

## Customization

You can customize the simulation by modifying the parameters in the `gameofLife` class in `GOL.py`. For example, you can change the grid size, speed, and initial cell placement.

## Dependencies

This project uses standard Python libraries and does not rely on external dependencies beyond what's included in the Python standard library.