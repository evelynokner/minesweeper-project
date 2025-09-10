# generate (print) minesweeper board, fill with 0's
def generate_board(rows, cols, num_of_mines):    
    board = [[0 for i in range(cols)] for j in range(rows)]
    plant_mines(board, num_of_mines)
    count_mines(board)
    return board

# testing 
''' board = generate_board(4, 4, 2)
print(board) '''

def plant_mines(board, num_of_mines):
    import random

    rows = len(board)
    cols = len(board[0])
    
    #while loop to check for duplicate coordinates
        # n = 0, while n <= num_of_mines: gen rand nums
        # if board[r][c] = -1, do nothing
        # else: board[r][c] = -1, n=n+1
    n = 0
    while n <= num_of_mines:
        #run random num generating num_of_mines times
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
    for (x, y) in  neighbors(board, x, y):
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

