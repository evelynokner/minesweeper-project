from flask import Flask, redirect, url_for
import minesweeper
import floodfill

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Hello World!</h1> <a href="/gameboard">Gameboard</a>'

@app.route("/gameboard")
def gameboard():
    return "<h2>minesweeper gameboard</h2>"

@app.route("/minesweeper")
def displayBoard():
    # hardcoded boards for now
    count_matrix = [[0, 0, 0, 0, 0],
                    [0, 1, 2, 2, 1],
                    [0, 1, -1, -1, 2],
                    [0, 1, 2, 3, -1],
                    [0, 0, 0, 1, 1]]
    gameboard = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    #minesweeper.generate_board()
    return minesweeper.generate_html(count_matrix, gameboard)

# hardcoded boards for now
count_matrix = [[0, 0, 0, 0, 0],
                    [1, 2, 2, 2, 1],
                    [-1, 2, -1, -1, 2],
                    [1, 2, 2, 3, -1],
                    [0, 0, 0, 1, 1]]
gameboard = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

@app.route("/move/<int:row>/<int:col>")
def move(row, col):
    global gameboard, count_matrix

    floodfill.dfs(gameboard, count_matrix, row, col)
    return minesweeper.generate_html(count_matrix, gameboard)

# redirect testing
# if on page /gameover, redirect to gameboard method's page
@app.route("/gameover")
def gameover():
    # put name of function we want to redirect to in url_for()
    return redirect(url_for("gameboard"))

if __name__ == "__main__":
    app.run()
