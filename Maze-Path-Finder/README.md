# Maze Path Finder
Find out if there is a path from origin (0,0) to goal (r,c), only moving down or to the right, using Dynamic Programming.

This class implements a solution to find a path that can traverse a Maze by moving downards or to the right.

The Maze is represented my a matrix (grid), with r (# of rows) x c (# of columns) size, where 0's represent free spaces, -1's
represent walls that stop any path.

- **[maze-path-find.py](/maze-path-find.py)**

   Run: $ python maze-path-find.py

   ![Screenshot](imgs/maze.png?raw=true "Maze Path Details.")

   Class structure:

        *def __init__(self, rows, cols)* - Initializer

        *def __createGrid__(self)* - Creates and fills a r x c Grid, with 0's and -1's on it.

        *def printMaze(self, *positional_parameters, **keyword_parameters)* - Prints the Grid (Matrix).

        *def __markVisited__(self,i,j)* - Marks with "X" every path the algorithm explored.

        *def traversePath(self, i, j)* - DP algorithm to explore in two directions and check if any path leads to the goal (r,c).

        *def __getPath__(self)* - Backtrack from goal to origin in visited list, creating a path.

        *def printPath(self)* - Prints the path to the goal, with ea ch position (x,y), for 0<=x<=r, 0<=y<=c.

        *def printDetailedPath(self)* - Prints the detials of the path without the Grid(Matrix).

        *def main()* - Testes/Caller
