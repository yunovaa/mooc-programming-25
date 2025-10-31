# Write your solution here

def no_vowels(my_string: str):
    a = ''
    for i in my_string:
        if i not in ['a', 'o', 'u', 'e', 'i']:
            a+=i
    return a