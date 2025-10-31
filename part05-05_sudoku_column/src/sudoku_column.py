# Write your solution here


def column_correct(sudoku: list, column_no: int):
    col_num = [col[column_no] for col in sudoku]
    
    for i in range(1, 10):
        if col_num.count(i)>1:
            return False
    return True