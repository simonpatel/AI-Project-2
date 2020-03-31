import sys
import re

grid = list()
gridsize = 3
win = 3
win_val = 2000000000
max_depth = 6

def copy(oldgrid):
    newgrid = list()
    for i in range(gridsize):
        temp = list()
        for j in range(gridsize):
            temp.append(oldgrid[i][j])
        newgrid.append(temp)
    return newgrid

def val_horizontal(newgrid, player):
    maxLen = 0
    for row in range(gridsize):
        for index in range(gridsize - win+1):
            win_x = True
            thisLen = 0
            for w in range(win):
                win_x = win_x and newgrid[row][index+w] == player
                if win_x: 
                    thisLen += 1
            if thisLen > maxLen:
                maxLen = thisLen
            if win_x:
                return win_val
    return maxLen

def val_vertical(newgrid, player):
    maxLen = 0
    for col in range(gridsize):
        for index in range(gridsize - win+1):
            win_x = True
            thisLen = 0
            for w in range(win):
                win_x = win_x and newgrid[index+w][col] == player
                if win_x: 
                    thisLen += 1
            if thisLen > maxLen:
                maxLen = thisLen
            if win_x:
                return win_val
    return maxLen

def val_diag_1(newgrid, player):
    maxLen = 0
    for dia in range(win-1, gridsize):
        i = 0
        temp = list()
        while dia >= 0 and i < gridsize:
            temp.append(newgrid[dia][i])
            dia -= 1
            i += 1
        l = len(temp)
        for index in range(l - win + 1):
            win_x = True
            thisLen = 0
            for w in range(win):
                win_x = win_x and temp[index + w] == player
                if win_x: 
                    thisLen += 1
            if thisLen > maxLen:
                maxLen = thisLen
            if win_x:
                return win_val

    for dia in range(1, gridsize - win + 1):
        i = gridsize-1
        temp = list()
        while i >= 0 and dia < gridsize:
            temp.append(newgrid[dia][i])
            dia += 1
            i -= 1
        l = len(temp)
        for index in range(l - win + 1):
            win_x = True
            thisLen = 0
            for w in range(win):
                win_x = win_x and temp[index + w] == player
                if win_x: 
                    thisLen += 1
            if thisLen > maxLen:
                maxLen = thisLen
            if win_x:
                return win_val
    return maxLen

def val_diag_2(newgrid, player):
    maxLen = 0
    for dia in range(gridsize - win + 1):
        i = 0
        temp = list()
        while dia < gridsize and i  < gridsize:
            temp.append(newgrid[dia][i])
            i += 1
            dia += 1
        l = len(temp)
        for index in range(l - win + 1):
            win_x = True
            thisLen = 0
            for w in range(win):
                win_x = win_x and temp[index + w] == player
                if win_x: 
                    thisLen += 1
            if thisLen > maxLen:
                maxLen = thisLen
            if win_x:
                return win_val

    for i in range(1, gridsize-win+1):
        dia = 0
        temp = list()
        while dia < gridsize and i  < gridsize:
            temp.append(newgrid[dia][i])
            i += 1
            dia += 1
        l = len(temp)
        for index in range(l - win + 1):
            win_x = True
            thisLen = 0
            for w in range(win):
                win_x = win_x and temp[index + w] == player
                if win_x: 
                    thisLen += 1
            if thisLen > maxLen:
                maxLen = thisLen
            if win_x:
                return win_val
    return maxLen



def value(newgrid, player):
    maxLen = 0
    vv = val_vertical(newgrid, player)
    if vv > maxLen:
        maxLen = vv

    vh = val_vertical(newgrid, player)
    if vh > maxLen:
        maxLen = vh

    vd1 = val_vertical(newgrid, player)
    if vd1 > maxLen:
        maxLen = vd1

    vd2 = val_vertical(newgrid, player)
    if vd2 > maxLen:
        maxLen = vd2

    return maxLen

        
    
#minmax search function should be generic.
#restrict depth by time taken.  Should be a defined constant

def min(oldgrid, depth):
    val = win_val
    bestMove = (-1, -1)
    if depth > 0:
        for i in range(gridsize):
            for j in range(gridsize):
                newGrid = copy(oldgrid)
                if newGrid[i][j] == '-':
                    newGrid[i][j] = 'X'
                    temp = max(newGrid, depth - 1)[0]
                    temp = -temp
                    if temp < val:
                        val = temp
                        bestMove = (i, j)
        return val, bestMove
    else:
        return value(oldgrid, 'X'), bestMove

def max(oldgrid, depth):
    val = win_val
    bestMove = (-1, -1)
    if depth > 0:
        for i in range(gridsize):
            for j in range(gridsize):
                newGrid = copy(oldgrid)
                if newGrid[i][j] == '-':
                    newGrid[i][j] = 'O'
                    temp = min(newGrid, depth - 1)[0]
                    if temp < val:
                        val = temp
                        bestMove = (i, j)
        return val, bestMove
    else:
        return value(oldgrid, 'O'), bestMove


def search():
    temp = max(grid, max_depth)
    return temp[1]

def printGrid(): #for debugging purposes only
    for i in range(gridsize):
        print(grid[i])



#build the grid.  This is all for testing.
for i in range(gridsize):
    temp = list()
    for j in range(gridsize):
        temp.append('-')
    grid.append(temp)


#main loop:
while True:
    move = search()
    grid[move[0]][move[1]] = 'X'
    printGrid()
    player_move = input('Enter your move (x y)...')
    print(player_move)
    pm = player_move.split(' ')
    if(grid[int(pm[0])][int(pm[1])] == '-'):
        grid[int(pm[0])][int(pm[1])] = 'O'
#print(value(grid, 'x'))
#printGrid()
