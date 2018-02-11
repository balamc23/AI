import heapq
from maze_loader_suboptimal import MazeLoader
import time
from copy import deepcopy
from operator import itemgetter
import string

class MultiDotSolver:
    def __init__(self,maze):
        if(maze is None):
            print('Error: No maze is passed in')
        self.maze = maze
        self.visited = set()
        self.solution = list()
        self.steps = 0
        self.counter = 0
        self.length = 0

    def manhattan_distance(self, x,y):
        (x1, y1) = x
        (x2, y2) = y
        return abs(x1 - x2) + abs(y1 - y2)

    def solve_maze(self):
        # print('list of dots', self.maze.end)
        # print('num of dots', self.maze.num_dots)
        self.multidot(self.maze, self.maze.start, self.maze.end)
        #point = self.maze.endpoints
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
        print('The number of steps taken is: ' , self.length)



    def multidot(self, maze, start, end):
        #print('dim', self.maze.width, self.maze.height)
        alphabet = dict(zip(string.ascii_lowercase, range(1,27)))
        alpha = dict (zip(alphabet.values(),alphabet.keys()))
        #print('alpha' , alpha)
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
                result = self.astar(maze,first,point)
                total_cost = result[0]
                curr_cost = result[1]
                d_.append((total_cost, point,curr_cost))
            d_ = sorted(d_, key = lambda x: x[0])
            final_order.append(d_[0])
            self.length += d_[0][2]
            first =d_[0][1]
            self.maze.maze_array[d_[0][1][0]][d_[0][1][1]] = alpha[done_check+1]
            done_check +=1


    def astar(self, maze, start, end):
        #initializes all local variables needed
        #set to check for already visited cells
        visitited = set()
        #solution dict
        draw_solution = {start:start}
        solution = []
        solution_set = set()
        # Add start to queue
        ts = time.time()
        #q = queue.Queue()
        d = self.manhattan_distance(start,end)
        total_cost = d + 0
        q = [(total_cost, start,0)]
        visitited = set()
        maze_done  = 0
        nodes = 0
        
        while(len(q) != 0):
            curr_node= heapq.heappop(q)
            curr_pos = curr_node[1]
            curr_cost = curr_node[2]
            self.steps +=1
            neighbors = self.get_neighbors(curr_pos)
            for pos in neighbors:
                x, y = pos[0], pos[1]
                if(self.maze.maze_array[x][y] != '%'):
                    if(pos not in visitited):
                        d = self.manhattan_distance(pos,end)
                        total_cost = d + curr_cost + 1
                        heapq.heappush(q,(total_cost,pos, curr_cost+1))
                        #add pos to visited set
                        draw_solution[pos] =curr_pos
                        visitited.add(pos)
                if(self.maze.maze_array[x][y] == "."):
                    #print("found solution")
                    d = self.manhattan_distance(pos,end)
                    total_cost = d + curr_cost + 1
                    ts2 = time.time()
                    draw_solution[pos] =curr_pos
                    maze_done =1
                    return (total_cost, curr_cost+1)
                    break
            if(maze_done):
                break


    def get_neighbors(self, cell):
        x, y = cell[0], cell[1]
        return [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]



m = MazeLoader('mazes_suboptimal/tinySearch.txt')
astar = MultiDotSolver(m)
t0 = time.clock()
astar.solve_maze()
t = time.clock() - t0
print('it took this long ', t)

m = MazeLoader('mazes_suboptimal/smallSearch.txt')
astar = MultiDotSolver(m)
t0 = time.clock()
astar.solve_maze()
t = time.clock() - t0
print('it took this long ', t)

m = MazeLoader('mazes_suboptimal/mediumSearch.txt')
astar = MultiDotSolver(m)
t0 = time.clock()
astar.solve_maze()
t = time.clock() - t0
print('it took this long ', t)

