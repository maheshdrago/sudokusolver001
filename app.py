from flask import Flask,render_template,url_for,request
import solver


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=['POST'])
def get_values():
    if request.method=="POST":
        board = [ [int(request.form[str(i)]) for i in range(1,10)],
                  [int(request.form[str(i)]) for i in range(10,19)],
                  [int(request.form[str(i)]) for i in range(19,28)],
                  [int(request.form[str(i)]) for i in range(28,37)],
                  [int(request.form[str(i)]) for i in range(37,46)],
                  [int(request.form[str(i)]) for i in range(46,55)],
                  [int(request.form[str(i)]) for i in range(55,64)],
                  [int(request.form[str(i)]) for i in range(64,73)],
                  [int(request.form[str(i)]) for i in range(73,82)] ]

        '''board = [ [3,0,6,5,0,8,4,0,0],
                  [5,2,0,0,0,0,0,0,0],
                  [0,8,7,0,0,0,0,3,1],
                  [0,0,3,0,1,0,0,8,0],
                  [9,0,0,8,6,3,0,0,5],
                  [0,5,0,0,9,0,6,0,0],
                  [1,3,0,0,0,0,2,5,0],
                  [0,0,0,0,0,0,0,7,4],
                  [0,0,5,2,0,6,3,0,0] ]'''



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

        solve(board)
        return render_template('show.html',board=board)















if __name__ == '__main__':
    app.run(debug=True)
