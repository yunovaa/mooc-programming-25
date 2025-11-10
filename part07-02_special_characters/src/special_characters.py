# Write your solution here

import string

def separate_characters(my_string: str):
    ass_part = ''.join(char for char in my_string if char in string.ascii_letters)
    punc_part = ''.join(char for char in my_string if char in string.punctuation)
    other_part = ''.join(char for char in my_string if not(char in string.ascii_letters or char in string.punctuation))
    return (ass_part, punc_part, other_part)

