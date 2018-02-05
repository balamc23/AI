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

    def solve_maze(self):
        self.find_dfs(self.maze.start, None)
        sol_arr = []
        sol_set = set()
        end_point = self.maze.end
        #for coord in self.solution.keys():
        #    self.maze.maze_array[coord[0]][coord[1]] = '.'
        # while(end_point != self.maze.start):
        #     print(end_point[0], end_point[1])
        #     self.maze.maze_array[end_point[0]][end_point[1]] = '.'
        #     end_point = self.solution[end_point[0]][end_point[1]]
        #     print(end_point)
        sol_arr.append(self.solution[self.maze.end])
        #loop to add parent node
        i =1
        while sol_arr[i-1] != self.maze.start:
            dict_index = sol_arr[i-1]
            sol_arr.append(self.solution[dict_index])
            sol_set.add(sol_arr[i])
            i+=1
        print()

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


    def find_dfs(self, current, prev):
        self.counter += 1
        maze = self.maze
        search_path = []
        search_path.append(current)
        i = 0
        while(search_path):
            curr_point = search_path.pop()
            # print('current', curr_point)
            #self.solution[curr_point] = prev
            prev = curr_point
            x,y = curr_point[0], curr_point[1]
            if(curr_point == self.maze.end):
                return
            if(self.maze.maze_array[x+1][y] != '%' and (x+1,y) not in self.visited):
                search_path.append((x+1,y))
                self.visited.add((x+1,y))
                self.solution[(x+1,y)] = prev
                curr_point = (x+1,y)
            if(self.maze.maze_array[x-1][y] != '%' and (x-1,y) not in self.visited):
                search_path.append((x-1,y))
                self.visited.add((x-1,y))
                self.solution[(x-1,y)] = prev
                curr_point = (x-1,y)
            if(self.maze.maze_array[x][y+1] != '%' and (x,y+1) not in self.visited):
                search_path.append((x,y+1))
                self.visited.add((x,y+1))
                self.solution[(x,y+1)] = prev
                curr_point = (x,y+1)
            if(self.maze.maze_array[x][y-1] != '%' and (x,y-1) not in self.visited):
                search_path.append((x,y-1))
                self.visited.add((x,y-1))
                self.solution[(x,y-1)] = prev
                curr_point = (x,y-1)
            # print('search', search_path)
            # print('visited', self.visited)
            # print('solution', self.solution, '\n')
            i +=1
            # break
            # print(self.solution)

m = MazeLoader('mazes/medium.txt')
dfs = DFSMazeSolver(m)
t0 = time.clock()
dfs.solve_maze()
t = time.clock() - t0
print('it took this long ', t)

m = MazeLoader(MazeLoader.big)
dfs = DFSMazeSolver(m)
t0 = time.clock()
dfs.solve_maze()
t = time.clock() - t0
print('it took this long ', t)

m = MazeLoader(MazeLoader.last)
dfs = DFSMazeSolver(m)
t0 = time.clock()
dfs.solve_maze()
t = time.clock() - t0
print('it took this long ', t)
