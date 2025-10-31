# Write your solution here
def line(number, string):
    if string == '':
        string='*'
    print(number*string[0])

if __name__ == "__main__":
    line(5, "x")