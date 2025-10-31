
def shape(n_1, s_1, n_2, s_2):
    for i in range(1, n_1 + 1):
        line(i, s_1)

    for i in range(n_2):
        line(n_1, s_2)
# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if string == '':
        string='*'
    print(number*string[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")