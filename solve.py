from check import check
from svgDict import svg


def backtrack(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] != "":
                continue
            else:
                dfs(board)
    return board


def findEmpty(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == "":
                return row, column
    return -1, -1


def dfs(board):
    row, column = findEmpty(board)
    if row == -1 and column == -1:
        return True
    for k in range(1, 10):
        if check(str(k), row, column, board):
            board[row][column] = str(k)
            if dfs(board):
                return True
            board[row][column] = ""
    return False
