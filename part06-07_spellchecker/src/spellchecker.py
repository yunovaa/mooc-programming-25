# write your solution here
sentence = input('Write text: ').split()

with open('wordlist.txt') as f:
    words = [line.strip() for line in f.readlines()]
    for i in range(len(sentence)):
        word = sentence[i]
        if not(word.lower() in words): 
            word = f'*{word}*'
            sentence[i] = word

print(' '.join(sentence))