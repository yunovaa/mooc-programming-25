# Write your solution here
l = []
while True:
    word = input('Word')
    if word in l:
        print(f'You typed in {len(l)} different words')
        break
    l.append(word)