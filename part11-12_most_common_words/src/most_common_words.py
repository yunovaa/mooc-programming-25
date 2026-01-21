# WRITE YOUR SOLUTION HERE:
import string
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        lines = [word.strip(string.punctuation) for words in f.readlines() for word in words.split()]
        return {word: lines.count(word) for word in lines if lines.count(word)>=lower_limit}
    
