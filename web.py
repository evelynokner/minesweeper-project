from flask import Flask, redirect, url_for
from pathlib import Path
from string import Template
# import necessary modules
import game, const
import minesweeper
# import floodfill

# generating html
def generate_html(count_matrix, game_board_matrix):
    joined_matrix = join_matrix(count_matrix, game_board_matrix)
    # read text from html file & store as string
    html_template = Path('table.html').read_text()
    template = Template(html_template)
    # make 2 different matrices
    html_count_table = generate_html_table(count_matrix)
    html_joined_table = generate_html_table(joined_matrix)
    return template.substitute(count_table=html_count_table,
                               game_board_table=html_joined_table)


def generate_html_table(matrix):
    content = ""
    num_rows = len(matrix)
    html_row = Path('row.html').read_text()
    template = Template(html_row)
    for i in range(num_rows):
        content = content + template.substitute(row=draw_row(matrix[i], i))
    return content


# combine matrices
def join_matrix(count_matrix, game_board_matrix):
    # create empty array for the joined matrix
    joined_table = []
    num_rows = len(game_board_matrix)
    num_cols = len(game_board_matrix[0])

    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            if game_board_matrix[i][j] == 1:
                row.append(count_matrix[i][j])
            else:
                row.append(-2)
        joined_table.append(row)
    return joined_table


def draw_row(row, row_number):
    content = ""
    num_cols = len(row)
    for col_number in range(num_cols):
        cell = row[col_number]
        content = content + draw_cell(cell, row_number, col_number)
    return content


def draw_cell(cell, row, col):
    html_cell = Path('cell.html').read_text()
    template = Template(html_cell)
    # change color of cell number based on the number
    match cell:
        case -2:  # black square Unicode
            cell = "&#x25A0"
            cell_color = "black"
        case -1:  # mine Unicode or img
            cell = "&#128163"
            cell_color = "black"
        case 0:  # blank
            cell_color = "white"
        case 1:
            cell_color = "blue"
        case 2:
            cell_color = "green"
        case 3:
            cell_color = "red"
        case 4:
            cell_color = "mediumpurple"
        case 5:
            cell_color = "darkorange"
        case 6:
            cell_color = "darkcyan"
        case 7:
            cell_color = "lime"
        case 8:
            cell_color = "mediumvioletred"
        case _:
            cell_color = "black"

    # cell_color and cell_value are placeholder elements in cell.html
    # row and col indices are used for getting url for move coordinates
    # replaces html placeholders with new values
    return template.substitute(cell_color=cell_color, cell_value=cell, row=row, col=col)


# create new html page displaying matrix
def create_page(count_matrix, board_matrix):
    # testing
    # print(join_matrix(count_matrix, game_board_matrix))
    html = generate_html(count_matrix, board_matrix)
    with open("page.html", "w") as file:  # w is for writing in new file
        file.write(html)


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
    return generate_html(count_matrix, gameboard)

# todo: create display_move method

# web module needs access to gameboard & count_matrix
# call move(row, col)
# return result
# either won, lost or continue
# each redirects to a different page
@app.route("/move/<int:row>/<int:col>")
def move(row, col):
    #global gameboard, count_matrix
    result = game.move(row, col)

    match result:
        case const.WON:
            return redirect(url_for("win-page"))
        case const.LOST:
            return redirect(url_for("lost-page"))
        case _:
            return generate_html(game.count_matrix, game.gameboard)

    # result = game.move(row, col)
    # or use switch
    # if result == WON:
        # return redirect(won page)
    # else if result == LOST:
        # return redirect(lost page)
    # else return generate_html(game.count_matrix, game.gameboard)
    #floodfill.dfs(gameboard, count_matrix, row, col)
    # generate html based on result (make methods for win & loss page)
    return generate_html(game.count_matrix, game.gameboard)

# redirect testing
# if on page /gameover, redirect to gameboard method's page
@app.route("/gameovertest")
def redirect_test():
    # put name of function we want to redirect to in url_for()
    return redirect(url_for("gameboard"))

# redirect to different page when game ends
'''
Conditions for game over:
    1) user clicks on a mine (value of -1 on count_matrix)
    2) every cell on gameboard has been opened (value of 1 on gameboard) EXCEPT mines
    
    - create method for page we want to redirect to when gameover = true
    - set conditions for redirecting to gameover page
'''
@app.route("/gameover")
def gameover():
    gameover = False
    return gameover
    #return redirect(url_for("gameover"))

if __name__ == "__main__":
    app.run()