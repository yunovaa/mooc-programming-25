# Write your solution here
def invert(s):
    temp = {key: value for value, key in s.items()}
    s.clear()
    s.update(temp)
