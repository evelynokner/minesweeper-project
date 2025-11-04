# flood fill code
# https://www.geeksforgeeks.org/dsa/flood-fill-algorithm/

import minesweeper
count_matrix = [[0,1,1],[0,1,-1],[0,1,1]]
gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Modified for minesweeper
def dfs(gameboard, count_matrix, x, y):
    print(f'dfs with {x} and {y}')

    # openedCell = 1
    openedCell = minesweeper.openedCell
    # closedCell = 0
    closedCell = minesweeper.closedCell
    
    # if cell has an adjacent mine, return (if count is not 0)

    # if [x][y] is opened, do nothing
    # if [x][y] == 1 
    if(gameboard[x][y] == openedCell):
        print("bye")
        return
    # if cell isn't open, mark as open
    #if(gameboard[x][y] == closedCell):
    else:
        print("marked as open")
        gameboard[x][y] = openedCell

    # ISSUE : only opening immediate neighbors
    neighbours = minesweeper.neighbors(count_matrix, x, y)
    print(f"neighbours: {neighbours}")
    for (nx, ny) in neighbours:
        # open neighbour cells
        print(f'opening cell: {nx} {ny}')
        gameboard[nx][ny] = openedCell
        # check count
        # if neighbour has no adjacent mines, perform dfs (open cell & adjacent cells)
        # that means that the value at neighbour coordinates is 0 in count_matrix 
        if count_matrix[nx][ny] == 0:
            print("count is 0")
            dfs(gameboard, count_matrix, nx, ny)

# test method for changing values in an array
arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
def test (arr1, arr2):
    arr1[0] = 100
    arr1[1] = 44
    arr2[2] = 70
    print(arr1, arr2)

'''
if __name__ == "__main__":
    # Input initialization
    matrix = [[1, 1, 1, 0],
              [0, 1, 1, 1],
              [1, 0, 1, 1]]
    
    # initial matrix
    for row in matrix:
        print(" ".join(map(str, row)))

    print("\n")
    sr, sc, newColor = 1, 2, 2

    # Perform flood fill
    result = floodFill(matrix, sr, sc, newColor)

    # output grid
    for row in result:
        print(" ".join(map(str, row)))
'''