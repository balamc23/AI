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
        point = self.maze.end
        self.solution.pop(0)
        self.solution.pop(0)
        for i in self.solution:
            (x,y) = i
            self.maze.maze_array[x][y] = '.'
        self.maze.maze_array[self.maze.start[0]][self.maze.start[1]] = 'P'
        for item in self.maze.maze_array:
            for c in item:
                print(c, end= ' ')
            print()
        print('The number of nodes explored is: ', self.steps)
        print('The number of steps taken is: ' , len(self.solution)-1)

    def printer(self, solution):
        for i in range(len(self.maze.maze_array)):
            for j in range(len(self.maze.maze_array[0])):
                if (i,j) in solution:
                    print('.', end = ' ')
                else:
                    print(self.maze.maze_array[i][j],end=' ')
            print()

    def astar(self, maze, start, end):
        # print('end', end)
        pq = []
        heapq.heappush(pq, (self.manhattan_distance(start, end), start, 0, list(start)))
        cum_cost = {}
        cum_cost[start] = 0

        while(len(pq) != 0):
            self.steps += 1
            curr_point = heapq.heappop(pq)
            print(curr_point[1])
            curr_cost = curr_point[2] #taking third value, cost, of pq tuple
            if curr_point[1] == end:
                print("found solution")
                self.solution = deepcopy(curr_point[3])
                self.solution.append((curr_point[1])) # adding current point to saved solution
                print('Cost', curr_cost)
                return
            x,y = curr_point[1][0], curr_point[1][1]

            self.solution = deepcopy(curr_point[3])
            self.solution.append((curr_point[1])) # adding current point to saved solution
            self.visited.add(curr_point[1]) # add tuple to visited
            self.printer(self.solution)
            time.sleep(0.05)
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

    def astar2(self):
        #initializes all local variables needed
        start = self.maze.start
        end = self.maze.end
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
            nodes +=1

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
                    print("found solution")
                    ts2 = time.time()
                    draw_solution[pos] =curr_pos
                    maze_done =1
                    break
            if(maze_done):
                break


        # Set end as top node
        solution.append(draw_solution[end])
        #loop to add parent node
        i =1
        while solution[i-1] != self.maze.start:
            dict_index = solution[i-1]
            solution.append(draw_solution[dict_index])
            solution_set.add(solution[i])
            i+=1


        point = end
        # self.printer(solution)
        # time.sleep(0.05)
        while(point != self.maze.start):
            point = draw_solution[point]
            self.maze.maze_array[point[0]][point[1]] = '.'
        self.maze.maze_array[start[0]][start[1]] = "P"

        for item in self.maze.maze_array:
            for c in item:
                print(c, end = ' ')
            print()
        print(solution)


        print(nodes, "nodes expanded")
        print(len(solution), "steps in path")
        print((ts2-ts), "Seconds")
        print()

    def get_neighbors(self, cell):
        x, y = cell[0], cell[1]
        return [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]

# m = MazeLoader('mazes/medium.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.solve_maze()
# t = time.clock() - t0
# print('it took this long ', t)

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

m = MazeLoader('mazes/medium.txt')
astar = ASTARMazeSolver(m)
t0 = time.clock()
astar.astar2()
t = time.clock() - t0
print('it took this long ', t)

# m = MazeLoader('mazes/bigmaze.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.astar2()
# t = time.clock() - t0
# print('it took this long ', t)
#
# m = MazeLoader('mazes/openmaze.txt')
# astar = ASTARMazeSolver(m)
# t0 = time.clock()
# astar.astar2()
# t = time.clock() - t0
# print('it took this long ', t)
