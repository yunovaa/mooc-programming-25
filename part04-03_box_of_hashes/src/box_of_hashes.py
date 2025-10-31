# Copy here code of line function from previous exercise

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")

def line(number, string):
    if string == '':
        string='*'
    print(number*string[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
