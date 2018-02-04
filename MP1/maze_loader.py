class MazeLoader:

    medium = 'mazes/medium.txt'
    big = 'mazes/bigmaze.txt'
    last = 'mazes/openmaze.txt'

    def __init__(self, maze):
        self.maze_array = []
        self.start = (-1, -1)
        self.end = (-1, -1)
        self.maze_x = -1
        self.maze_y = -1

        with open(maze) as m:
            maze_lines = m.readlines()
            self.maze_x = len(maze_lines)
            self.maze_y = len(maze_lines[0])
            for i in range(len(maze_lines)):
                temp_array = []
                for j in range(len(maze_lines[i])):
                    curr_char = maze_lines[i][j]
                    temp_array.append(curr_char)
                    if curr_char == 'P':
                        self.start = (i, j)
                    if curr_char == '.':
                        self.end = (i, j)

                temp_array = [c for c in temp_array if c != '\n']
                self.maze_array.append(temp_array)
            # curr = (1,2)
            # self.maze_array[curr[0]][curr[1]] = '@'

            print (self.start, self.end)
            print(self.maze_y, self.maze_x)
            for item in self.maze_array:
                for c in item:
                    print(c, end=' ')
                print()

MazeLoader('mazes/medium.txt')
