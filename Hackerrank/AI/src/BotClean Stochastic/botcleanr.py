#!/bin/python3

def nextMove(posr, posc, board):
    di = 0
    dj = 0
    found = False
    for xj in board:
        for xi in xj:
            if xi == 'd':
                found = True
                break
            else:
                di += 1
        if found is True:
            break
        dj += 1
        di = 0
    diffr = dj - posr
    diffc = di - posc

    # print("r : ", diffr)
    # print("c : ", diffc)
    # if +ve that means i need to travel right or down or both
    # if -ve that means I need to travel left or up or both
    if diffr == 0:
        resr = None
    elif diffr < 0:
        resr = "UP"
    else:
        resr = "DOWN"

    if diffc == 0:
        resc = None
    elif diffc < 0:
        resc = "LEFT"
    else:
        resc = "RIGHT"

    if resr is not None:
        ret = resr
    elif resc is not None:
        ret = resc
    else:
        ret = "CLEAN"
    print(ret)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
