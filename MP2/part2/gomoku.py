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
        #stones go (y,x)
        self.stones = {}
        self.stones['r'] = []
        self.stones['b'] = []

    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end=' ')
            print()

    def reflex(self, color):
        opponent = 'b'
        if(color == 'b'):
            opponent = 'r'
        #Rule 1. Check for chains of length 4 in own color
        for point in self.stones[color]:
            for d in directions:
                length, start, end, direction = self.stone_chain(point, d, color)
                # print(point, length, d)
                x_start, y_start, x_end, y_end = start[0], start[1], end[0], end[1]
                # print('Info', x_start, y_start, x_end, y_end, point)
                if(length == 4):
                    if(direction == 'L'):
                        # print('End, x_end', end, x_end)
                        # check left side first then right
                        value = self.board[y_start][x_start - 1]
                        value2 = self.board[y_end][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start, x_start - 1))
                            self.board[y_start][x_start - 1] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end, x_end + 1))
                            self.board[y_end][x_end + 1] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        value2 = self.board[y_end -1 ][x_end]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'DL'):
                        # check left down side first then up right
                        value = self.board[y_start + 1][x_start -1]
                        value2 = self.board[y_end - 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start + 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'UL'):
                        # check left up side first then down right
                        value = self.board[y_start - 1][x_start -1]
                        value2 = self.board[y_end + 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start - 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end + 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            return

        #Rule 2. Check opponent for chains of 4 
        for point in self.stones[opponent]:
            for d in directions:
                length, start, end, direction = self.stone_chain(point, d, opponent)
                print(point, length, d, opponent)
                x_start, y_start, x_end, y_end = start[0], start[1], end[0], end[1]
                if(length == 4):
                    if(direction == 'L'):
                        # print("printing ...")
                        # check left side first then right
                        value = self.board[y_start][x_start - 1]
                        value2 = self.board[y_end][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start, x_start - 1))
                            self.board[y_start][x_start - 1] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end, x_end + 1))
                            self.board[y_end][x_end + 1] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        value2 = self.board[y_end -1 ][x_end]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'DL'):
                        # check left down side first then up right
                        value = self.board[y_start + 1][x_start -1]
                        value2 = self.board[y_end - 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start + 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            return
                    elif(direction == 'UL'):
                        # check left up side first then down right
                        value = self.board[y_start - 1][x_start -1]
                        value2 = self.board[y_end + 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start - 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end + 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            return
        #3. Check whether the opponent has an unbroken chain formed by 3 stones and has empty spaces on BOTH ends of the chain
        for point in self.stones[opponent]:
            for d in directions:
                length, start, end, direction = self.stone_chain(point, d, opponent)
                print(point, length, d, opponent)
                x_start, y_start, x_end, y_end = start[0], start[1], end[0], end[1]
                if(length == 3):
                    if(direction == 'L'):
                        # print("printing ...")
                        # check left side first then right
                        value = self.board[y_start][x_start - 1]
                        value2 = self.board[y_end][x_end + 1]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start, x_start - 1))
                            self.board[y_start][x_start - 1] = alphabet[color][len(self.stones[color])-1]
                            return

                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        value2 = self.board[y_end -1 ][x_end]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return
                        
                    elif(direction == 'DL'):
                        # check left down side first then up right
                        value = self.board[y_start + 1][x_start -1]
                        value2 = self.board[y_end - 1 ][x_end + 1]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start + 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return

                    elif(direction == 'UL'):
                        # check left up side first then down right
                        value = self.board[y_start - 1][x_start -1]
                        value2 = self.board[y_end + 1 ][x_end + 1]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start - 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
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
            value = self.board[y+1][x-1]
            while(value != '.'):
                # dealing with red
                if(color == 'r' and value.isupper()):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break
                x = x - 1
                y = y + 1

                value = self.board[y+1][x-1]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            # print('start, end', start, end)
            value = self.board[y-1][x+1]
            while(value != '.'):
                # print(x)
                # dealing with red

                if(color == 'r' and value.isupper() ):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break
                    
                x = x + 1
                y = y - 1
                count += 1
                end = (x, y)
                value = self.board[y-1][x + 1]
            return count, start, end, direction
    
        # left
        elif(direction == 'L'):
            value = self.board[y][x-1]
            while(value != '.'):
                # dealing with red
                if(color == 'r' and value.isupper()):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break
                x = x - 1

                value = self.board[y][x-1]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            # print('start, end', start, end)
            value = self.board[y][x+1]
            while(value != '.'):
                # print(x)
                # dealing with red

                if(color == 'r' and value.isupper() ):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break

                x = x + 1
                count += 1
                # print("count: ", count,"value", value)
                end = (x, y)
                value = self.board[y][x + 1]
            # return something, (length, start, end, direction?)
            # print('start, end after', start, end)
            return count, start, end, direction

        # up-left
        elif(direction == 'UL'):
            value = self.board[y-1][x-1]
            while(value != '.'):
                # dealing with red
                if(color == 'r' and value.isupper()):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break
                x = x - 1
                y = y - 1

                value = self.board[y-1][x-1]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            # print('start, end', start, end)
            value = self.board[y+1][x+1]
            while(value != '.'):
                print(x)
                # dealing with red

                if(color == 'r' and value.isupper() ):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break
                    
                x = x + 1
                y = y + 1
                count += 1
                end = (x, y)
                value = self.board[y+1][x + 1]
            return count, start, end, direction
    

        # up
        else:
            value = self.board[y-1][x]
            while(value != '.'):
                # dealing with red
                if(color == 'r' and value.isupper()):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break
                y = y - 1

                value = self.board[y-1][x]
            # At this point its at the farthest back in the chain
            start = (x, y)
            end = (x, y)
            # print('start, end', start, end)
            value = self.board[y+1][x]
            while(value != '.'):
                # dealing with red

                if(color == 'r' and value.isupper() ):
                    break

                # dealing with blue
                elif(color == 'b'and not value.isupper()):
                    break

                y = y + 1
                count += 1
                start = (x, y)
                value = self.board[y+1][x]

            return count, start, end, direction



g = Gomoku()

# test left
# g.board[2][1] = 'A'
# g.board[2][2] = 'B'
# g.board[2][3] = 'C'
# g.board[2][4] = 'D'
# g.board[3][1] = 'a'
# g.board[3][3] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[4][4] = 'e'

# (y,x)
# g.stones['b'] = [(2,1),(2,2),(2,3),(2,4)]
# g.stones['r'] = [(3,1),(3,3),(4,3),(6,2),(4,4)]

# g.board[2][1] = 'A'
# g.board[2][2] = 'B'
# g.board[2][3] = 'C'
# g.board[2][4] = 'D'
# g.board[3][1] = 'a'
# g.board[3][3] = 'b'
# g.board[4][3] = 'c'
# g.board[2][0] = 'd'
# g.board[2][5] = 'e'

# g.stones['b'] = [(2, 1), (2, 2), (2, 3), (2, 4)]
# g.stones['r'] = [(3, 1), (3, 3), (4, 3), (2, 0), (2, 5)]

# test down left
# g.board[5][1] = 'A'
# g.board[4][2] = 'B'
# g.board[3][3] = 'C'
# g.board[2][4] = 'D'
# g.board[3][1] = 'a'
# g.board[3][4] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[4][4] = 'e'

# g.stones['b'] = [(5,1),(4,2),(3,3),(2,4)]
# g.stones['r'] = [(3,1),(3,4),(4,3),(6,2),(4,4)]

# g.board[5][1] = 'A'
# g.board[4][2] = 'B'
# g.board[3][3] = 'C'
# g.board[2][4] = 'D'
# g.board[6][0] = 'a'
# g.board[3][4] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[4][4] = 'e'

# g.stones['b'] = [(5,1),(4,2),(3,3),(2,4)]
# g.stones['r'] = [(6,0),(3,4),(4,3),(6,2),(4,4)]

#test down/up

# g.board[5][1] = 'A'
# g.board[4][1] = 'B'
# g.board[3][1] = 'C'
# g.board[2][1] = 'D'
# g.board[6][0] = 'a'
# g.board[3][4] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[4][4] = 'e'

# g.stones['b'] = [(5,1),(4,1),(3,1),(2,1)]
# g.stones['r'] = [(6,0),(3,4),(4,3),(6,2),(4,4)]

# g.board[5][1] = 'A'
# g.board[4][1] = 'B'
# g.board[3][1] = 'C'
# g.board[2][1] = 'D'
# g.board[6][1] = 'a'
# g.board[3][4] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[1][1] = 'e'

# g.stones['b'] = [(5,1),(4,1),(3,1),(2,1)]
# g.stones['r'] = [(6,1),(3,4),(4,3),(6,2),(1,1)]

#test up- left

# g.board[1][1] = 'A'
# g.board[2][2] = 'B'
# g.board[3][3] = 'C'
# g.board[4][4] = 'D'
# g.board[3][1] = 'a'
# g.board[3][4] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[5][4] = 'e'

# g.stones['b'] = [(1,1),(2,2),(3,3),(4,4)]
# g.stones['r'] = [(3,1),(3,4),(4,3),(6,2),(5,4)]

# g.board[1][1] = 'A'
# g.board[2][2] = 'B'
# g.board[3][3] = 'C'
# g.board[4][4] = 'D'
# g.board[0][0] = 'a'
# g.board[3][4] = 'b'
# g.board[4][3] = 'c'
# g.board[6][2] = 'd'
# g.board[5][5] = 'e'

# g.stones['b'] = [(1,1),(2,2),(3,3),(4,4)]
# g.stones['r'] = [(0,0),(3,4),(4,3),(6,2),(5,5)]

#test for #2

# g.board[3][0] = 'A'
# g.board[2][0] = 'B'
# g.board[2][1] = 'C'

# g.board[3][1] = 'a'
# g.board[3][2] = 'b'
# g.board[3][3] = 'c'
# g.board[3][4] = 'd'

# g.stones['b'] = [(3,0),(2,0),(2,1)]
# g.stones['r'] = [(3,1),(3,2),(3,3),(3,4)]


#test for #3

g.board[1][1] = 'A'
g.board[3][2] = 'B'

g.board[2][2] = 'a'
g.board[2][3] = 'b'
g.board[2][4] = 'c'

g.stones['b'] = [(1,1),(3,2)]
g.stones['r'] = [(2,3),(2,2),(2,4)]





g.print_board()

g.reflex('b')

print()
g.print_board()
