def check(value, row, column, board):
    return check_row(value, row, column, board) and \
        check_column(value, row, column, board) and \
        check_cell(value, row, column, board)


def check_row(value, row, column, board):
    for i in range(9):
        if board[row][i] == value and i != column:
            return False
    return True


def check_column(value, row, column, board):
    for i in range(9):
        if board[i][column] == value and i != row:
            return False
    return True


def check_cell(value, row, column, board):
    row_block = row // 3
    column_block = column // 3
    for r in range(3*row_block, 3*row_block + 3):
        for c in range(3*column_block, 3*column_block + 3):
            if r == row and column == c:
                continue
            elif board[r][c] == value:
                return False
    return True
