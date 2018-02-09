import heapq
from maze_loader import MazeLoader
import time
from copy import deepcopy


class ASTARMazeSolver:

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
        self.astar(self.maze, self.maze.start, self.maze.end)
        # sol_arr = []
        # sol_set = set()
        point = self.maze.end
        #for coord in self.solution.keys():
        #    self.maze.maze_array[coord[0]][coord[1]] = '.'
        # print('solution', self.solution, '\n')
        self.solution.pop(0)
        self.solution.pop(0)
        for i in self.solution:
            (x,y) = i
            self.maze.maze_array[x][y] = '.'
        self.maze.maze_array[self.maze.start[0]][self.maze.start[1]] = 'P'
        # sol_arr.append(self.solution[self.maze.end])
        i,j = 0,0
        for item in self.maze.maze_array:
            for c in item:
                print(c, end= ' ')
            print()
        print('The number of nodes explored is: ', self.steps)
        print('The number of steps taken is: ' , len(self.solution))

    # def printer(self, solution):
    #     for i in range(len(self.maze.maze_array)):
    #         for j in range(len(self.maze.maze_array[0])):
    #             if (i,j) in solution:
    #                 print('.', end = ' ')
    #             else:
    #                 print(self.maze.maze_array[i][j],end=' ')
    #         print()

    def astar(self, maze, start, end):
        # print('end', end)
        pq = []
        heapq.heappush(pq, (self.manhattan_distance(start, end), start, 0, list(start)))
        cum_cost = {}
        cum_cost[start] = 0

        while(len(pq) != 0):
            self.steps += 1
            curr_point = heapq.heappop(pq)
            curr_cost = curr_point[2] #taking third value, cost, of pq tuple
            if curr_point[1] == end:
                self.solution = deepcopy(curr_point[3])
                self.solution.append((curr_point[1])) # adding current point to saved solution
                return
            x,y = curr_point[1][0], curr_point[1][1]

            self.solution = deepcopy(curr_point[3])
            self.solution.append((curr_point[1])) # adding current point to saved solution
            self.visited.add(curr_point[1]) # add tuple to visited
            # self.printer(self.solution)
            # time.sleep(0.05)
            if(self.maze.maze_array[x-1][y] != '%' and (x-1,y) not in self.visited):
                d = self.manhattan_distance((x-1,y), end) + curr_cost + 1
                curr_sol_1 = deepcopy(self.solution)
                temp_tuple_1 = (d, (x-1, y), curr_cost + 1, curr_sol_1)
                heapq.heappush(pq, temp_tuple_1)
            if(self.maze.maze_array[x+1][y] != '%' and (x+1,y) not in self.visited):
                d = self.manhattan_distance((x+1,y), end) + curr_cost + 1
                curr_sol_2 = deepcopy(self.solution)
                temp_tuple_2 = (d, (x+1, y), curr_cost + 1, curr_sol_2)
                heapq.heappush(pq, temp_tuple_2)
            if(self.maze.maze_array[x][y+1] != '%' and (x,y+1) not in self.visited):
                d = self.manhattan_distance((x,y+1), end) + curr_cost + 1
                curr_sol_3 = deepcopy(self.solution)
                temp_tuple_3 = (d, (x, y+1), curr_cost + 1, curr_sol_3)
                heapq.heappush(pq, temp_tuple_3)
            if(self.maze.maze_array[x][y-1] != '%' and (x,y-1) not in self.visited):
                d = self.manhattan_distance((x,y-1), end) + curr_cost + 1
                curr_sol_4 = deepcopy(self.solution)
                temp_tuple_4 = (d, (x, y-1), curr_cost + 1, curr_sol_4)
                heapq.heappush(pq, temp_tuple_4)

m = MazeLoader('mazes/medium.txt')
astar = ASTARMazeSolver(m)
t0 = time.clock()
astar.solve_maze()
t = time.clock() - t0
print('it took this long ', t)
#
# m = MazeLoader('mazes/bigmaze.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.solve_maze()
# t = time.clock() - t0
# print('it took this long ', t)
#
# m = MazeLoader('mazes/openmaze.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.solve_maze()
# t = time.clock() - t0
# print('it took this long ', t)
