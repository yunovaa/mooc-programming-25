# Write your solution here
import random
def words(n: int, beginning: str):
    l = []
    with open('words.txt') as file:
        words = [word for word in file.readlines() if word.startswith(beginning)]
    
    if len(words) < n:
        raise ValueError
    else:
        while len(l)<n:
            word = random.choice(words)
            if not word in l:
                l.append(word)

    return l