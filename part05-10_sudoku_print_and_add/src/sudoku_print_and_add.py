# Write your solution here
def print_sudoku(sudoku: list):
    for k in range(0, 9):
        val = ''
        i = sudoku[k]
        for j in range(0, 9):
            if i[j] == 0:
                val += '_ '
            else:
                val += f'{i[j]} '
            if (j+1) == 9:
                val += ''
            elif (j+1)%3 == 0:
                val+= ' '
        print(val)
        if (k+1)%3 == 0:
            print('')

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    return sudoku
