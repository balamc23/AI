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
        final_order = []
        done_check = 0
        first = start
        loc_end = deepcopy(end)
        nodes = 0

        while(done_check != self.maze.num_dots):
        	d_ = []
        	for point in loc_end:
        		total_cost = MultiDotSolver.astar(maze,first,end_point)
        		d_.append((total_cost, end_point))
        	d_.sort(d_, key = lambda x: x[0])
        	final_order.append(d_[0])
        	first = loc_end.remove(d_[0])


    def astar(self, maze, start, end):
        # print('end', end)
        pq = []
        heapq.heappush(pq, (self.manhattan_distance(start, end), start, 0, list(start)))
        local_sol = []

        while(len(pq) != 0):
            self.steps += 1
            curr_point = heapq.heappop(pq)
            curr_cost = curr_point[2] #taking third value, cost, of pq tuple
            if curr_point[1] == end:
                local_sol = deepcopy(curr_point[3])
                local_sol.append((curr_point[1])) # adding current point to saved solution
                print('Cost', curr_cost)
                return curr_cost
            x,y = curr_point[1][0], curr_point[1][1]

            local_sol = deepcopy(curr_point[3])
            local_sol.append((curr_point[1])) # adding current point to saved solution
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
        # From start find total cost( M_dist + path_cost + points left) of every end point
        # Priotize largest man dist when checking each one
        # Take smallest total cost as point to go to first
        # From there do the exact same thing but do it from the end point you just went to
        # Boom thats it 
        # Time to code this shit

