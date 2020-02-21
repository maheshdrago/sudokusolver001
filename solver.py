

def accept(num,row,col,board):

    for c in range(0,9):
        if board[row][c]==num:
            return False

    for r in range(0,9):
        if board[r][col]==num:
            return False

    if row<=2  and col<=2:
        x,y=0,0

    elif row<=2 and (col<=5 and col>=3):
        x,y=0,3

    elif row<=2 and (col<=8 and col>=6):
        x,y=0,6

    elif (row>2 and row<=5) and col<=2:
        x,y=3,0

    elif (row>2 and row<=5) and (col<=5 and col>=3):
        x,y=3,3

    elif (row>2 and row<=5) and (col<=8 and col>=6):
        x,y=3,6

    elif row>5  and col<=2 :
        x,y=6,0

    elif row>5 and (col>2 and col<=5):
        x,y=6,3

    elif row>5 and (col>5 and col<=8):
        x,y=6,6


    for i in range(0,3):
        for j in range(0,3):
            if board[i+x][j+y]==num:

                return False
    return True

def solve(board):

    if not find_empty(board):
        return board

    else:

        row,col=find_empty(board)
        for num in range(1,10):
            if accept(num,row,col,board):
                board[row][col]=num

                if solve(board):
                    return True
                board[row][col]=0
        return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
