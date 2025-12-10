# Write your solution here
def row_sums(my_matrix: list):
    for ind, row in enumerate(my_matrix):
        s = sum(row)
        my_matrix[ind].append(s)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)