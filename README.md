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


To create a `requirements.txt` file for your Python project, you can follow these steps:

1. Activate your project's virtual environment (if you're using one). This step ensures that the dependencies you install are isolated to your project and won't conflict with other Python installations on your system.

2. Install the required packages for your project using `pip`. For example, if you install a package named `package1`, you can use the following command:

   ```
   pip install package1
   ```

   Repeat this step for all the packages your project depends on. Make sure you install the specific versions of the packages that your project requires.

3. Generate the `requirements.txt` file. Run the following command in your project's root directory:

   ```
   pip freeze > requirements.txt
   ```

   This command generates a `requirements.txt` file that lists all the installed packages and their respective versions in the current environment.

4. Review and modify the `requirements.txt` file if needed. It's a good practice to remove any unnecessary packages and update the versions of the packages to match the specific versions your project requires.

5. Commit the `requirements.txt` file to your Git repository along with your project code. This step ensures that other users who clone your repository can easily install the required dependencies.

That's it! You now have a `requirements.txt` file that contains the necessary packages and versions for your project.
