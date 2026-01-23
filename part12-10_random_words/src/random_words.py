# Write your solution here:
import random as rn
def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        yield ''.join(rn.choice(characters) for i in range(length))
