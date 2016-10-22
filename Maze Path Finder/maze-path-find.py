# Hector Ferronato, 2016.
# Dynamic Programming Example.
# Find a path between origin (0,0) and goal (R-1,C-1).
# Can only move down and to the right.

import random

class Maze:
    def __init__(self, rows, cols):
        self.r = rows
        self.c = cols
        self.visited = {}
        self.pathList = []
        self.grid = self.__createGrid__()

    def __createGrid__(self):
        # This version performs with RxC grid, with R=R>1. 

        # Use to make sure R>1 and C>1.
        if self.r<=1: print("\t-Fix: Grid must have at least 2 rows."); self.r+=1
        if self.c<=1: print("\t-Fix:Grid must have at least 2 cols."); self.c+=1

        # Start grid, 0's are free positions.
        grid = [[0 for i in range(self.c)] for j in range(self.r)]

        # Randomly add some walls to grid, -1's are walls.
        for row in range(0,self.r-1):
            # This formula in range defines the ratio of walls among cells.
            for wallsPerRow in range(0,(min(self.c,self.r)/4)):
                randomIdx = random.randint(0,self.c-1)
                grid[row][randomIdx] = -1

        # Keep the origin and goal represented by a 0, so it's visitable.
        grid[0][0],grid[self.r-1][self.c-1] = 0,0

        return grid

    def printMaze(self, *positional_parameters, **keyword_parameters):
        if len(keyword_parameters)==0: grid = self.grid
        else: grid = keyword_parameters[0]

        print("\nMaze:\n")
        p = "  "
        for row in range(self.r):
            for column in range(self.c):
                if grid[row][column] >=0: p+= ("   "+str(grid[row][column]))
                else: p+= ("  "+str(grid[row][column]))
            print p; p = "  "

    def __markVisited__(self,i,j):
        if i == 0 and j == 1: self.visited[(i,j-1)] = (i,j)
        elif i == 1 and j == 0: self.visited[(i-1,j)] = (i,j)
        else:
            if (i-1,j) in self.visited.values(): self.visited[(i-1,j)] = (i,j)
            elif (i,j-1) in self.visited.values(): self.visited[(i,j-1)] = (i,j)

        self.grid[i][j] = "X";

    def traversePath(self, i, j):
        # Base Case of DP, if we reached the goal.
        if i==self.r-1 and j==self.c-1: 
            self.__markVisited__(i,j)
            return True

        # Recurse to try the cell below and cell to the right.
        if i<self.r and j<self.c and self.grid[i][j] == 0:

            self.__markVisited__(i,j)

            # Ensures that both directions have 50% chances of being picked first.
            randomness = random.random()
            if randomness>.5:
                if self.traversePath(i+1,j) or self.traversePath(i,j+1): return True
            else:
                if self.traversePath(i,j+1) or self.traversePath(i+1,j): return True

            return False
        return False

    def __getPath__(self):
        start = (0,0)
        path,current = [(0,0)],start

        # Creates pathList checking the previous cell that moved to current cell.
        while current != (self.r-1,self.c-1):
            self.pathList.append(current)
            current = self.visited[current]
        self.pathList.append((self.r-1,self.c-1))
        return self.pathList

    def printPath(self):
        pathListLen = len(self.pathList)
        s=("*Origin ("+str(self.pathList[0][0])
                      +","+str(self.pathList[0][1])
                      +")* -> ")
        for pair in range(1,pathListLen-1): 
            s+=("("+str(self.pathList[pair][0])
                   +","
                   +str(self.pathList[pair][1])+")"+" -> ")
        s+=("#("+str(self.pathList[pathListLen-1][0])
                +","+str(self.pathList[pathListLen-1][1])+") Goal# ")
        print(s+"\n")

    def printDetailedPath(self):
        self.__getPath__()
        s,n,rightSpaces = "\n     *",len(self.pathList),0

        for cellIdx in range(0,n-1):
            # If the path moves to the right.
            if self.pathList[cellIdx][1]<self.pathList[cellIdx+1][1]: 
                s,rightSpaces = s+("   *"),rightSpaces+1
            # If the path moves downwards.
            elif self.pathList[cellIdx][0]<self.pathList[cellIdx+1][0]: 
                s+=("\n"+" "*(rightSpaces*4)+"     *")
        
        # Print the goal cell, out of loop because of index range.
        if self.pathList[n-1][1]>self.pathList[cellIdx+1][1]: 
            s,rightSpaces = s+("   *"),rightSpaces+1
        elif self.pathList[n-1][0]>self.pathList[cellIdx+1][0]: 
            s+=("\n"+" "*(rightSpaces*4)+"     *")
        print(s)

def main():
    r,c = 7,7
    print("\nMaze with "+str(r)+" rows and "+str(c)+" columns.")
    maze = Maze(r,c)
    maze.printMaze()
    if(maze.traversePath(0,0)):
        print("\nMaze has been traversed.")
        maze.printMaze()
        print("\nPath in detail: ")
        maze.printDetailedPath()
        print("\nPath: \n")
        maze.printPath()
    else: print("\nNo path found.\n")

main()