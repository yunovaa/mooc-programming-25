# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return ' '.join([''.join(letter for letter in word if letter not in forbidden) for word in string.split()])

