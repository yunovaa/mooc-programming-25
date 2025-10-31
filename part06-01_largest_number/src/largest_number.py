# write your solution here

def largest():
    with open('numbers.txt') as f:
        numbers = [int(line.strip()) for line in f.readlines() if line.strip()]
    return max(numbers)