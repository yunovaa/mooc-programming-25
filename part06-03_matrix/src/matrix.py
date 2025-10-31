# write your solution here
def open_file():
    with open('matrix.txt') as f:
        return [list(map(lambda x: int(x), row.split(','))) for row in f.readlines() if row]
    
#print(open_file())

def row_sums():
    matrix = open_file()
    return [sum(row) for row in matrix] 

def row_greater():
    matrix = open_file()
    return [max(row) for row in matrix]

def matrix_sum():
    return sum(row_sums())

def matrix_max():
    return max(row_greater())

