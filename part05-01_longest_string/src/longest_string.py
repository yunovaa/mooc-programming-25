# Write your solution here
def lenf(l):
    return len(l)

def longest(strings: list):
    strings = sorted(strings ,key=lenf)
    return strings[-1]

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))