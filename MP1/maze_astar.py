import heapq
from maze_loader import MazeLoader
import time


class ASTARMazeSolver:

    def __init__(self, maze):
        if(maze is None):
            print('Error: No maze passed in')
        self.maze = maze
        self.visited = set()
        self.solution = dict()
        self.steps = 0
        self.counter = 0

    def manhattan_distance(self, x, y):
        (x1, y1) = x
        (x2, y2) = y
        return abs(x1 - x2) + abs(y1 - y2)

    def solve_maze(self):
        self.astar(self.maze, self.maze.start, self.maze.end)
        sol_arr = []
        sol_set = set()
        point = self.maze.end
        #for coord in self.solution.keys():
        #    self.maze.maze_array[coord[0]][coord[1]] = '.'
        while(point != self.maze.start):
            point = self.solution[point]
            self.maze.maze_array[point[0]][point[1]] = '.'
        self.maze.maze_array[self.maze.start[0]][self.maze.start[1]] = 'P'
        sol_arr.append(self.solution[self.maze.end])
        i,j = 0,0
        for item in self.maze.maze_array:
            for c in item:
                if((i,j) in sol_set):
                    print(".", end= ' ')
                else:
                    print(c, end = ' ')
                j += 1
            j = 0
            i+=1
            print()

    def astar(self, maze, start, end):
        pq = []
        heapq.heappush(pq, start)
        # cum_cost = {}
        # cum_cost[start] = 0
        # prev[start] = None

        while(len(pq) != 0):
            curr_point = heapq.heappop(pq)
            prev = curr_point
            if curr_point == end:
                return
            x,y = curr_point[0], curr_point[1]
            # distances = []
            if(self.maze.maze_array[x-1][y] != '%' and (x-1,y) not in self.visited):
                self.visited.add((x-1,y))
                self.solution[(x-1,y)] = prev
                d = self.manhattan_distance((x-1,y), end)
                heapq.heappush(pq, (d, (x-1,y)))
                curr_point = (x-1,y)
            if(self.maze.maze_array[x][y+1] != '%' and (x,y+1) not in self.visited):
                self.visited.add((x,y+1))
                self.solution[(x,y+1)] = prev
                d = self.manhattan_distance((x,y+1), end)
                heapq.heappush(pq, (d, (x,y+1)))
                curr_point = (x,y+1)
            if(self.maze.maze_array[x+1][y] != '%' and (x+1,y) not in self.visited):
                self.visited.add((x+1,y))
                self.solution[(x+1,y)] = prev
                d = self.manhattan_distance((x+1,y), end)
                heapq.heappush(pq, (d, (x+1,y)))
                curr_point = (x+1,y)
            if(self.maze.maze_array[x][y-1] != '%' and (x,y-1) not in self.visited):
                self.visited.add((x,y-1))
                self.solution[(x,y-1)] = prev
                d = self.manhattan_distance((x,y-1), end)
                heapq.heappush(pq, (d, (x,y-1)))
                curr_point = (x,y-1)

m = MazeLoader('mazes/medium.txt')
astar = ASTARMazeSolver(m)
t0 = time.clock()
astar.solve_maze()
t = time.clock() - t0
print('it took this long ', t)
