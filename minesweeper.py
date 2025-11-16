# constants for checking if a cell is open or closed
global openedCell
openedCell = 1
global closedCell
closedCell = 0

def plant_mines(board, num_of_mines):
    import random

    rows = len(board)
    cols = len(board[0])
    
    #while loop to check for duplicate coordinates
        # n = 0, while n <= num_of_mines: gen rand nums
        # if board[r][c] = -1, do nothing
        # else: board[r][c] = -1, n=n+1
    n = 0
    while n < num_of_mines:
        # run random num generating num_of_mines times
        random_row = random.randrange(0, rows)
        random_col = random.randrange(0, cols)
        print(random_row, random_col)
        if board[random_row][random_col] == -1:
            pass
        else:
            board[random_row][random_col] = -1
            n = n + 1
    #return (random_row, random_col)

def count_mines(board):
    num_rows = len(board)
    num_cols = len(board[0])
    # iterate through board
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == -1:
                board = increase_mine_counts(board, i, j)
    return board

def increase_mine_counts(board, x, y):
    for (x, y) in neighbors(board, x, y):
        if board[x][y] != -1:
            board[x][y] = board[x][y] + 1
    return board

def neighbors(board, x, y):
    #dimensions
    num_rows = len(board)
    num_cols = len(board[0])
    point = (x, y)
    
    # CORNERS
    if x > num_rows-1 or x < 0 or y > num_cols-1 or y < 0:
        print("out of bounds")
        return False
    # top left corner
    if x == 0 and y == 0:
        return [(0, 1), (1, 0), (1, 1)]
    # top right corner
    if x == 0 and y == num_cols - 1:
        return [(0, num_cols - 2), (1, num_cols - 2), (1, num_cols - 1)]
    # bottom left corner
    if x == num_rows - 1 and y == 0:
        return [(num_rows - 2, 0), (num_rows - 1, 1), (num_rows - 2, 1)]
    # bottom right corner
    if x == num_rows - 1 and y == num_cols - 1:
        return [(num_rows - 1, num_cols - 2), (num_rows - 2, num_cols - 2), (num_rows - 2, num_cols - 1)]
    
    # EDGES
    # top
    if x == 0 and y == y:
        return [(0, y-1), (0, y+1), (1, y-1), (1, y), (1, y+1)]
    # bottom
    if x == num_rows - 1 and y == y:
        return [(num_rows-1, y-1), (num_rows-1, y+1), (num_rows-2, y-1), (num_rows-2, y), (num_rows-2, y+1)]
    # left
    if x == x and y == 0:
        return [(x+1, 0), (x-1, 0), (x+1, 1), (x, 1), (x-1, 1)]
    # right 
    if x == x and y == num_cols - 1:
        return [(x+1, num_cols-1), (x-1, num_cols-1), (x+1, num_cols-2), (x, num_cols-2), (x-1, num_cols-2)]
    
    # MIDDLE (everything else)
    else:
        return [(x-1, y), (x+1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)] 
    
def test_neighbors(board):
    # CORNERS
        # top left
    return [
        sorted(neighbors(board, 0, 0)) == sorted([(0, 1),(1, 0),(1, 1)]) 
    and 
        # top right
    sorted(neighbors(board, 8, 0)) == sorted([(7, 0), (7, 1), (8,1)])
    and
        # bottom left
    sorted(neighbors(board, 0, 8)) == sorted([(0, 7), (1, 7), (1, 8)])
    and
        # bottom right
    sorted(neighbors(board, 8, 8)) == sorted([(8, 7), (7, 7), (7, 8)])
    and
    # EDGES
        # top
    sorted(neighbors(board, 4, 0)) == sorted([(3, 0), (3, 1), (4, 1), (5, 1), (5, 0)]) 
    and
        # bottom
    sorted(neighbors(board, 4, 8)) == sorted([(3, 8), (3, 7), (4, 7), (5, 7), (5, 8)]) 
    and
        # left
    sorted(neighbors(board, 0, 4)) == sorted([(0, 3), (1, 3), (1, 4), (1, 5), (0, 5)])
    and
        # right
    sorted(neighbors(board, 8, 4)) == sorted([(8, 3), (7, 3), (7, 4), (7, 5), (8, 5)])
    and
    # MIDDLE
    sorted(neighbors(board, 5, 5)) == sorted([(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]) 
    ]

# generate (print) minesweeper board, fill with 0's
def generate_board(rows, cols, num_of_mines):
    board = [[0 for i in range(cols)] for j in range(rows)]
    plant_mines(board, num_of_mines)
    count_mines(board)
    return board

# testing
#board = generate_board(4, 4, 2)
#print(board)

"""
from pathlib import Path
from string import Template

def generate_html(count_matrix, game_board_matrix): # count_matrix, game_board_matrix
    joined_matrix = join_matrix(count_matrix, game_board_matrix)
    # read text from html file & store as string
    html_template = Path('table.html').read_text()
    template = Template(html_template)
    # make 2 different matrices 
    html_count_table = generate_html_table(count_matrix)
    html_joined_table = generate_html_table(joined_matrix)
    return template.substitute(count_table = html_count_table,
                               game_board_table = html_joined_table)

def generate_html_table(matrix):
    content = ""
    num_rows = len(matrix)
    html_row = Path('row.html').read_text()
    template = Template(html_row)
    for i in range (num_rows):
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
        case -2: # black square Unicode
           cell = "&#x25A0"
           cell_color = "black"
        case -1: # mine Unicode or img
           cell = "&#128163"
           cell_color = "black"
        case 0: # blank
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
    #testing
    #print(join_matrix(count_matrix, game_board_matrix))
    html = generate_html(count_matrix, board_matrix)
    with open("page.html", "w") as file: # w is for writing in new file
        file.write(html)
"""
# print(join_matrix(count_matrix, game_board_matrix))
#create_page(count_matrix, game_board_matrix)
