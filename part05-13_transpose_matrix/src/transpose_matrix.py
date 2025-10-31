# Write your solution here
def transpose(matrix: list) -> list:
    ln = len(matrix)
    for i in range(ln):
        for j in range(i + 1, ln): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

