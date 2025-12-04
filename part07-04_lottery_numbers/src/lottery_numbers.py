# Write your solution here
import random
def lottery_numbers(amount: int, lower: int, upper: int):
    l = []
    while len(l)<amount:
        number = random.randint(lower, upper)
        if number in l:
            continue
        l.append(number)
    return sorted(l)