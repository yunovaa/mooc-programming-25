# Write your solution here
import string


def change_case(orig_string: str):
    return orig_string.swapcase()


def split_in_half(orig_string: str):
    l = len(orig_string)//2
    return (orig_string[:l], orig_string[l:])


def remove_special_characters(orig_string: str):
    letters = string.ascii_letters
    numbers = string.digits
    return ''.join(letter for letter in orig_string if letter in letters 
                   or letter == ' ' or letter in numbers)