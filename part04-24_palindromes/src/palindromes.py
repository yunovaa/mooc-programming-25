# Write your solution here
def palindromes(s):
    return s == s[::-1]

while True:
    word = input('Please type in a palindrome: ')
    if palindromes(word):
        print(f'{word} is a palindrome!')
        break
    print("that wasn't a palindrome")
