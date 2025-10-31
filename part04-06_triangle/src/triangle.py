# Copy here code of line function from previous exercise

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1, size + 1):
        line(i, '#')

def line(number, string):
    if string == '':
        string='*'
    print(number*string[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
