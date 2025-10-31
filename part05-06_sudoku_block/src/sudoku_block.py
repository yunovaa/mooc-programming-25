# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    grid = [item for row in sudoku[row_no:row_no+3] for item in row[column_no:column_no+3]]

    for i in range(1, 10):
        if grid.count(i)>1:
            return False
    return True
