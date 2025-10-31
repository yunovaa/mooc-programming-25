# Write your solution here

def row_correct(sudoku: list, row_no: int):
    row_num = sudoku[row_no]
    for i in range(1, 10):
        if row_num.count(i)>1:
            return False
    return True