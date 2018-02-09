class SokobanLoader:

    input1 = 'puzzles/sokoban1.txt'
    input2 = 'puzzles/sokoban.txt'
    input3 = 'puzzles/sokobban.txt'
    input4 = 'puzzles/sokoban.txt'

    def __init__(self, puzzle):
        self.puzzle_array = []
        self.start = (-1, -1)
        self.end = (-1, -1)
        self.maze_x = -1
        self.maze_y = -1

        with open(puzzle) as p:
            
