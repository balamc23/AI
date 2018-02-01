from maze_loader import MazeLoader

class DFSMazeSolver:

    def __init__(self, maze):
        if(maze is None):
            print('Error: No maze passed in')
        self.maze = maze
        self.visited = set()
        self.solution = dict()
        self.steps = 0
        self.counter = 0

    def print_maze(self, maze=None):
        if(maze is None):
            raise Exception('No maze passed in!')
        for row in maze.maze_array:
            for char in row:
                print(char, end=' ')
            print()
        print()

    def solve_maze(self):
        answer = self.find_dfs(self.maze.start)
        finish = self.maze.end
        final = list()
        while(finish != self.maze.start):
            x = finish[0]
            y = finish[1]
            print(finish)
            print(self.maze.maze_x, self.maze.maze_y)
            next_move = self.solution[finish]
            final.append(next_move)
            self.maze.maze_array[next_move[0]][next_move[1]] = '@'
            self.steps += 1
            finish = next_move
            # print(final)
            #self.print_maze(answer)


    def find_dfs(self, current):
        self.counter += 1
        maze = self.maze
        if (current == self.maze.end):
            return maze
        else:
            self.visited.add(current)
        x = current[0]
        y = current[1]
        adj_points = []
        for i in range(2):
            for j in range(-1,2,2):
                if(i==0):
                    xn=x+j
                    yn=y
                else:
                    xn=x
                    yn=y+1
                adj_points.append((xn,yn))
        for adj in adj_points:
            x = adj[0]
            y = adj[1]
            if(maze.maze_array[x][y] == '%' or current in self.visited):
                continue
            elif(x < self.maze.maze_x-1 and x >= 1 and y < self.maze.maze_y-1 and y >= 1):
                self.solution[adj] = current
                self.find_dfs(adj)
        return maze

m = MazeLoader('mazes/medium.txt')
dfs = DFSMazeSolver(m)
dfs.solve_maze()
