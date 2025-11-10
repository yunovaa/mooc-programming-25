# Write your solution here

import fractions

def fractionate(amount: int):
    l = []
    for i in range(amount):
        l.append(fractions.Fraction(1, amount))

    return l