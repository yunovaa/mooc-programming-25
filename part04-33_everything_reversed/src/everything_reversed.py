# Write your solution here

def everything_reversed(l):
    a = []
    for item in l:
        a.insert(0, item[::-1])    
    return a
