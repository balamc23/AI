class MazeLoader:

    medium = 'mazes/medium.txt'
    big = 'mazes/bigmaze.txt'
    last = 'mazes/open.txt'

    def __init__(self, maze):
        self.maze_array = []
        self.start = (-1, -1)
        self.end = (-1, -1)

        with open(maze) as m:
            maze_lines = m.readlines()
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

            # print (self.start, self.end)
            # for item in self.maze_array:
            #     for c in item:
            #         print(c, end=' ')
            #     print()
MazeLoader(MazeLoader.medium)
