def placeQueens(board):
    n = tmp = 1
    for row in range(len(board) // 2):
        for col in range(len(board[row])):
            if n == 0: 
                board[row][col] = 'Q'
                break
            n -= 1
        n = tmp + n + 2
        tmp = n
    n = tmp = 0
    for row in range(len(board) // 2, len(board)):
        for col in range(len(board[row])):
            if n == 0: 
                board[row][col] = 'Q'
                break
            n -= 1
        n = tmp + n + 2
        tmp = n
    return board

def solveNQueens(board):
    brd = placeQueens(board)

    for i in brd:
        print(i)

# board = [[0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0]]
board = [['.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]
solveNQueens(board)