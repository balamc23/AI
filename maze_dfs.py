from maze_loader import MazeLoader
import time

class DFSMazeSolver:

    def __init__(self, maze):
        if(maze is None):
            print('Error: No maze passed in')
        self.maze = maze
        self.visited = set()
        self.solution = dict()
        self.steps = 0
        self.counter = 0

    # def print_maze(self, maze=None):
    #     if(maze is None):
    #         raise Exception('No maze passed in!')
    #     for row in maze.maze_array:
    #         for char in row:
    #             print(char, end=' ')
    #         print()
    #     print()

    def solve_maze(self):
        answer = self.find_dfs(self.maze.start)
        for coord in self.solution.keys():
            self.maze.maze_array[coord] = '.'
        for item in self.maze_array:
            for c in item:
                print(c, end=' ')
            print()


        # finish = self.maze.end
        # final = list()
        # while(finish != self.maze.start):
        #     x = finish[0]
        #     y = finish[1]
        #     print(finish)
        #     print(self.maze.maze_x, self.maze.maze_y)
        #     # try:
        #     next_move = self.solution[finish]
        #     # except Exception as e:
        #     print('printing', self.solution)
        #     final.append(next_move)
        #     self.maze.maze_array[next_move[0]][next_move[1]] = '@'
        #     self.steps += 1
        #     finish = next_move
            # print(final)
            # self.print_maze(answer)


    def find_dfs(self, current):
        self.counter += 1
        maze = self.maze
        search_path = []
        search_path.append(current)
        while(search_path):
            curr_point = search_path.pop()
            print(curr_point)
            self.solution[curr_point] = '.'
            x,y = curr_point[0], curr_point[1]
            if(curr_point == self.maze.end):
                for point in search_path:
                    self.maze.solution[search_path[point]] = '.'
                break
            if(self.maze.maze_array[x+1][y] != '%' and self.maze.maze_array[x+1][y] not in search_path):
                search_path.append((x+1,y))
            if(self.maze.maze_array[x-1][y] != '%' and self.maze.maze_array[x-1][y] not in search_path):
                search_path.append((x-1,y))
            if(self.maze.maze_array[x][y+1] != '%' and self.maze.maze_array[x][y+1] not in search_path):
                search_path.append((x,y+1))
            if(self.maze.maze_array[x][y-1] != '%' and self.maze.maze_array[x][y-1] not in search_path):
                search_path.append((x,y-1))
            # print(search_path)
            # break

        # neighbors = []
        # for i in range(2):
        #     for j in range(-1,2,2):
        #         if(i==0):
        #             xn=x+j
        #             yn=y
        #         else:
        #             xn=x
        #             yn=y+1
        #         neighbors.append((xn,yn))
        # for n in neighbors:
        #     a = n[0]
        #     b = n[1]
        #     if(self.maze.maze_array[a][b] != '%'):
        #         search_path.append(n)
        #     else:


        # if (current == self.maze.end):
        #     return maze
        # else:
        #     self.visited.add(current)
        # x = current[0]
        # y = current[1]
        # adj_points = []
        # for i in range(2):
        #     for j in range(-1,2,2):
        #         if(i==0):
        #             xn=x+j
        #             yn=y
        #         else:
        #             xn=x
        #             yn=y+1
        #         adj_points.append((xn,yn))
        # for adj in adj_points:
        #     x = adj[0]
        #     y = adj[1]
        #     if(maze.maze_array[x][y] == '%' or (x,y) in self.visited):
        #         continue
        #     elif(x < self.maze.maze_x-1 and x >= 1 and y < self.maze.maze_y-1 and y >= 1):
        #         self.solution[adj] = current
        #         self.find_dfs(adj)
        # return maze

m = MazeLoader('mazes/medium.txt')
dfs = DFSMazeSolver(m)
t0 = time.clock()
dfs.solve_maze()
t = time.clock() - t0
print('it took this long ', t)
