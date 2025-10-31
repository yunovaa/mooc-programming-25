# Write your solution here
from copy import deepcopy

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    copy_sudoku = deepcopy(sudoku)
    copy_sudoku[row_no][column_no] = number
    return copy_sudoku

