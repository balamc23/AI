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
        self.gameover = 0

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
                            self.gameover = 1
                            return (y_start,x_start - 1), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end, x_end + 1))
                            self.board[y_end][x_end + 1] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_end,x_end + 1), direction
                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        value2 = self.board[y_end -1 ][x_end]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_start +1,x_start), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_end -1,x_end), direction
                    elif(direction == 'DL'):
                        # check left down side first then up right
                        value = self.board[y_start + 1][x_start -1]
                        value2 = self.board[y_end - 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start + 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_start +1,x_start -1 ), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_end -1,x_end +1), direction
                    elif(direction == 'UL'):
                        # check left up side first then down right
                        value = self.board[y_start - 1][x_start -1]
                        value2 = self.board[y_end + 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start - 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_start  -1,x_start - 1 ), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end + 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            self.gameover = 1
                            return (y_end +1,x_end +1), direction

        #Rule 2. Check opponent for chains of 4 
        for point in self.stones[opponent]:
            for d in directions:
                length, start, end, direction = self.stone_chain(point, d, opponent)
                # print(point, length, d, opponent)
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
                            return (y_start,x_start - 1), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end, x_end + 1))
                            self.board[y_end][x_end + 1] = alphabet[color][len(self.stones[color])-1]
                            return (y_end,x_end + 1), direction
                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        value2 = self.board[y_end -1 ][x_end]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return (y_start +1,x_start), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end] = alphabet[color][len(self.stones[color])-1]
                            return (y_end -1,x_end), direction
                    elif(direction == 'DL'):
                        # check left down side first then up right
                        value = self.board[y_start + 1][x_start -1]
                        value2 = self.board[y_end - 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start + 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return (y_start +1,x_start -1 ), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end - 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            return (y_end -1,x_end +1), direction
                    elif(direction == 'UL'):
                        # check left up side first then down right
                        value = self.board[y_start - 1][x_start -1]
                        value2 = self.board[y_end + 1 ][x_end + 1]
                        if(value == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start - 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return (y_start  -1,x_start - 1 ), direction
                        elif(value2 == '.'):
                            self.stones[color].append((y_end - 1, x_end))
                            self.board[y_end + 1][x_end +1] = alphabet[color][len(self.stones[color])-1]
                            return (y_end +1,x_end +1), direction
        #Rule 3. Check whether the opponent has an unbroken chain formed by 3 stones and has empty spaces on BOTH ends of the chain
        for point in self.stones[opponent]:
            for d in directions:
                length, start, end, direction = self.stone_chain(point, d, opponent)
                # print(point, length, d, opponent)
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
                            return (y_start,x_start - 1), direction

                    elif(direction == 'U'):
                        # check down side first then up
                        value = self.board[y_start + 1][x_start]
                        value2 = self.board[y_end -1 ][x_end]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start + 1, x_start))
                            self.board[y_start + 1][x_start] = alphabet[color][len(self.stones[color])-1]
                            return (y_start +1,x_start), direction
                        
                    elif(direction == 'DL'):
                        # check left down side first then up right
                        value = self.board[y_start + 1][x_start -1]
                        value2 = self.board[y_end - 1 ][x_end + 1]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start + 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return (y_start +1,x_start -1 ), direction

                    elif(direction == 'UL'):
                        # check left up side first then down right
                        value = self.board[y_start - 1][x_start -1]
                        value2 = self.board[y_end + 1 ][x_end + 1]
                        if(value == '.' and value2 == '.'):
                            self.stones[color].append((y_start + 1, x_start -1 ))
                            self.board[y_start - 1][x_start-1] = alphabet[color][len(self.stones[color])-1]
                            return (y_start  -1,x_start - 1 ), direction
        #Rule 4. 
        x,y = 0,0
        winning_blocks = []
        for row in self.board:
            for cell in row:
                if(cell == '.' or (color == 'r' and  not cell.isupper()) or (color == 'b' and cell.isupper())):
                    for d in directions:
                        stone_count = 0
                        x_temp,y_temp = x,y
                        for count in range(1,6):
                            value = self.board[y_temp][x_temp]
                            #If theres a stone in the path check if its yours or nah
                            if(value != '.'):
                                if(color == 'r'):
                                    if(not value.isupper()):
                                        stone_count += 1
                                    else:
                                        count -= 1
                                        break
                                elif(color == 'b'):
                                    if(value.isupper()):
                                        stone_count += 1
                                    else:
                                        count -= 1
                                        break

                            if(d =='L'):
                                #go right
                                if(x_temp +1 > 6):
                                    break
                                x_temp += 1
                            elif(d == 'DL'):
                                #down-left
                                if((x_temp -1 < 0) or (y_temp +1 > 6)):
                                    break
                                x_temp -= 1
                                y_temp += 1
                            elif(d == 'U'):
                                #go down
                                if(y_temp +1 > 6):
                                    break
                                y_temp +=1
                            elif(d =='UL'):
                                # go down-right
                                if((x_temp +1 > 6) or (y_temp +1>6)):
                                    break
                                x_temp +=1
                                y_temp +=1

                        if(count == 5):
                            winning_blocks.append( (stone_count, (x,y), d))
                # print(cell, self.board[y][x])
                x+=1
            x=0
            y+=1 

        winning_blocks.sort(reverse = True)
        max_stones = winning_blocks[0][0]
        best_winners = []
        for item in winning_blocks:
            if (item[0] < max_stones):
                break
            dist_to_x = 0+item[1][0]
            best_winners.append( ( dist_to_x , (item[1][0],item[1][1]), item[2]))
        best_winners.sort()
        closest_x = best_winners[0][0]
        closest_y = 7
        start_point = (best_winners[0][1],best_winners[0][2] )
        for item in best_winners:
            if(item[0] > closest_x):
                break
            if(6-item[1][1] < closest_y):
                closest_y = 6-item[1][1]
                start_point = (item[1],item[2])

        #time to add the actual point
        place_point = start_point[0]
        X,Y = start_point[0][0], start_point[0][1]
        v, direct  = self.board[start_point[0][1]][start_point[0][0]], start_point[1]
        while(v != '.'):
            # print(X,Y, v)
            if(direct =='L'):
                #go right
                X = X + 1
            elif(direct == 'DL'):
                #down-left
                X = X -1
                Y = Y +1
            elif(direct == 'U'):
                #go down
                Y +=1
            elif(direct =='UL'):
                # go down-right
                X +=1
                Y +=1

            place_point = (X, Y)
            v = self.board[place_point[1]][place_point[0]]
            
        self.stones[color].append((place_point[1], place_point[0]))
        self.board[place_point[1]][place_point[0]] = alphabet[color][len(self.stones[color])-1]
        return (place_point[1],place_point[0]), direct




    def stone_chain(self, point, direction, color):
        y, x = point[0], point[1]
        count = 1
        # down-left
        if(direction == 'DL'):
            if (y+1 < 7 and x-1 > -1):
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
                    if( x -1 < 0 or y +1 > 6):
                        break

                    value = self.board[y+1][x-1]
                # At this point its at the farthest back in the chain
                start = (x, y)
                end = (x, y)
                # print('start, end', start, end)
                if (y-1 >-1 and x+1 < 7):
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
                        if( x+1 > 7 or y-1 < 0):
                            break
                        value = self.board[y-1][x + 1]
                return count, start, end, direction
            else:
                return 0, point, point, direction
    
        # left
        elif(direction == 'L'):
            if (x-1 > -1):
                value = self.board[y][x-1]
                while(value != '.'):
                    # dealing with red
                    if(color == 'r' and value.isupper()):
                        break

                    # dealing with blue
                    elif(color == 'b'and not value.isupper()):
                        break
                    x = x - 1
                    if( x -1 < 0):
                        break
                    value = self.board[y][x-1]
                # At this point its at the farthest back in the chain
                start = (x, y)
                end = (x, y)
                # print('start, end', start, end)
                if(x+1 < 7):
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

                        end = (x, y)
                        if(x +1 > 6):
                            break
                        value = self.board[y][x + 1]
                # return something, (length, start, end, direction?)
                # print('start, end after', start, end)
                return count, start, end, direction
            else:
                return 0, point, point, direction

        # up-left
        elif(direction == 'UL'):
            if (x-1 > -1 and y-1 > -1):
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
                    if( x -1 < 0 or y -1 < 0):
                        break
                    value = self.board[y-1][x-1]
                # At this point its at the farthest back in the chain
                start = (x, y)
                end = (x, y)
                # print('start, end', start, end)
                if( y+1 < 7 and x+1 < 7):
                    value = self.board[y+1][x+1]
                    while(value != '.'):
                        # prnt(x)
                        # dealing with red

                        if(color == 'r' and value.isupper() ):
                            break

                        # dealing with blue
                        elif(color == 'b'and not value.isupper()):
                            break
                            
                        x = x + 1
                        y = y + 1
                        # print((x,y), count)
                        
                        count += 1
                        end = (x, y)
                        if(x +1 > 6 or y +1 > 6 ):
                            break
                        value = self.board[y+1][x + 1]
                # print("start: ", start, " End: ", end)
                return count, start, end, direction
            else:
                return 0, point, point, direction
    

        # up
        elif(direction == 'U'):
            if ( y-1 > -1):
                value = self.board[y-1][x]
                while(value != '.'):
                    # dealing with red
                    if(color == 'r' and value.isupper()):
                        break

                    # dealing with blue
                    elif(color == 'b'and not value.isupper()):
                        break
                    y = y - 1
                    if( y -1 < 0):
                        break
                    value = self.board[y-1][x]
                # At this point its at the farthest back in the chain
                start = (x, y)
                end = (x, y)
                # print('start, end', start, end)
                if( y+1 < 7):
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
                        if(y +1 > 6):
                            break
                        value = self.board[y+1][x]

                return count, start, end, direction
            else:
                return 0, point, point, direction



        else:
            return 0, point, point, direction



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

# g.board[1][1] = 'A'
# g.board[3][2] = 'B'

# g.board[2][2] = 'a'
# g.board[2][3] = 'b'
# g.board[2][4] = 'c'

# g.stones['b'] = [(1,1),(3,2)]
# g.stones['r'] = [(2,3),(2,2),(2,4)]

#test for #4

# g.board[0][1] = 'A'
# g.board[2][2] = 'B'
# g.board[2][4] = 'C'

# g.board[4][1] = 'a'
# g.board[5][1] = 'b'
# g.board[5][2] = 'c'

# g.stones['b'] = [(0,1),(2,2),(2,4)]
# g.stones['r'] = [(4,1),(5,1),(5,2)]

# g.board[1][5] = 'A'


# g.board[5][1] = 'a'

# g.stones['b'] = [(1,5)]
# g.stones['r'] = [(5,1)]






g.print_board()

turn = 'r'
while(not g.gameover):
    point, d = g.reflex(turn)
    print()
    g.print_board()
    for D in directions:
        check, trash1, trash2, trash3 = g.stone_chain(point, D, turn)
        print(check, D)
        if(check == 5):
            g.gameover =1
    if(turn == 'r'):
        turn = 'b'
    elif(turn == 'b'):
        turn = 'r'
    if(len(g.stones['r'])+ len(g.stones['b']) == 49):
        g.gameover = 1

# g.reflex('r')
# g.reflex('b')
# g.reflex('r')
# g.reflex('b')
# g.reflex('r')
# g.reflex('b')
# g.reflex('r')
# g.reflex('b')



print()
g.print_board()
print("Game Over! ")
