# Write your solution here

iteration = int(input('How many items: '))
l = []
for i in range(1, iteration + 1):
    number = int(input(f'Item {i}: '))
    l.append(number)

print(l)