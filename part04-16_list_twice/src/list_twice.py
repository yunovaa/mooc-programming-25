# Write your solution here
l = []
while True:
    item = int(input('New item: '))
    if item == 0:
        print('Bye!')
        break
    l.append(item)
    print(f'The list now: {l}')
    print(f'The list in order: {sorted(l)}')