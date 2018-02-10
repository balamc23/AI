import heapq
from maze_loader_suboptimal import MazeLoader
import time
from copy import deepcopy
from operator import itemgetter
import string

class MultiDotSolver:

	 def __init__(self, maze):
        if(maze is None):
            print('Error: No maze passed in')
        self.maze = maze
        self.visited = set()
        self.solution = list()
        self.steps = 0
        self.counter = 0

    def manhattan_distance(self, x, y):
        (x1, y1) = x
        (x2, y2) = y
        return abs(x1 - x2) + abs(y1 - y2)

    def solve_maze(self):
        # print('list of dots', self.maze.end)
        # print('num of dots', self.maze.num_dots)
        self.multidot(self.maze, self.maze.start, self.maze.end)
        #point = self.maze.endpoints
        self.solution.pop(0)
        self.solution.pop(0)
        # print('solution', self.solution)
        for i in self.solution:
            (x,y) = i
            # self.maze.maze_array[x][y] = '.'
        self.maze.maze_array[self.maze.start[0]][self.maze.start[1]] = 'P'
        for item in self.maze.maze_array:
            for c in item:
                print(c, end= ' ')
            print()
        print('The number of nodes explored is: ', self.steps)
        print('The number of steps taken is: ' , len(self.solution)-1)

    def multidot(self, maze, start, end):
    	print('dim', self.maze.width, self.maze.height)
        alphabet = dict(zip(string.ascii_lowercase, range(1,27)))
        alpha = dict (zip(alphabet.values(),alphabet.keys()))
        print('alpha' , alpha)
        abcs = {}
        first = start
        d_ = []

        # From start find total cost( M_dist + path_cost + points left) of every end point
        # Priotize largest man dist when checking each one
        # Take smallest total cost as point to go to first
        # From there do the exact same thing but do it from the end point you just went to
        # Boom thats it 
        # Time to code this shit