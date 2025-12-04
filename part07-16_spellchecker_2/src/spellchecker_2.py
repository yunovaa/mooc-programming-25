# Write your solution here
import difflib
sentence = input('Write text: ').split()

with open('wordlist.txt') as f:
    words = [line.strip() for line in f.readlines()]
    suggestions = {}
    for i in range(len(sentence)):
        word = sentence[i]
        if not(word.lower() in words): 
            suggestions[word] = difflib.get_close_matches(word, words)
            word = f'*{word}*'
            sentence[i] = word

print(' '.join(sentence))
print('suggestions: ')
for word in suggestions:
    print(f'{word}: {', '.join(suggestions[word])}')