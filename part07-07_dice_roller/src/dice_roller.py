# Write your solution here
import random
def roll(die: str):
    d = {'A': [3, 3, 3, 3, 3, 6],
         'B': [2, 2, 2, 5, 5, 5],
         'C': [1, 4, 4, 4, 4, 4],}
    
    return random.choice(d[die])

def play(die1: str, die2: str, times: int):

    res1 = 0
    res2 = 0
    for i in range(times):
        a = roll(die1)
        b = roll(die2)
        if a> b:
            res1+=1
        elif a<b:
            res2+=1

    return (res1, res2, times-res2-res1)
