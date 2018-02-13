import heapq
from maze_loader_suboptimal import MazeLoader
import time
from copy import deepcopy
from operator import itemgetter
import string



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
        # print('list of dots', self.maze.end)
#        print('num of dots', self.maze.num_dots)
        self.astar(self.maze, self.maze.start, self.maze.end)
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
        print('Number of nodes expanded: ', self.steps)
        print('Total path cost: ' , len(self.solution)-1)

    def astar(self, maze, start, end):
#        print('dim', self.maze.width, self.maze.height)
        alphabet = dict(zip(string.ascii_lowercase, range(1,27)))
        alpha = dict (zip(alphabet.values(),alphabet.keys()))
#        print('alpha' , alpha)
        abcs = {}
        first = start
        d_ = []
        #self.maze.end.append(start)
#        print(self.maze.end)
        for i in range(len(self.maze.end)):
            # print('first', first, 'i', self.maze.end[i])
            x = self.manhattan_distance(first, self.maze.end[i])
            d_.append((x,self.maze.end[i]))
            first = self.maze.end[i]
        d_ = sorted(d_, key = lambda x: x[0])
        # print('list', d_, end = ' ')
        time.sleep(0.05)
        # print('end', end)
        pq = []
        heapq.heappush(pq, (self.manhattan_distance(start, d_[0][1]), start, 0, list(start)))
        #d_.pop(0)
        cum_cost = {}
        cum_cost[start] = 0
        sol_found = 0
        sol_found_set = set()
        i = 1
        while(len(pq) != 0 and len(d_) != 0):
           # print('list', d_, end = ' ')
            self.steps += 1
            curr_point = heapq.heappop(pq)
            curr_cost = curr_point[2] #taking third value, cost, of pq tuple
            if curr_point[1] in end and curr_point[1] not in sol_found_set:
                sol_found += 1
                sol_found_set.add(curr_point[1])
                # print('******', curr_point[1])
                self.maze.maze_array[curr_point[1][0]][curr_point[1][1]] = '~'
                # print("Solution Found")
                print(d_.pop(0))
                self.solution = deepcopy(curr_point[3])
                self.solution.append((curr_point[1])) # adding current point to saved solution
                # print('printing' , sol_found, curr_point[1])
                # print('solution: ', self.solution)
                # print('Cost', curr_cost)
                # print('self.sol', sol_found_set)
                i+=1
                while(len(pq) != 0):
                    heapq.heappop(pq)

                self.visited.clear()
                if(sol_found == self.maze.num_dots):
                    return
                #return
            x,y = curr_point[1][0], curr_point[1][1]
            # print(x,y)

            self.solution = deepcopy(curr_point[3])
            self.solution.append((curr_point[1])) # adding current point to saved solution
            self.visited.add(curr_point[1]) # add tuple to visited
            # self.printer(self.solution)
            # time.sleep(0.05)
            if(self.maze.maze_array[x-1][y] != '%' and (x-1,y) not in self.visited):
                d = self.manhattan_distance((x-1,y), d_[0][1]) + curr_cost + 1
                curr_sol_1 = deepcopy(self.solution)
                temp_tuple_1 = (d, (x-1, y), curr_cost + 1, curr_sol_1)
                heapq.heappush(pq, temp_tuple_1)
                #d_.pop(0)
            if(self.maze.maze_array[x+1][y] != '%' and (x+1,y) not in self.visited):
                d = self.manhattan_distance((x+1,y), d_[0][1]) + curr_cost + 1
                curr_sol_2 = deepcopy(self.solution)
                temp_tuple_2 = (d, (x+1, y), curr_cost + 1, curr_sol_2)
                heapq.heappush(pq, temp_tuple_2)
                #d_.pop(0)
            if(self.maze.maze_array[x][y+1] != '%' and (x,y+1) not in self.visited):
                d = self.manhattan_distance((x,y+1), d_[0][1]) + curr_cost + 1
                curr_sol_3 = deepcopy(self.solution)
                temp_tuple_3 = (d, (x, y+1), curr_cost + 1, curr_sol_3)
                heapq.heappush(pq, temp_tuple_3)
                #d_.pop(0)
            if(self.maze.maze_array[x][y-1] != '%' and (x,y-1) not in self.visited):
                d = self.manhattan_distance((x,y-1), d_[0][1]) + curr_cost + 1
                curr_sol_4 = deepcopy(self.solution)
                temp_tuple_4 = (d, (x, y-1), curr_cost + 1, curr_sol_4)
                heapq.heappush(pq, temp_tuple_4)
               #d_.pop(0)


m = MazeLoader('mazes_suboptimal/bigDots.txt')
dfs = ASTARMazeSolver(m)
t0 = time.clock()
dfs.solve_maze()
t = time.clock() - t0
print("Runtime in seconds: ", t)

# m = MazeLoader('mazes_suboptimal/tinySearch.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.solve_maze()
# t = time.clock() - t0
# print('it took this long ', t)

# m2 = MazeLoader('mazes_suboptimal/smallSearch.txt')
# astar = ASTARMazeSolver(m2)
# t0 = time.clock()
# astar.solve_maze()
# t = time.clock() - t0
# print('it took this long ', t)
# #
# m = MazeLoader('mazes_suboptimal/mediumSearch.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.solve_maze()
# t = time.clock() - t0
# print('it took this long ', t)
