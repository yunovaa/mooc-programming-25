# Copy here code of line function from previous exercise

def square_of_hashes(size):
    for i in range(size):
        line(size, "#")

def line(number, string):
    if string == '':
        string='*'
    print(number*string[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
