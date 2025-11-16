# consts representing if a cell is opened or closed in gameboard matrix
# uppercase for constants
OPENED_CELL = 1
#global OPENED_CELL
CLOSED_CELL = 0
#global CLOSED_CELL

WON = 1
LOST = 0

# hard-coded boards for testing
# gameboard starts closed

# TODO: populate closed gameboard in forloop

gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
count_matrix = [[0,1,1],[0,1,-1],[0,1,1]]

gameboard2 = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
count_matrix2 = [[0, 0, 0, 0, 0],
                [1, 2, 2, 2, 1],
                [-1, 2, -1, -1, 2],
                [1, 2, 2, 3, -1],
                [0, 0, 0, 1, 1]]
