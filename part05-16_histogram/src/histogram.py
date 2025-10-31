# Write your solution here
def histogram(str):
    dct = {}
    for letter in str:
        dct[letter] = dct.get(letter, 0) + 1
    
    for key, value in dct.items():
        print(f"{key} {value*'*'}")

