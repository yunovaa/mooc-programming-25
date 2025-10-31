# Write your solution here
def spruce(number):
    print('a spruce!')
    st = '*'
    for i in range(1, 2*number, 2):
        nst = i*st
        print(nst.center(2*number-1))
    print(st.center(2*number-1))
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)