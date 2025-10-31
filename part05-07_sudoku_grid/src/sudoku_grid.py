def row_correct(sudoku: list, row_no: int):
    row_num = sudoku[row_no]
    for i in range(1, 10):
        if row_num.count(i)>1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    col_num = [col[column_no] for col in sudoku]
    
    for i in range(1, 10):
        if col_num.count(i)>1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    grid = [item for row in sudoku[row_no:row_no+3] for item in row[column_no:column_no+3]]

    for i in range(1, 10):
        if grid.count(i)>1:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    list = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    for i in range(0, 9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False
    for j in list:
        if not block_correct(sudoku, j[0], j[1]):
            return False
    return True



