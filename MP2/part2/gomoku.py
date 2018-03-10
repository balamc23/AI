import numpy as np

alphabet = {}
alphabet['r'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet['b'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
directions = ['DL', 'L', 'UL', 'U']


class Gomoku:

    def __init__(self):
        self.board = [['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.']
                      ]
        # index stones at r for red
        # index stones at b for blue
        self.stones = {}
        self.stones['r'] = []
        self.stones['b'] = []

    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end=' ')
            print()

    def reflex(self, color):
        for point in self.stones[color]:
            # neighbors = self.get_neighbors(point)
            # y,x, direction = neighbors[0], neighbors[1], neighbors[2]
            for d in directions:
                length, start, end, direction = self.stone_chain(point, d, color)
                print(point, length, d)
                x_start, y_start, x_end, y_end = start[0], start[1], end[0], end[1]
                print('Info', x_start, y_start, x_end, y_end, point)
                if(length == 4):
                    if(direction == 'L'):
                        print('End, x_end', end, x_end)
                        # check left side first then right
                        value = self.board[y_start][x_start - 1]
                        if(value == '.'):
                            self.stones[color].append((y_start, x_start - 1))
                            self.board[y_start][x_start - 1] = alphabet[color][len(self.stones[color])-1]
                            return
                        else:
                            self.stones[color].append((y_end, x_end + 1))
                            self.board[y_end][x_end + 1] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return
                        else:
                            self.stones[color].append((y_start - 1, x_start))
                            self.board[y_start - 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return

   # def get_neighbors(self, cell):
   #      x, y = cell[0], cell[1]
   #      return [
   #          (x - 1, y,'L'),       #left
   #          # (x + 1, y),     #right
   #          (x, y - 1,'U'),       #up
   #          # (x, y + 1),     #down
   #          (x - 1, y - 1,'UL'),  #up-left
   #          # (x + 1, y - 1), #up-right
   #          (x - 1, y + 1,'DL'),  #down-left
   #          # (x + 1, y + 1)  #down-right
   #      ]

    def stone_chain(self, point, direction, color):
        y, x = point[0], point[1]
        count = 1
        # down-left
        if(direction == 'DL'):
            value = self.board[y][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r'):
                    if(value.isupper()):
                        break
                    x = x - 1
                    y = y + 1

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break
                    x = x-1
                    y = y+1
                value = self.board[y][x]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            value = self.board[y][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r'):
                    if(value.isupper()):
                        break
                    x = x+1
                    y = y-1

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break
                    x = x+1
                    y = y-1

                end = (x, y)
                value = self.board[y][x]
                count += 1
            # return something, (length, start, end, direction?)
            return count, start, end, direction

        # left
        elif(direction == 'L'):
            value = self.board[y][x-1]
            while(value != '.'):
                # dealing with red
                if(color == 'r' and value.isupper()):
                    break

                # dealing with blue
                elif(not value.isupper()):
                    break
                x = x - 1

                value = self.board[y][x-1]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            print('start, end', start, end)
            value = self.board[y][x+1]
            while(value != '.'):
                print(x)
                # dealing with red

                if(color == 'r'):
                    if(value.isupper()):
                        break

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break

                x = x + 1
                count += 1
                end = (x, y)
                value = self.board[y][x + 1]
            # return something, (length, start, end, direction?)
            print('start, end after', start, end)
            return count, start, end, direction

        # up-left
        elif(direction == 'UL'):
            value = self.board[y][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r'):
                    if(value.isupper()):
                        break
                    x = x-1
                    y = y-1

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break
                    x = x-1
                    y = y-1
                value = self.board[y][x]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            value = self.board[y][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r'):
                    if(value.isupper()):
                        break
                    x = x+1
                    y = y+1

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break
                    x = x+1
                    y = y+1

                end = (x, y)
                value = self.board[y][x]
                count += 1
            # return something, (length, start, end, direction?)
            return count, start, end, direction

        # up
        else:
            value = self.board[y][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r'):
                    if(value.isupper()):
                        break
                    y = y-1

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break
                    y = y-1
                value = self.board[y][x]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            value = self.board[y][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r'):
                    if(value.isupper()):
                        break
                    y = y+1

                # dealing with blue
                else:
                    if(not value.isupper()):
                        break
                    y = y+1

                end = (x, y)
                value = self.board[y][x]
                count += 1
            # return something, (length, start, end, direction?)
            return count, start, end, direction


g = Gomoku()
g.board[2][1] = 'A'
g.board[2][2] = 'B'
g.board[2][3] = 'C'
g.board[2][4] = 'D'
g.board[3][1] = 'a'
g.board[3][3] = 'b'
g.board[4][3] = 'c'
g.board[6][2] = 'd'
g.board[4][4] = 'e'

g.stones['b'] = [(2,1),(2,2),(2,3),(2,4)]
g.stones['r'] = [(3,1),(3,3),(4,3),(6,2),(4,4)]

# g.board[2][1] = 'A'
# g.board[2][2] = 'B'
# g.board[2][3] = 'C'
# g.board[2][4] = 'D'
# g.board[3][1] = 'a'
# g.board[3][3] = 'b'
# g.board[4][3] = 'c'
# g.board[2][0] = 'd'
# g.board[4][4] = 'e'

# g.stones['b'] = [(2, 1), (2, 2), (2, 3), (2, 4)]
# g.stones['r'] = [(3, 1), (3, 3), (4, 3), (2, 0), (4, 4)]


g.print_board()

g.reflex('b')

print()
g.print_board()