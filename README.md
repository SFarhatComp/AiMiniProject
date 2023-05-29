# AiMiniProject
8Puzzle Solver
This repository contains a Python code that solves the 8Puzzle Quiz using various algorithms and heuristics. The 8Puzzle Quiz is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty tile. The objective of the puzzle is to rearrange the tiles from a given initial state to a target state by sliding them horizontally or vertically into the empty space.

How it works
The code in this repository utilizes the following components to solve the 8Puzzle Quiz:

State Generator: The state generator generates valid puzzle states by applying legal moves (sliding tiles) to the current state. Each generated state is added to a dictionary along with its depth (number of moves required to reach that state from the initial state).

Depth Calculation: The dictionary mentioned above is used to calculate the depth of each state. The depth represents the number of moves required to reach a particular state.

Algorithms: Multiple algorithms are implemented to solve the 8Puzzle Quiz. These algorithms include breadth-first search (BFS), depth-first search (DFS), and A* search.

Heuristics: The code incorporates multiple heuristics to estimate the cost of reaching the target state from a given state. These heuristics aid in making informed decisions during the search process and can improve the efficiency of the algorithms. Some commonly used heuristics include the misplaced tiles heuristic and the Manhattan distance heuristic.

Multiple Tries: The algorithms and heuristics are run on multiple tries to compare their performance. By executing them on various puzzle instances, we can evaluate their effectiveness and determine which combination yields the best results.


Getting Started
To use the 8Puzzle Solver code, follow these steps:

Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/8puzzle-solver.git
Install the required dependencies. The code utilizes Python 3, and you can install the necessary packages by running:

Copy code
pip install -r requirements.txt
Configure the initial and target states: In the code, specify the initial state of the puzzle and the desired target state.

Run the solver: Execute the Python script that implements the algorithms and heuristics to solve the 8Puzzle Quiz.


