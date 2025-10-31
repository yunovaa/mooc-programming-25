# Write your solution here
def fact(n):
    return n*fact(n-1) if n>0 else 1

def factorials(n: int):
    return {key: fact(key) for key in range(1, n+1)}