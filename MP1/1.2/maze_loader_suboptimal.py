class MazeLoader:

    medium = 'mazes_suboptimal/mediumSearch.txt'
    big = 'mazes_suboptimal/smallSearch.txt'
    last = 'mazes_suboptimal/tinySearch.txt'

    def __init__(self, maze):
        self.maze_array = []
        self.start = (-1, -1)
        self.end = []
        self.maze_x = -1
        self.maze_y = -1
        self.num_dots = 0

        with open(maze) as m:
            maze_lines = m.readlines()
            self.maze_x = len(maze_lines)
            self.maze_y = len(maze_lines[0])
            self.width = len(maze_lines[0])
            self.height = len(maze_lines)
            for i in range(len(maze_lines)):
                temp_array = []
                for j in range(len(maze_lines[i])):
                    curr_char = maze_lines[i][j]
                    temp_array.append(curr_char)
                    if curr_char == 'P':
                        self.start = (i, j)
                    if curr_char == '.':
                        self.end.append(i, j)
                        self.num_dots += 1

                temp_array = [c for c in temp_array if c != '\n']
                self.maze_array.append(temp_array)

            # print (self.start, self.end)
            # for item in self.maze_array:
            #     for c in item:
            #         print(c, end=' ')
            #     print()

            # for item in self.maze_array:
            #     for c in item:
            #         if(c == " "):
            #             print("*", end = ' ')
            #         else:
            #             print(c, end=' ')
            #     print()
            # for i in range(len(self.maze_array)):
            #     for j in range(len(self.maze_array[i])):
            #         if(self.maze_array[i][j] == " "):
            #             print("*", end = ' ')
            #         else:
            #             print(self.maze_array[i][j], end=' ')
            #     print()

#MazeLoader(MazeLoader.medium)
